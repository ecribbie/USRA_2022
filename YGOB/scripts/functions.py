#!/usr/bin/python

import math


def readurl(url):
    import urllib.request as ur
    f=ur.urlopen(url)
    file=f.readlines()
    f.close()
    return(file)

def import_species(url):
    raw=readurl(url)

    #Create nested dictionary for the species genes then direction (dir), and start and end coordinates (start) (end)
    
    #This is for the basic layout of species genomes see link:ygob.ucd.ie > genome sequences > README > section (2) the delimiter between columns when copied to txt is \\t
    
    
    species={}
    for i in range(len(raw)):
      x=repr(raw[i].decode("utf-8")).split('\\t')
      species[x[0].removeprefix("'")]={}
      species[x[0].removeprefix("'")]['dir']=x[1]
      species[x[0].removeprefix("'")]['start']=x[2]
      species[x[0].removeprefix("'")]['end']=x[3]
      species[x[0].removeprefix("'")]['seq']=x[5]
    return species



def import_ancestor(url):    
    raw=readurl(url)

    #Create nested dictionary for the species genes then direction (dir), and start and end coordinates (start) (end)
    
    #This is for the basic layout of species genomes see link:ygob.ucd.ie > genome sequences > README > section (2) the delimiter between columns when copied to txt is \\t
    
    
    species={}
    for i in range(len(raw)):
      x=repr(raw[i].decode("utf-8")).split('\\t')
      species[x[0].removeprefix("'")]={}
      species[x[0].removeprefix("'")]['dir']=x[1]
      species[x[0].removeprefix("'")]['seq']=x[3]
    return species





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


def family_lengths(families,max_size_of_family=20):
    lengths=[]
    dist=[0]*max_size_of_family
    for i in families:
        lengths.append(len(families[i]['genes']))
    for i in range(1,max_size_of_family+1):
        dist[i-1]=lengths.count(i)
        
    return(dist)


def species_fragmentation(species):
    fragmentation=[0]*len(species)
    i=0
    for specie in species:
        unique=[]
        for gene in specie:
            if specie[gene]['seq'] not in unique:
                unique.append(specie[gene]['seq'])
        fragmentation[i]=len(unique)
        i=i+1
    return(fragmentation)

def species_associations(species,pillars):
    pillars = {key: pillars[key]  for key in pillars.keys() if len(pillars[key]['genes'])>1}
    associations=[0]*len(species)
    i=0
    for specie in species:
        links=[]
        for gene in specie:
            for family in pillars:
                if gene in pillars[family]['genes'] and family not in links:
                    links.append(family)
        associations[i]=len(links)
        i=i+1
    return(associations)


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
    
    
    
def match_matrix(species,names,pillars):
    dat={}
    for i in range(len(species)):
        matches=[species_pairs(x,species[i],pillars) for x in species]
        dat[names[i]]=matches
    return(dat)
    
    
    
    
    
    
    
    
    
    
    
        