#!/usr/bin/python

f=open("../Additional_files/Pillars.txt")
pillars=f.readlines()
f.close()


dict={}

for i in range(len(pillars)):
	dict[int(i+1)]={}
	dict[int(i+1)]['genes']=repr(pillars[i]).removesuffix("\\n'").removeprefix("'").split('\\t')



print(dict[1]['genes'])
print("######################################################")
print(dict[2]['genes'])
