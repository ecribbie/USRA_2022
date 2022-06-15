import sys
import functions as f
from copy import deepcopy

species={}


pil_f=sys.argv[1]
AA_f=sys.argv[2]
map_f=sys.argv[3]
AA_genes_f=sys.argv[4]

f_open=open(map_f)
mapping=f_open.readlines()
f_open.close()


for line in mapping:
	if line.split(" ")[1].removesuffix("\n") in species:
		species[line.split(" ")[1].removesuffix("\n")].append(line.split(" ")[0])
	else:
		species[line.split(" ")[1].removesuffix("\n")]=[line.split(" ")[0]]

pillars=f.pillar_filter(pil_f,AA_genes_f)


pillars_keep=deepcopy(pillars)

for family in pillars:
	for gene in pillars[family]['genes']:
		count=0
		for specie in species:
			if gene in species[specie]:
				count=count+1
				break
		if count==0:
			pillars_keep[family]['genes'].remove(gene)

families= {key: pillars_keep[key]  for key in pillars_keep.keys() if len(pillars_keep[key]['genes'])>=3}



print("length of families is:",len(families))



g=open('../DATA/desired_pillar.txt','w')

for fam in families:
	g.write(" ".join(pillars[fam]['genes']))
	g.write("\n")

g.close()
