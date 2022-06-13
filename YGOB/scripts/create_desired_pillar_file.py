import sys
import functions as f

species=

pillars=f.pillar_filter(sys.argv[1],sys.argv[2])

pillars={key: pillars[key]  for key in pillars.keys() if len(pillars[key]['genes'])>=3}

families=f.pillar_resort(species,pillars)

g=open('desired_pillar.txt','w')
for fam in pillars:
    g.write(" ".join(pillars[fam]['genes']))

g.close()
