import sys


def read_file(file_path):
	f=open(file_path)
	file=f.readlines()
	f.close()
	return(file)


def get_species(spp_tree):
	species=[]
	file=read_file(spp_tree)
	for line in file:
		line=line.strip("\n")
		spec1,spec2=line.split("\t")
		if spec1 not in species:
			species.append(spec1)
		if spec2 not in species:
			species.append(spec2)
	return(species)

def get_sub_adj_list(adjacencies_path,species):
	adj=read_file(adjacencies_path)
	adj_keep=[adj[0]]
	for line in adj[1:]:
		spec=line.split("\t")[0]
		if spec in species:
			adj_keep.append(line)
	return(adj_keep)

def write_new_adj_file(path,adj):
	out_f=open(path,'w')
	for line in adj:
		out_f.write(line)
	out_f.close()

def run_all(tree,adjacencies,output_file):
	species=get_species(tree)
	kept_adj=get_sub_adj_list(adjacencies,species)
	write_new_adj_file(output_file,kept_adj)


tree=sys.argv[1]
adjacencies=sys.argv[2]
output_file=sys.argv[3]

run_all(tree,adjacencies,output_file)
