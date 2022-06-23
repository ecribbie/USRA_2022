import sys
import re


alignments_f=sys.argv[1]
mapping=sys.argv[2]
subst=sys.argv[3]
output=sys.argv[4]

f=open(alignments_f)
alignments=f.readlines()
f.close()

w=open(output,'w')


path='/'.join(alignments_f.split("/")[:-1])


w.write("[FAMILIES]\n")


for line in alignments:
	w.write("- " + line.removesuffix(".fsa"))
	w.write("alignment = " + ''.join([path,"/",line]))
	w.write("mapping = " + mapping + "\n")
	w.write("subst_model = " + subst + "\n")

w.close()
