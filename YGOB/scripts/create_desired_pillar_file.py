import sys
import functions as f

species={}

AA_f=sys.argv[2]
pil_f=sys.argv[1]

map_f=sys.argv[3]

f_open=open(map_f)
file=f_open.readlines()
f_open.close()

for line in file:
	if line.split(" ")[1] in species:
		species[line.split(" ")[1]].append(line.split(" ")[0])
	else:
		species[line.split(" ")[1]]=[line.split(" ")[0]]



pillars=f.pillar_filter(pil_f,AA_f)

pillars={key: pillars[key]  for key in pillars.keys() if len(pillars[key]['genes'])>=3}

families=f.pillar_resort(species,pillars)

print("about to open output file \n"

g=open('desired_pillar.txt','w')
for fam in pillars:
    g.write(" ".join(pillars[fam]['genes']))
    if int(fam)%100==0:
        print("reached fam",fam)

g.close()
