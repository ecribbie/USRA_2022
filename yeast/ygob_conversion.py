# get txt file of species genomes
file=input('file name')
#read in that txt file to raw
f=open('file','r')
raw=f.readlines()
f.close()

#output file to check
print(raw)


