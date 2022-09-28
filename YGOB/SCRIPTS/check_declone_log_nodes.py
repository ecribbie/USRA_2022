import sys

f=open(sys.argv[1])
files=f.readlines()
f.close()


def get_nodes(file):
	nodes=[]
	for line in file:
		if line.startswith("Tree"):
			nodes.append(line.split(',')[0].split('|')[2])
	return(nodes)


matches=0
non_matches=0


for file_name in files:
	f=open(file_name.strip("\n"))
	file=f.readlines()
	f.close()
	nodes=get_nodes(file)
	if nodes[0]==nodes[1]:
		matches=matches+1
	else:
		non_matches=non_matches+1

print("The number of matching root nodes is:",matches)
print("The number of non matching root nodes is:",non_matches)

