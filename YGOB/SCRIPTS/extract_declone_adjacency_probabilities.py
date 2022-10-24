import sys

def get_table(file):
	table=[]
	for line in file:
		if not line.strip().startswith(">"):
			if not line.strip().rstrip("/n")=="":
				table.append(line.strip("\n"))
	return(table)
def get_orientation(file_name,script):
	num=file_name.split(".")[0]
	orientation1=script.strip("\n")[int(num)-1].split(".")[-2].split("_")[-2]
	orientation1=script.strip("\n")[int(num)-1].split(".")[-2].split("_")[-1]
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

def create_file(file,output_file,script):
	table=get_table(file)
	col_genes=get_col_genes(table)
	row_genes=get_row_genes(table)
	orientation1,orientation2=get_orientation(file,script)
	for i in range(len(row_genes)):
		for j in range(len(col_genes)):
			weight=get_weight(table,i,j)
			if not weight=="0":
				output_file.write(''.join([row_genes[i]," ",col_genes[j]," ",weight,"\n"]))


f=open(sys.argv[1])
file=f.readlines()
f.close()

outf=open(sys.argv[2],'w')
create_file(file,outf)
outf.close()

f=open(sys.argv[3])
script=f.readlines()
f.close()
