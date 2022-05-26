#!/usr/bin/python import re

import re

f=open("../Additional_files/Pillars.txt")
pillars=f.readlines()
f.close()


import urllib.request

f=urllib.request.urlopen('http://ygob.ucd.ie/ygob/data/v7-Aug2012/AA.fsa')
#AA=f.read()
#f=open("../Additional_files/AA.txt")
AA=f.readlines()
f.close()

print(AA[0].decode("utf-8"))
print(AA[1].decode("utf-8"))

AA_genes=[x.decode("utf-8").split(" ")[0].removeprefix(">") for x in AA if x.decode("utf-8").startswith(">")]



dict={}

# len(pillars)
for i in range(1,10):
	dict[int(i+1)]={}
	dict[int(i+1)]['genes']=repr(pillars[i]).removesuffix("\\n'").removeprefix("'").split('\\t')
	dict[int(i+1)]['genes'][:]= (gene for gene in dict[int(i+1)]['genes'] if gene != "---")


bad_genes=[]
bad_families=[]
for family in dict:

	for gene in dict[family]['genes']:

		if gene in AA_genes:
			None
		else:
			bad_genes.append(gene)
			bad_families.append(family)


print(bad_families)
print(bad_genes)
