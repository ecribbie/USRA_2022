import sys
import os
adjacencies_f=sys.argv[1]
mapping_dir=sys.argv[2]
output_dir=sys.argv[3]
script=sys.argv[4]
family_dir=sys.argv[5]
def get_family_dict(mapping_dir):
	dict={}
	for file in os.listdir(mapping_dir):
		f=open(os.path.join(mapping_dir,file))
		mapping=f.readlines()
		f.close()
		num=file.split("_")[1]
		dict[num]={}
		dict[num]['genes']=[]
		for line in mapping:
			gene=line.split()[0]
			dict[num]['genes'].append(gene)
	return(dict)


def get_family(gene,dict):
	for key in dict.keys():
		if gene in dict[key]['genes']:
			break
	return(key)




def get_adj_dict(adjacencies_file,fam_dict):
	f=open(adjacencies_file)
	adj=f.readlines()
	f.close()
	adj_dict={}
	for line in adj:
		gene1=line.split()[0]
		gene2=line.split()[1]
		fam1=get_family(gene1,fam_dict)
		fam2=get_family(gene2,fam_dict)
		if int(fam1)==int(fam2):
			if '_'.join([fam1,fam2]) not in adj_dict:
				adj_dict['_'.join([fam1,fam2])]=[]
			adj_dict['_'.join([fam1,fam2])].append(' '.join([gene1,gene2]))
		elif int(fam1)<int(fam2):
			if '_'.join([fam1,fam2]) not in adj_dict:
				adj_dict['_'.join([fam1,fam2])]=[]
			adj_dict['_'.join([fam1,fam2])].append(' '.join([gene1,gene2]))
		elif int(fam1)>int(fam2):
			if '_'.join([fam2,fam1]) not in adj_dict:
                                adj_dict['_'.join([fam2,fam1])]=[]
			adj_dict['_'.join([fam2,fam1])].append(' '.join([gene1,gene2]))
	return(adj_dict)


def write_adjacency_files(adj_dict,out_dir):
	for pair in adj_dict:
		f=open(os.path.join(out_dir,''.join([pair,".txt"])),'w')
		for adj in adj_dict[pair]:
			f.write(adj)
			f.write("\n")
		f.close()


def create_declone_script(adj_dict,script,fam_dir,out_dir):
	f=open(script,'w')
	for pair in adj_dict:
		fam1=pair.split("_")[0]
		fam2=pair.split("_")[1]
		f.write(' '.join([os.path.join(fam_dir,''.join([fam1,"_reconciliated.nhx"])),os.path.join(fam_dir,''.join([fam2,"_reconciliated.nhx"])),os.path.join(out_dir,''.join([pair,".txt"]))]))
		f.write("\n")
	f.close()


fam_dict=get_family_dict(mapping_dir)

adj_dict=get_adj_dict(adjacencies_f,fam_dict)

write_adjacency_files(adj_dict,output_dir)

create_declone_script(adj_dict,script,family_dir,output_dir)
