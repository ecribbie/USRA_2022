import sys
import re

f=open(sys.argv[1])
files=f.readlines()
f.close()

path='/'.join(sys.argv[1].split('/')[:-1])


for file_n in files:
	file=file_n.removesuffix("\n")
	g=open('/'.join([path,file]))
	msa=g.readlines()
	g.close()
	
	w=open('/'.join([path,file]),'w')

		
	for line in msa:
		if re.search(">",line):
			w.write(line.split(' ')[0])
			w.write("\n")
		else:
			w.write(line)

	w.close()



