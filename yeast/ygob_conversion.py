#!/usr/bin/python

#will want to have a way to input desired file but for now using directly ygob_testfile.txt
f=open("ygob_testfile.txt",'r')
raw=f.readlines()
f.close()

gene=[]
direction=[]
for i in range len(raw):
  x=raw[i]
  gene[i]=x.split('/')[0]
  direction[i]=x.split('/')[1]
print(gene[:10])
print(direction[:10])

  
