#!/usr/bin/python

#will want to have a way to input desired file but for now using directly ygob_testfile.txt
f=open("ygob_testfile.txt",'r')
raw=f.readlines()
f.close()

gene=[None]*len(raw)
direction=[None]*len(raw)
for i in range(len(raw)):
  x=repr(raw[i]).split('\\t')
  gene[i]=x[0]
  direction[i]=x[1]
print(gene[:10])
print(direction[:10])


  
