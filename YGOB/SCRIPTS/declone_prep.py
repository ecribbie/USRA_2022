import sys

f=open(sys.argv[1])
f1=f.readlines()
f.close()
g=open(sys.argv[2])
f2=g.readlines()
g.close()
species={}
nextspecie=0
nextid=0
trees=[f1,f2]
trees[0]=f1[0]
trees[1]=f2[0]
for k in range(len(trees)):
	tree=trees[k]
	pieces=tree.split(":")
	for i in range(len(pieces)):
		parts=pieces[i]
		if "S=" in parts:
			specie=parts
			if specie.replace("S=",'') in species:
				parts=''.join(["S=",species[specie.replace("S=",'')]])
			else:
				parts=''.join(["S=",str(nextspecie)])
				species[specie.replace("S=",'')]=str(nextspecie)
				nextspecie+=1
		if "ND=" in parts:
			NDparts=parts.split("]")
			NDpart=NDparts[0].split("=")
			NDpart[1]=str(nextid)
			NDparts[0]='='.join(NDpart)
			parts=']'.join(NDparts)
			nextid+=1
		pieces[i]=parts
	trees[k]=':'.join(pieces)

g=open(''.join([sys.argv[1].split(".")[0],"_declone_ready.nhx"]),'w')
g.write(trees[0])
g.close()
g=open(''.join([sys.argv[2].split(".")[0],"_declone_ready.nhx"]),'w')
g.write(trees[1])
g.close()

