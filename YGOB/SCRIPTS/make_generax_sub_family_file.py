import sys

f=open(sys.argv[1])
full=f.readlines()
f.close()

keep=sys.argv[2].split(",")
for i in range(len(keep)):
	keep[i]=int(keep[i])

g=open(sys.argv[3],'w')

g.write(full[0])

for line_num in range(len(full)):
	line=full[line_num]
	if line.startswith("- ") and len(line.split(" ")[1].removesuffix('\n'))>0:
		if int(line.split(" ")[1].removesuffix('\n')) in keep:
			for j in range(4):
				g.write(full[line_num+j])


g.close()

