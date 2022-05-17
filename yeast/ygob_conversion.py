#!/usr/bin/python

#will want to have a way to input desired file but for now using directly ygob_testfile.txt

f=open("ygob_testfile.txt",'r')
raw=f.readlines()
f.close()

#Create nested dictionary for the species genes then direction (dir), similarity sentence (sim) and start and end coordinates (start) (end)
#This is for the basic layout of species genomes see link:ygob.ucd.ie > genome sequences > README > section (2) the delimiter between columns when copied to txt is \\t
gene={}
for i in range(len(raw)):
  x=repr(raw[i]).split('\\t')
  gene[x[0]]={}
  gene[x[0]]['dir']=x[1]
  gene[x[0]]['sim']=x[8]
  gene[x[0]]['start']=x[2]
  gene[x[0]]['end']=x[3]

print(gene[repr(raw[0]).split('\\t')[0]])
print('---------------------------------------------')
print(gene[repr(raw[1]).split('\\t')[0]])

  
