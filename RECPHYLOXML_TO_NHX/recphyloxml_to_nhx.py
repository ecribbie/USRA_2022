#!/usr/bin/env python3
# coding: utf-8

"""
Convert a (set of) RecPhyloXml file(s from a directory) into the nhx format
Usage: recphyloxml_to_nhx input output_directory
- input: (str) path to a file or a directory
         if directory, all RecPhyloXml files of the directory will be converted
- output: (str) path to a directory, created if not existing

For every RecPhyloXml file <file_name>.xml that is processed, 
a NHX file <output>/<file_name>.nhx is created.

This program assumes that each RecPhyloXml file has a single species tree, 
a single gene tree and that both species and gene trees are rooted.
"""

import argparse
import inspect
import os
import sys
import xml.etree.ElementTree as ET

def get_xml_tag_prefix(xml_object):
    """
    Input:
      xml_object: parsed XML file
    Output:
      (str) XML tags prefix
    """
    root_tag = xml_object.getroot().tag
    if '}' in root_tag: prefix = '{'+root_tag.split('}')[0].strip('{')+'}'
    else: prefix = ''
    return prefix

def find_tag(node, tag):
    """
    Input: 
      - node: xml object
      - tag: string
    Output:
      xml object: First child of node with tag 'tag'
    """
    return node.find(f'{XML_TAG_PREFIX}{tag}')

def findall_tags(node, tag):
    """
    Input: 
      - node: xml object
      - tag: string
    Output:
      list(xml_object): List of all children of node with tag 'tag'
    """
    return node.findall(f'{XML_TAG_PREFIX}{tag}')

def get_tag(node):
    """
    Input: 
      - node: xml object
    Output:
      str: xml tag of node
    """
    return node.tag.replace(XML_TAG_PREFIX, '')

def get_children(node):
    """
    Input: 
      - node: xml object
    Output:
      list(xml object): List of all children of node corresponding to nodes of the tree
    """
    return [child for child in node if get_tag(child) == 'clade']

def get_event_data(event):
    """
    Input: 
      - event: xml object encoding a reconciliation event
    Output:
      dict: type and species of the reconciliation event
    Assumption: 
      xml tag eventsRec has a single child defining the event type and species
    """
    event_type = get_tag(event[0])
    event_species = event[0].get('speciesLocation')
    return {'type': event_type, 'species': event_species}

def find_trees(xml_object, tree_type):
    """
    Input:
      - xml_object: xml object obtained from parsing a full XML file
      - tree_type: str
    Output:
      - list(xml object): list of xml object corresponding to the root of
                          all trees of the given type
    """
    trees_aux = findall_tags(xml_object.getroot(), tree_type)
    trees = []
    for tree_aux in trees_aux:
        # RecPhyloXml format: a tree start by a tag describing its type
        # then a nested phylogeny tag then the first node (if rooted)
        # or set of nodes if unrooted
        tree_phyl = find_tag(tree_aux, 'phylogeny')
        trees.append(findall_tags(tree_phyl, 'clade'))
    return trees


def declone_tag(xml_tag):
    """
    Input:
      - xml_tg: str encoding a speciation event in RecPhyloXml
    Output:
      - str: correspondign event in DeClone format
    """
    XMLTAG_2_DECLONETAG = {
        'speciation': 'Spec',
        'duplication': 'GDup',
        'loss': 'GLos',
        'leaf': 'Extant'
    }
    return XMLTAG_2_DECLONETAG[xml_tag]


def read_file(input_file):
    """
    Read input file and if it is a valid RecPhyloXml file with a single rooted species tree
    and a single reconciled gene tree, returns a pair '',(spTree, recGeneTree) of xml objects 
    for the root node of each tree.
    Otherwise returns None and an error message.
    """
    global XML_TAG_PREFIX
    # Checking the file name ends with .xml
    if not input_file.endswith('.xml'):
        return f'File {input_file} does not have suffix .xml', None
    # Parsing the input file
    try:
        xml_object = ET.parse(input_file)
    except ET.ParseError as exception_parsing:
        return f'File {input_file} is not an XML file', None
    # Checking the parsed XML object is of type RecPhyloXml
    XML_TAG_PREFIX = get_xml_tag_prefix(xml_object)
    if get_tag(xml_object.getroot()) != 'recPhylo': 
        return f'File {input_file} is not a RecPhyloXml file', None
    # Parsing the species tree
    spTrees = find_trees(xml_object, 'spTree')
    if len(spTrees) > 1:
        return f'File {input_file} has more than one species tree', None
    spTree = spTrees[0]
    if len(spTree) > 1:
        return f'File {input_file} species tree is unrooted', None
    # Parsing the gene tree
    recGeneTrees = find_trees(xml_object, 'recGeneTree')
    if len(recGeneTrees) > 1:
        return f'File {input_file} has more than one gene tree', None
    recGeneTree = recGeneTrees[0]
    if len(recGeneTree) > 1:
        return f'File {input_file} gene tree is unrooted', None
    return f'{input_file} is a valid RecPhyloXml file', (spTree[0], recGeneTree[0])
        

