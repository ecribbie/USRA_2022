import sys
missing_f=sys.argv[1]
f=open(missing_f)
missing=f.readlines()
f.close()

out_f=sys.argv[2]

missing_list=[]
for line in missing:
	missing_list.append(line.split(".")[0].split("_")[-1])


g=open(out_f,'w')

for num in missing_list:
	g.write(num)
	g.write("\n")

g.close()
