#!/usr/bin/python import re

import re
import timeit
import urllib.request



start_file=timeit.default_timer()



f=open("../Additional_files/Pillars.txt")
pillars=f.readlines()
f.close()



f=urllib.request.urlopen('http://ygob.ucd.ie/ygob/data/v7-Aug2012/AA.fsa')
#AA=f.read()
#f=open("../Additional_files/AA.txt")
AA=f.readlines()
f.close()


AA_genes=[x.decode("utf-8").split(" ")[0].removeprefix(">") for x in AA if x.decode("utf-8").startswith(">")]






dict={}

for i in range(len(pillars)):
	dict[int(i+1)]={}
	dict[int(i+1)]['genes']=repr(pillars[i]).removesuffix("\\n'").removeprefix("'").split('\\t')
	dict[int(i+1)]['genes'][:]= (gene for gene in dict[int(i+1)]['genes'] if gene != "---")


stop_file=timeit.default_timer()




print("Time:",stop_file-start_file)




bad_genes=[]
bad_families=[]
for family in dict:

	for gene in dict[family]['genes']:

		if gene in AA_genes:
			None
		elif re.search("Anc_",gene):
			None
		else:
			bad_genes.append(gene)
			bad_families.append(family)

stop_loop=timeit.default_timer()

print("Time:",stop_loop-start_file)
print(bad_families)
print(bad_genes)

