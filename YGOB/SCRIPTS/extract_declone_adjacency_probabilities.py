import sys

def get_family_nums(file_name,script):
	line_num=file_name.split(".")[0]
	fam_num1=script[int(line_num)-1].split("/")[-1].split("_")[0]
	fam_num2=script[int(line_num)-1].split("/")[-1].split("_")[1]
	return(fam_num1,fam_num2)

def get_gene_specie_map(file,mapping={}):
	portions=file[0].split("S=")
	for i in range(1,len(portions)):
		piece=portions[i]
		specie_id=piece.split(":")[0]
		gene_id=piece.split("ND=")[1].split("]")[0]
		mapping[gene_id]=specie_id
	return(mapping)

def get_table(file):
	table=[]
	for line in file:
		if not line.strip().startswith(">"):
			if not line.strip().rstrip("/n")=="":
				table.append(line.strip("\n"))
	return(table)

def get_orientation(file_name,script):
	num=file_name.split(".")[0]
	orientation1=script[int(num)-1].split(".")[-2].split("_")[-2]
	orientation2=script[int(num)-1].split(".")[-2].split("_")[-1]
	return(orientation1,orientation2)

def get_col_genes(table):
	line=table[0]
	genes=line.split()
	return(genes)

def get_row_genes(table):
	genes=[]
	for i in range(1,len(table)):
		line=table[i]
		genes.append(line.split()[0])
	return(genes)

def get_weight(table,row,col):
	weight=table[row+1].split()[col+1]
	return(weight)

def get_mapping(file_path,script,map_path_prefix,map_path_suffix):
	fam1,fam2=get_family_nums(sys.argv[1],script)
	path1=''.join([mapping_path_prefix,fam1,mapping_path_suffix])
	path2=''.join([mapping_path_prefix,fam2,mapping_path_suffix])
	f=open(path1)
	map_file1=f.readlines()
	f.close()
	f=open(path2)
	map_file2=f.readlines()
	f.close()
	map1=get_gene_specie_map(map_file1)
	mapping=get_gene_specie_map(map_file2)
	return(mapping)

def create_file(file_path,file,output_file,script,mapping_path_prefix,mapping_path_suffix):
	mapping=get_mapping(file_path,script,mapping_path_prefix,mapping_path_suffix)
	table=get_table(file)
	col_genes=get_col_genes(table)
	row_genes=get_row_genes(table)
	orientation1,orientation2=get_orientation(file_path,script)
	for i in range(len(row_genes)):
		for j in range(len(col_genes)):
			weight=get_weight(table,i,j)
			if not weight=="0" and not int(col_genes[j])<0 and not int(row_genes[i])<0:
				row_specie=mapping[row_genes[i]]
				col_specie=mapping[col_genes[j]]
				output_file.write(''.join([row_specie," ",row_genes[i]," ",orientation1," ",col_specie," ",col_genes[j]," ",orientation2," ",weight,"\n"]))


f=open(sys.argv[1])
file=f.readlines()
f.close()

f=open(sys.argv[3])
script=f.readlines()
f.close()

mapping_path_prefix=sys.argv[4]
mapping_path_suffix=sys.argv[5]

outf=open(sys.argv[2],'w')
create_file(sys.argv[1],file,outf,script,mapping_path_prefix,mapping_path_suffix)
outf.close()

