#!/usr/bin/python
import re

f=open("../Additional_files/Pillars.txt")
pillars=f.readlines()
f.close()

f.open("../Additional_files/AA.txt")
AA=f.readlines()
f.close()

dict={}

for i in range(len(pillars)):
	dict[int(i+1)]={}
	dict[int(i+1)]['genes']=repr(pillars[i]).removesuffix("\\n'").removeprefix("'").split('\\t')

bad=[]
for familiy in dict:
	count=0
	for gene in dict[family]['genes']:
		if not re.search(''.join(">",gene),AA):
			count=count+1
	if count !=0:
		bad.append(family)
print(bad)
		

