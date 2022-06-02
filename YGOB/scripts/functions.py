#!/usr/bin/python

import math
from copy import deepcopy
import re



#The readurl function takes in a url to a .txt or .tab file and reads in the contents of the file into a list where each element is a line of the text stored as a string.
def readurl(url):
    import urllib.request as ur
    
    f=ur.urlopen(url)
    file=f.readlines()
    f.close()
    
    return(file)



#The import_species function takes in the url of a file of a species genome as well as the species' name. The format for that file is as described in link:ygob.ucd.ie > genome sequences > README > section (2). This function outputs a dictionary of the species genes each of which is a dictionary containing the direction (dir) (Crick strand=0, Watson strand=1) and the start and end coordinates (start) (end) of the gene.
def import_species(url,name):
    raw=readurl(url)
   
    species={}
    species['name']=name
    
    for i in range(len(raw)):
      x=repr(raw[i].decode("utf-8")).split('\\t')
      if x[0].startswith('\"'): 
            x[0]=x[0].removeprefix('\"')
      species[x[0].removeprefix("'")]={}
      species[x[0].removeprefix("'")]['dir']=x[1]
      species[x[0].removeprefix("'")]['start']=x[2]
      species[x[0].removeprefix("'")]['end']=x[3]
      species[x[0].removeprefix("'")]['seq']=x[5]
    
    return species



#The import_ancestor file does the same as above function import_species but for the Ancestor species as it has a different file format, also described in link:ygob.ucd.ie > genome sequences > README > section (2).
def import_ancestor(url):    
    raw=readurl(url)

    species={}
    
    for i in range(len(raw)):
      x=repr(raw[i].decode("utf-8")).split('\\t')
      species[x[0].removeprefix("'")]={}
      species[x[0].removeprefix("'")]['dir']=x[1]
      species[x[0].removeprefix("'")]['seq']=x[3]
    
    return species



#The pillar_filter function takes in a url to a pillar file aswell as the AA or NT file in which it filters out pillars(families) that have genes that do not have their sequence information stored in the second file. The link to the structure of these files can be found in link:ygob.ucd.ie > genome sequences > README. This function clearly ignores ancestor genes (containing Anc_) as they do not have gene sequences. It outputs a dictionary of the families with the genes in each (genes).
def pillar_filter(pillarurl,AAurl):
       
    import re
    
    pillars=readurl(pillarurl)
    AA=readurl(AAurl)

    AA_genes=[x.decode("utf-8").split(" ")[0].removeprefix(">") for x in AA if x.decode("utf-8").startswith(">")]

    dict={}

    for i in range(len(pillars)):
        dict[int(i+1)]={}
        dict[int(i+1)]['genes']=repr(pillars[i].decode("utf-8")).removesuffix("\\n'").removeprefix("'").split('\\t')
        dict[int(i+1)]['genes'][:]= (gene for gene in dict[int(i+1)]['genes'] if gene != "---")

    bad_genes=[];   bad_families=[];   good_families=[]
    
    for family in dict:
        for gene in dict[family]['genes']:
            if gene in AA_genes:
                None
            elif re.search("Anc_",gene):
                None
            else:
                bad_genes.append(gene)
                if family not in bad_families:
                    bad_families.append(family)
    
    for key in bad_families:
        del dict[key]
    
    return(dict)



#The family_lengths function takes in a dictionary of families, output of above pillar_filter function aswell as an optional maximum size the family can be. The default is 20. It outputs a list of the number of families with each length from 1 to the maximum. Example: [3,0,4,1] would imply there where 8 families and 3 had one gene, 4 had 3 genes and 1 had 4 genes (this would assume a max input of 4, or else the list would have 16 additional zeros at the end).
def family_lengths(families,max_size_of_family=20):
    
    lengths=[]
    dist=[0]*max_size_of_family
    
    for i in families:
        lengths.append(len(families[i]['genes']))
    for i in range(1,max_size_of_family+1):
        dist[i-1]=lengths.count(i)
        
    return(dist)