def read_spTree(xml_tree_root):
    """
    Input:
      - xml_tree_root: xml node corresponding to the root of a species tree
    Output:
      - dict: dictionary species name -> species integer ID
    """
    def read_xml_spTree_aux(node, species_id_dict, species_id):
        """
        Recursive (depth-first) function updating the dictionary 
        and returning the next available species ID
        """
        name = find_tag(node, 'name').text
        species_id_dict[name] = species_id        
        children = get_children(node)
        for child in children:
            species_id = read_xml_spTree_aux(child, species_id_dict, species_id+1)
        return species_id
    
    species_id_dict = {}
    _ = read_xml_spTree_aux(xml_tree_root, species_id_dict, 0)
    return species_id_dict

def convert_recGeneTree(xml_tree_root, node_id_offset, species_id_dict):
    """
    Converting a RecPhyloXml reconciled gene tree into a Newick string
    Input:
      - xml_tree_root: xml object encoding the root node of a reconciled gene tree
      - node_id_offset: (integer) offset to labels the gene tree nodes
      - species_id_dict: (dict) dictionary species name -> species integer ID
    Output:
      - integer, str: next gene tree node ID available, nhx string
    """
    def convert_recGeneTree_aux(node, nhx_str, node_id):
        """
        Recursive (depth-first) function
        """
        # Recording reconciliation featues of current node
        name = find_tag(node, 'name').text
        event = get_event_data(find_tag(node, 'eventsRec'))
        event_species, event_type = event['species'], declone_tag(event['type'])
        if event_type == 'duplication': is_duplication = 'Y'
        else: is_duplication = '?'
        event_species_id = species_id_dict[event_species]
        # Bulding nhx string for current node
        nhx_tag = f'[&&NHX:D={is_duplication}:Ev={event_type}:S={event_species_id}:ND={node_id}]'
        nhx_name = f'{name}|{event_species}:1.0'
        # Recursive calls on children
        children = get_children(node)
        nhx_str_subtrees = [] # List of nhx strings of children subtrees
        for child in children:        
            node_id, nhx_str_subtree = convert_recGeneTree_aux(child, '', node_id+1)
            nhx_str_subtrees.append(nhx_str_subtree)
        # Aggregating nhx subtrees strings
        if len(children) > 0:
            nhx_str_aux = f'({",".join(nhx_str_subtrees)})'
        else:
            nhx_str_aux = ''
        nhx_str_aux += f'{nhx_name}{nhx_tag}'
        return node_id, f'{nhx_str}{nhx_str_aux}'
    
    next_node_id, nhx_str = convert_recGeneTree_aux(xml_tree_root, '', node_id_offset)
    return f'{nhx_str};', next_node_id

def process_RecPhyloXml_trees(spTree, recGeneTree, output_file, node_id_offset):
    """
    Processing a RecPhyloXml object to write a NHX file
    Input:
      - xml_object: parsed RecPhyloXml file
      - output_file: (str) path to the output NHX file
      - node_id_offset: (integer) offset to labels the gene tree nodes
    """
    # Reading species tree to create the dictionary of species ID
    species_id_dict = read_spTree(spTree)  
    # Reading and converting gene tree
    output = open(output_file, 'w')
    next_node_id = node_id_offset    
    nhx_str, current_node_id = convert_recGeneTree(recGeneTree, next_node_id, species_id_dict)
    output.write(f'{nhx_str}')
    output.close()
    return current_node_id + 1


def main(input: 'Input (RecPhyloXml file or directory containing some RecPhyloXml files)',
         output_dir: 'Directory where the nhx files are written'): 
    """
    Convert either a RecPhyloXml file or all the RecPhyloXml files in a directory to the nhx format
    The nhx files have the same basename than the RecPhyloXml files and are written in output_dir
    """
    input_files = []
    if os.path.isfile(input): input_files = [input]            
    elif os.path.isdir(input):
        input_files = [os.path.join(input, input_file) for input_file in os.listdir(input) if input_file.endswith('.xml')]
    else:
        print('ERROR f{input} is neither a file nor  directory')
        sys.exit(1)

    next_node_id=0
    for input_file in input_files:
        # Reading the file
        msg, trees = read_file(input_file)
        if trees is None:
            print(f'WARNING {msg}')
        else:
            (spTree, recGeneTree) = trees
            input_file_basename = os.path.basename(input_file)
            output_file_basename = input_file_basename.replace('.xml', '.nhx')
            output_file = os.path.join(output_dir, output_file_basename)
            next_node_id = process_RecPhyloXml_trees(spTree, recGeneTree, output_file, next_node_id)
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=inspect.getdoc(main))
    parser.add_argument('input', help='Input (RecPhyloXml file or directory containing RecPhyloXml files)')
    parser.add_argument('output_dir', help='Directory where the nhx files are written')
    args = parser.parse_args()
    main(** vars(args))       

