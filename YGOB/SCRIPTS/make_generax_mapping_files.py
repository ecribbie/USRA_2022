import sys
import re



f=open(sys.argv[1])
mapping=f.readlines()
f.close()


g=open(sys.argv[2])
fam_files=g.readlines()
g.close()


out_path=sys.argv[3]

for file in fam_files:
	num_str = ""
	for c in file:
    		if c.isdigit():
        		num_str=num_str+c
	globals()[''.join(["fam_",num_str])]=[]
	h=open('/'.join(['/'.join(sys.argv[2].split("/")[:-1]),file.removesuffix("\n")]))
	fam_f=h.readlines()
	h.close()
	for line in fam_f:
		if re.search(">",line):
			globals()[''.join(["fam_",num_str])].append(line.split(" ")[0].removeprefix(">"))



for i in range(len(fam_files)):
	 globals()["".join(["file_",str(i)])]=open(''.join([out_path,"fam_",str(i),"_mapping.txt"]),'w')




for line in mapping:
	gene=line.split(" ")[0]
	specie=line.split(" ")[1].removesuffix("\n")
	for i in range(len(fam_files)):
		if gene in globals()[''.join(["fam_",str(i)])]:
			globals()["".join(["file_",str(i)])].write(' '.join([gene,specie]))
			globals()["".join(["file_",str(i)])].write("\n")
			break


for i in range(len(fam_files)):
	globals()["".join(["file_",str(i)])].close()
