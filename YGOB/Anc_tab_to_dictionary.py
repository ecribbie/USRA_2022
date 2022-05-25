#!/usr/bin/python

import re

#will want to have a way to input desired file but for now using directly ygob_testfile.txt

f=open("species_genome_tabs/Anc_genome.txt",'r')
raw=f.readlines()
f.close()

#Create nested dictionary for the species genes then direction (dir), similarity sentence (sim) and start and end coordinates (start) (end)
#This is for the basic layout of species genomes see link:ygob.ucd.ie > genome sequences > README > section (2) the delimiter between columns when copied to txt is \\t
species={}
for i in range(len(raw)):
  x=repr(raw[i]).split('\\t')
  species[x[0]]={}
  species[x[0]]['dir']=x[1]


print(species[repr(raw[0]).split('\\t')[0]])
print(species[repr(raw[1]).split('\\t')[0]])
print(species[repr(raw[59]).split('\\t')[0]])

