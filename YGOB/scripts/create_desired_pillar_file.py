import sys
import functions as f

species={}


pil_f=sys.argv[1]
AA_f=sys.argv[2]
map_f=sys.argv[3]
AA_genes_f=sys.argv[4]

f_open=open(map_f)
mapping=f_open.readlines()
f_open.close()


for line in mapping:
	if line.split(" ")[1] in species:
		species[line.split(" ")[1]].append(line.split(" ")[0])
	else:
		species[line.split(" ")[1]]=[line.split(" ")[0]]


pillars=f.pillar_filter(pil_f,AA_genes_f)

families=f.pillar_resort(species,pillars,3)


g=open('desired_pillar.txt','w')

for fam in families:
    g.write(" ".join(pillars[fam]['genes']))
    g.write("\n")
    
g.close()
