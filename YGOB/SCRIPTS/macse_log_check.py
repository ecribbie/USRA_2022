import sys
import re


f=open(sys.argv[1])
file=f.readlines()
f.close


bad_files=[]


for line_num in range(len(file)):
	g=open("".join(["log/",file[line_num].removesuffix("\n")]))
	log=g.readlines()
	g.close()
	if re.search("FINISHED SUCCESSFULLY",log[-1]):
		None
	else:
		bad_files.append(file[line_num].removesuffix("\n"))

print("The files that did not finish successfully are",bad_files)

