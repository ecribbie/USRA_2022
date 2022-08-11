#!/usr/bin/env python3
# coding: utf-8

"""
Convert a (set of) RecPhyloXml file(s from a directory) into the Newick format
Usage: recphyloxml_to_newick input (XML file or directory) output_directory [XML_prefix]
"""

import argparse
import inspect
import os
import sys
import xml.etree.ElementTree as ET


def find_tag(node, tag):
    """
    Input: 
      - node: xml object
      - tag: string
    Output:
      xml object: First child of node with tag 'tag'
    """
    return node.find(f'{XML_PREFIX}{tag}')

def findall_tags(node, tag):
    """
    Input: 
      - node: xml object
      - tag: string
    Output:
      list(xml object): List of all children of node with tag 'tag'
    """
    return node.findall(f'{XML_PREFIX}{tag}')

def get_tag(node):
    """
    Input: 
      - node: xml object
    Output:
      str: xml tag of node
    """
    return node.tag.replace(XML_PREFIX, '')

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

def check_RecPhyloXml(xml_object):
    """
    Input:
      - xml_object: xml object from parsing an XML file
    Output:
      - bool: True if RecPhyloXml file, False otherwise
    """
    header_tag = get_tag(xml_object.getroot())
    if header_tag == 'recPhylo':
        return True
    else:
        return False

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


def read_xml_spTree(xml_tree_root):
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


def convert_xml_recGeneTree(xml_tree_root, node_id_offset, species_id_dict):
    """
    Converting an xml reconciled gene tree into a Newic string
    Input:
      - xml_tree_root: xml object encoding the root node of a reconciled gene tree
      - node_id_offset: (integer) offset to labels the gene tree nodes
      - species_id_dict: (dict) dictionary species name -> species integer ID
    Output:
      - integer, str: next gene tree node ID available, Newick string
    """
    def read_xml_recGeneTree_aux(node, newick_str, node_id):
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
        # Bulding Newick string for current node
        newick_tag = f'[&&NHX:D={is_duplication}:Ev={event_type}:S={event_species_id}:ND={node_id}]'
        newick_name = f'{name}|{event_species}:1.0'
        # Recursive calls on children
        children = get_children(node)
        newick_str_subtrees = [] # List of Newick strings of children subtrees
        for child in children:        
            node_id, newick_str_subtree = read_xml_recGeneTree_aux(child, '', node_id+1)
            newick_str_subtrees.append(newick_str_subtree)
        # Aggregating Newick subtrees strings
        if len(children) > 0:
            newick_str_aux = f'({",".join(newick_str_subtrees)})'
        else:
            newick_str_aux = ''
        newick_str_aux += f'{newick_name}{newick_tag}'
        return node_id, f'{newick_str}{newick_str_aux}'
    
    next_node_id, newick_str = read_xml_recGeneTree_aux(xml_tree_root, '', node_id_offset)
    return f'{newick_str};', next_node_id

def process_xml_file(input_file, output_dir):
    """
    Processing a single xml file F.xml: if valid RecPhyloXml file, it 
    creates an equivalent output_dir/F.nhx Newick file
    Input:
      - input_file: (str) path to input xml file
      - output_dir: (str) path to output directory
    """
    # Parsing input file
    xml_object = ET.parse(input_file)
    if check_RecPhyloXml(xml_object):
        # Reading species tree
        spTrees = find_trees(xml_object, 'spTree')
        try:
            spTree = spTrees[0][0]
            species_id_dict = read_xml_spTree(spTree)
        except len(spTrees) > 1 or len(spTrees[0]) > 1:
            print(f'File {input_file} has more than one species tree or an unrooted species tree')
        # Opening output file
        input_file_basename = os.path.basename(input_file)
        output_file_basename = input_file_basename.replace('.xml', '.nhx')
        output_file = os.path.join(output_dir, output_file_basename)
        output = open(output_file, 'w')
        # Reading and converting gene tree(s)
        recGeneTrees = find_trees(xml_object, 'recGeneTree')
        next_node_id = 0
        for recGeneTree in recGeneTrees:
            try:
                nhx_str, next_node_id = convert_xml_recGeneTree(recGeneTree[0], next_node_id, species_id_dict)
                output.write(f'{nhx_str}\n')
            except len(recGeneTree) > 1:
                output.close()
                print(f'File {input_file} contains unrooted gene tree(s)')
        output.close()


def main(input: 'Input (RecPhyloXml file or directory containing some RecPhyloXml files)',
         output_dir: 'Directory where the Newick files are written',
         xml_prefix: 'Prefix of RecPhyloXml tags'): 
    """
    Convert either a RecPhyloXml file or all the RecPhyloXml files in a directory to the Newick format
    The Newick files have the same basename than the RecPhyloXml files and are written in output_dir
    xml_prefix: prefix of xml tags (Question: readable from the header?)
    """
    # Prefix of all XML tags
    global XML_PREFIX
    XML_PREFIX = xml_prefix

    if os.path.isfile(input):
        try:
            process_xml_file(input, output_dir)
        except not input.endswith('.xml'):
            print(f'File {input} does not have suffix .xml')
            
    elif os.path.isdir(input):
        input_files = [input_file for input_file in os.listdir(input) if input_file.endswith('.xml')]
        for input_file in input_files:
            process_xml_file(os.path.join(input, input_file), output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=inspect.getdoc(main))
    parser.add_argument('input', help='Input (RecPhyloXml file or directory containing RecPhyloXml files)')
    parser.add_argument('output_dir', help='Directory where the Newick files are written')
    parser.add_argument('--xml_prefix', default='{http://www.recg.org}', help='Prefix of RecPhyloXml tags')
    args = parser.parse_args()
    main(** vars(args))       
