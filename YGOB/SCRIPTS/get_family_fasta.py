from Bio import SeqIO
import sys

file_type=sys.argv[3]

AA=sys.argv[1]

f=open(sys.argv[2])
pillars=f.readlines()
f.close()

d1={}
d2={}


for fam in range(0,len(pillars)):
    
    genes=pillars[fam].split(" ")
    
    for gene in genes:
        d1[gene]=fam
    d2[fam]={}
    d2[fam]["read"]=0
    d2[fam]["total"]=len(genes)
        

for record in  SeqIO.parse(AA,"fasta"):
    gene=record.id.split(" ")[0]
    if gene not in d1:
        continue
    pillar=d1[gene]
    if d2[pillar]['read']==0:
        globals()["".join(["fam",str(pillar)])]=open("".join([file_type,"_",str(pillar),".fsa"]),"w")
    SeqIO.write(record,globals()["".join(["fam",str(pillar)])],"fasta")
    globals()["".join(["fam",str(pillar)])].write("\n")
    d2[pillar]["read"]+=1
    if d2[pillar]["read"]==d2[pillar]["total"]:
        globals()["".join(["fam",str(pillar)])].close()
    
