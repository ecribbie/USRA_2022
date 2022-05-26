#!/usr/bin/python
import re

f=open("../Additional_files/Pillars.txt")
pillars=f.readlines()
f.close()

f=open("../Additional_files/NT.txt")
NT=f.readlines()
f.close()

dict={}
# len(pillars)
for i in range(10):
	dict[int(i+1)]={}
	dict[int(i+1)]['genes']=repr(pillars[i]).removesuffix("\\n'").removeprefix("'").split('\\t')
	dict[int(i+1)]['genes'][:]= (gene for gene in dict[int(i+1)]['genes'] if gene != "---")


badgene=[]
bad=[]
for family in dict:
	count=0
	for gene in dict[family]['genes']:
		for line in NT:
			if re.search(''.join([">",gene]),line):
				count=count+1
			if count !=0:
				break
		if count==0:
			badgene.append(gene)
			bad.append(family)
			break
	
print(bad)
		
print(badgene)
