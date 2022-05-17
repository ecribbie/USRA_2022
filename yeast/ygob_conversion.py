#!/usr/bin/python

#will want to have a way to input desired file but for now using directly ygob_testfile.txt
f=open("ygob_testfile.txt",'r')
raw=f.readlines()
f.close()

#gene=[None]*len(raw)
#direction=[None]*len(raw)
#similarities=[None]*len(raw)
#for i in range(len(raw)):
#  x=repr(raw[i]).split('\\t')
#  gene[i]=x[0]
#  direction[i]=x[1]
#  similarities[i]=x[8]
#print(gene[:10])
#print(direction[:10])
#print(similarities[:10])
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

  
