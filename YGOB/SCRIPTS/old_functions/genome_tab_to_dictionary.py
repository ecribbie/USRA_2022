#!/usr/bin/python

import re

#will want to have a way to input desired file but for now using directly ygob_testfile.txt

f=open("species_genome_tabs/Suvarum_genome.txt",'r')
raw=f.readlines()
f.close()

author="Scannell 2011"

#Create nested dictionary for the species genes then direction (dir), similarity sentence (sim) and start and end coordinates (start) (end)
#This is for the basic layout of species genomes see link:ygob.ucd.ie > genome sequences > README > section (2) the delimiter between columns when copied to txt is \\t
species={}
for i in range(len(raw)):
  x=repr(raw[i]).split('\\t')
  species[x[0]]={}
  species[x[0]]['dir']=x[1]
  species[x[0]]['sim']=x[8].lstrip()
  species[x[0]]['start']=x[2]
  species[x[0]]['end']=x[3]

print(species[repr(raw[0]).split('\\t')[0]])
print(species[repr(raw[1]).split('\\t')[0]])
print(species[repr(raw[59]).split('\\t')[0]])


#Convert similarity columns to gene mathches.


if author=="Gordon":
  for gene in species:
    if len(species[gene]['sim'].split(" "))==1 and re.search("Y",species[gene]['sim']):
      species[gene]['match']=species[gene]['sim'].removesuffix("\\n'")
    elif len(species[gene]['sim'].split(" "))==1 and re.search("Anc",species[gene]['sim']):
      species[gene]['match']=species[gene]['sim'].removesuffix("\\n'")
    elif re.search("Anc",species[gene]['sim']):
      ind=[species[gene]['sim'].split(" ").index(i) for i in species[gene]['sim'].split(" ") if 'Anc' in i]
      ind=[x+1 for x in ind]
      species[gene]['match']=species[gene]['sim'].split(" ")[ind[0]].removesuffix("\\n'")
    else:
      species[gene]['match']=None

elif author=="Scannell 2011":
  for gene in species:
    if re.search(" ",species[gene]['sim']):
      if len(species[gene]['sim'].split(" "))==2 and re.search("Y",species[gene]['sim']):
        species[gene]['match']=species[gene]['sim'].split(" ")[0].removesuffix("\\n'")
      else:
        species[gene]['match']=None
    else:
      species[gene]['match']=None


print('---------------------------------------------')
print(species[repr(raw[0]).split('\\t')[0]])
print(species[repr(raw[1]).split('\\t')[0]])
print(species[repr(raw[59]).split('\\t')[0]])
