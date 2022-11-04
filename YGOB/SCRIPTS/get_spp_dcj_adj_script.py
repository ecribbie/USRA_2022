import sys
import os

def get_adj(file,threshold):
	adj=[]
	for line in file:
		if float(line.split()[-1])>=float(threshold):
			adj.append(line)
	return(adj)

def get_files(dir):
	files=[]
	for file_name in os.listdir(dir):
		f=os.path.join(dir,file_name)
		if os.path.isfile(f):
			files.append(f)
	return(files)

def read_file(file_path):
	f=open(file_path)
	file=f.readlines()
	f.close()
	return(file)

def get_script_list(dir,threshold):
	script=[]
	files=get_files(dir)
	for file_path in files:
		file=read_file(file_path)
		file_adj=get_adj(file,threshold)
		script=script+file_adj
	return(script)

def write_script(output,script):
	out=open(output,'w')
	out.write("#Species\tGene_1\tExt_1\tSpecies\tGene_2\tExt_2\tWeight\n")
	for line in script:
		out.write(line)
	out.close()


dir=sys.argv[1]
output_file=sys.argv[2]
threshold=sys.argv[3]

script_list=get_script_list(dir,threshold)
write_script(output_file,script_list)
