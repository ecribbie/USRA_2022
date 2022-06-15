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
        

print(d1.keys(),flush=True)

for record in  SeqIO.parse(AA,"fasta"):
    gene=record.id.split(" ")[0]
    pillar=d1[gene]
    if d2[pillar]['read']==0:
        globals()["".join(["fam",pillar])]=open("".join([filetype,"_",str(pillar),".fsa"]),"w")
    globals()["".join(["fam",pillar])].write(record)
    globals()["".join(["fam",pillar])].write("\n")
    d2[pillar]["read"]+=1
    if d2[pillar]["read"]==d2[pillar]["total"]:
        globals()["".join(["fam",pillar])].close()
    
