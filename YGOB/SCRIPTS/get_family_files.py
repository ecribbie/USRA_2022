#!/bin/bash

import functions as f
from importlib import reload
reload(f);
import itertools



Cglabrata=f.import_species('../species_genome_tabs/Cglabrata_genome.txt',"Cglabrata")
Scerevisiae=f.import_species('../species_genome_tabs/Scerevisiae_genome.txt',"Scerevisiae")
Vpolyspora=f.import_species('../species_genome_tabs/Vpolyspora_genome.txt',"Vpolyspora")
Zrouxii=f.import_species('../species_genome_tabs/Zrouxii_genome.txt',"Zrouxii")
Klactis=f.import_species('../species_genome_tabs/Klactis_genome.txt',"Klactis")
Lwaltii=f.import_species('../species_genome_tabs/Lwaltii_genome.txt',"Lwaltii")

species=[Cglabrata, Scerevisiae,Vpolyspora,Zrouxii,Klactis,Lwaltii]

pillars=f.pillar_filter('../Additional_files/pillars.txt','../Additional_files/AA.txt')
pillars={key: pillars[key]  for key in pillars.keys() if len(pillars[key]['genes'])>=3}

families=f.pillar_resort(species,pillars)

AA=f.readurl('http://ygob.ucd.ie/ygob/data/v7-Aug2012/AA.fsa')
NT=f.readurl('http://ygob.ucd.ie/ygob/data/v7-Aug2012/NT.fsa')

for i in range(len(AA)):
    AA[i]=AA[i].decode("utf-8")

for i in range(len(NT)):
    NT[i]=NT[i].decode("utf-8")
    
z=0

for fam in families:
    z=z+1
    g=open(str("".join(["../Additional_files/AA_family_files/","AA_fam_",str(z)])),'w')
    h=open(str("".join(["../Additional_files/NT_family_files/","NT_fam_",str(z)])),'w')
    
    gene_ind_AA=[ind for ind, s in enumerate(AA) if ">" in s]
    gene_ind_NT=[ind for ind, s in enumerate(NT) if ">" in s]
    
    for gene in families[fam]['genes']:
        
        match="".join([">",gene])
        indAA_t=[ind for ind, s in enumerate(AA) if match in s]
        indNT_t=[ind for ind, s in enumerate(NT) if match in s]
        if len(indAA_t)<1:
            print(gene)
        indAA=indAA_t[0]
        indNT=indNT_t[0]
        
        startAA=indAA+1
        endAA=gene_ind_AA[gene_ind_AA.index(indAA)+1]
        startNT=indNT+1
        endNT=gene_ind_NT[gene_ind_NT.index(indNT)+1]
        
        sequenceAA=AA[startAA:endAA]
        sequenceNT=NT[startNT:endNT]
        
        g.write("".join([">",gene]))
        h.write("".join([">",gene]))
        g.write("\n")
        h.write("\n")
        g.write("".join(sequenceAA))
        h.write("".join(sequenceNT))        
        g.write("\n\n")
        h.write("\n\n")
        
    g.close()
    h.close()

        
        
        
        
        
        
        
        
        