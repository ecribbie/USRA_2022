import sys

f=open(sys.argv[1])
files=f.readlines()
f.close()

g=open(sys.argv[2])
original=g.readlines()
g.close


numbers=[]
all=[]

for file in files:
	num_str = ""
	for c in file:
    		if c.isdigit():
        		num_str=num_str+c
	numbers.append(int(num_str))

for file in original:
	num_str=""
	for c in file:
		if c.isdigit():
			num_str=num_str+c
	all.append(int(num_str))


missing=[]


for i in range(len(all)):
	if all[i] not in numbers:
		missing.append(i+1)

print(missing)
