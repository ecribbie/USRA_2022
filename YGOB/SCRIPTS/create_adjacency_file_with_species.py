import sys
import os.path


num=len(sys.argv)-3

f=open(sys.argv[1])
gene_file=f.readlines()
f.close()

genes=[]

for line in gene_file:
	genes.append(line.split(" ")[0].removeprefix(">"))


if not os.path.exists(sys.argv[2]):
	f=open(sys.argv[2],'w')
else:
	print("give as second argument path to non existent file to write adjacencies to")
	exit()



def write_adjacencies(file):
	global f
	g=open(file)
	data=g.readlines()
	g.close()
	while len(data[-1])<5:
		data=data[:-1]
	for i in range(len(data)-1):
		line=data[i]
		next=data[i+1]
		if line.split()[0] in genes:
			if next.split()[0] in genes:
				if line.split()[5]==next.split()[5]:
					if line.split()[1]=="0":
						first_dir="+"
					else:
						first_dir="-"
					if next.split()[1]=="0":
						second_dir="+"
					else:
						second_dir="-"
					f.write(' '.join(['_'.join([file.split("/")[-1].split("_")[0],line.split()[0]]),'_'.join([file.split("/")[-1].split("_")[0],next.split()[0]]),first_dir,second_dir,"1"]))
					if int(line.split()[3]) > int(next.split()[2]):
						f.write(" overlap")
					f.write("\n")
			else:
				for j in range(1,100):
					if data[i+j].split()[0] in genes:
						if line.split()[5]==data[i+j].split()[5]:
							if line.split()[1]=="0":
		                                                first_dir="+"
							else:
								first_dir="-"
							if data[i+j].split()[1]=="0":
								second_dir="+"
							else:
								second_dir="-"
							f.write(' '.join(['_'.join([file.split("/")[-1].split("_")[0],line.split()[0]]),'_'.join([file.split("/")[-1].split("_")[0],data[i+j]]).split()[0],first_dir,second_dir,"1"]))

							if int(line.split()[3]) > int(data[i+j].split()[2]):
	                                                	f.write(" overlap")
							f.write("\n")
						break
					if i+j+1==len(data):
						break






for i in range(3,num+3):
	write_adjacencies(sys.argv[i])


f.close()
