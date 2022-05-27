#!/usr/bin/python

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
      species[x[0]]={}
      species[x[0]]['dir']=x[1]
      species[x[0]]['start']=x[2]
      species[x[0]]['end']=x[3]
      species[x[0]]['seq']=x[5]
    return species



def import_ancestor(url):    
    raw=readurl(url)

    #Create nested dictionary for the species genes then direction (dir), and start and end coordinates (start) (end)
    
    #This is for the basic layout of species genomes see link:ygob.ucd.ie > genome sequences > README > section (2) the delimiter between columns when copied to txt is \\t
    
    
    species={}
    for i in range(len(raw)):
      x=repr(raw[i].decode("utf-8")).split('\\t')
      species[x[0]]={}
      species[x[0]]['dir']=x[1]
      species[x[0]]['seq']=x[3]
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


def family_lengths(families):
    lengths=[]
    dist=[0]*20
    for i in families:
        lengths.append(len(families[i]['genes']))
    for i in range(1,21):
        dist[i-1]=lengths.count(i)
        
    return(dist)