#The species_fragmentation function takes in a list of species dictionaries, a list of outputs from import_species function (several different runs for different species saved into a list), and returns a list of the the number of distinct fragments for each specie.
def species_fragmentation(species):
    
    fragmentation=[0]*len(species)
    
    i=0
    for specie in species:
        unique=[]
        for gene in specie:
            if gene=='name':
                continue
            if specie[gene]['seq'] not in unique:
                unique.append(specie[gene]['seq'])
        fragmentation[i]=len(unique)
        i=i+1
        
    return(fragmentation)



# The species_associations function takes in a list of dictionaries of species (list of different outputs from import_species) as well as a dictionary of families (output of pillars_filter function). It outputs a list where each entry is the number of families that contain at least one gene of the associated species.
def species_associations(species,pillars):
    
    pillars = {key: pillars[key]  for key in pillars.keys() if len(pillars[key]['genes'])>1}
    
    associations=[0]*len(species)
    
    i=0
    for specie in species:
        links=[]
        for gene in specie:
            if gene=='name':
                continue
            for family in pillars:
                if gene in pillars[family]['genes'] and family not in links:
                    links.append(family)
        associations[i]=len(links)
        i=i+1
    
    return(associations)



# The species_pairs function takes in two specie dictionaries (output of import_species function) as well as a family dictionary (output of pillars-filter function). It outputs the number of families with a gene from each species, if there are two copies from each then that is counted as 2 families and same for 3 and so on, if there is only 1 gene from one specie and 2 from the other in the family this only counts as one pair. If the same specie is inputed in both arguments then the output is the number of families with more than one gene from the specie.
def species_pairs(speciea,specieb,pillars):
    
    pairs=0
    
    for family in pillars:
        
        counta=0
        countb=0
        countdup=0
        
        for gene in pillars[family]['genes']:
            
            if gene in speciea:
                counta=counta+1
            elif gene in specieb:
                countb=countb+1
            if gene in speciea and gene in specieb:
                countdup=countdup+0.5
            
        pairs=pairs+min(counta,countb)
        
        if math.floor(countdup)>0.5:
            pairs=pairs+1
    
    return(pairs)
    

    
# The match_matrix function takes in a list of specie dictionaries as well as the list of the specie names. The output is a dictionary of specie names with a list associated that is the number of pairs with each specie in the inputed list, incluing itself, calculated as in species_pairs function.   
def match_matrix(species,pillars):
    
    dat={}
    
    for i in range(len(species)):
        matches=[species_pairs(x,species[i],pillars) for x in species]
        dat[species[i]['name']]=matches
        
    return(dat)



#The group_pairs function takes in a list of species dictionaries (output from import_species) and a family dictionry (output of pillar_filter). It returns the total number of matches of genes that would be found in a same reconcilled family for all the given species.
def group_pairs(group,pillars):
    
    total=0
    
    for i in range(len(group)):
        for j in range(i+1,len(group)):            
            total=total+species_pairs(group[i],group[j],pillars)
            
    return(total)



#The gene_species_mapping function creates a text file where each line is a map from a gene followed by a space and then its specie it came from (GeneRax format). This will get used when reconstructing reconcilled gene trees.
def gene_species_mapping(species):
    
    f=open("gene_species_mapping_output.txt",'w')
    
    for specie in species:
        i=0
        for gene in specie:
            if gene=='name':
                continue
            f.write(' '.join([gene,specie['name']]))
            f.write("\n")
        i=i+1
    
    f.close()
    
    return("Done")
    
    

def pillar_resort(species,pil,minimum=1):
    pillars=deepcopy(pil)
    for family in pillars:
        for gene in pillars[family]['genes']:
            count=0
            for specie in species:
                if gene in specie:
                    count=count+1
            if count==0: #and not re.search("Anc_",gene)
                pillars[family]['genes'].remove(gene)
    pillars = {key: pillars[key]  for key in pillars.keys() if len(pillars[key]['genes'])>=minimum}
    return(pillars)
    
    
    
    
    
    