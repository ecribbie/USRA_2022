import sys

xml_file=sys.argv[1]
#output_file=sys.argv[2]
dict={}

def read_xml_to_dict(xmlf,dict):
	f=open(xmlf)
	xml=f.readlines()
	f.close()
	nextid=0
	i=0
	line=xml[i]
	while "<recGeneTree>" not in line:
		i=i+1
		line=xml[i]
	xml=xml[i:]
	for j in range(len(xml)):
		line=xml[j]
		if "<speciation" in line:
			name=line.split('"')[1]
			if name not in dict:
				name=str(nextid)
				nextid+=1
				dict[name]={}
				dict[name]['event']=[]
				dict[name]['kids']=[]
				dict[name]['species']=[line.split('"')[1]]
			dict[name]['event'].append("speciation")
			leveldown=0
			for k in range(j,len(xml)):
				line=xml[k]
				if "<clade>" in line:
					leveldown=leveldown+1
				if "</clade>" in line:
					leveldown=leveldown-1
				if leveldown == 1:
					if "<speciation" in line:
						if line.split('"')[1] in dict:
							dict[name]['kids'].append(line.split('"')[1])
						else:
							dict[str(nextid)]={}
							dict[str(nextid)]['event']=[]
							dict[str(nextid)]['kids']=[]
							dict[str(nextid)]['species']=[line.split('"')[1]]
							change=line.split('"')
							change[1]=str(nextid)
							xml[k]='"'.join(change)
							line=xml[k]
							dict[name]['kids'].append(line.split('"')[1])
							nextid+=1
					elif "<loss" in line:
						dict[name]['kids'].append(line.split('"')[1])
					elif "<duplication" in line:
						if line.split('"')[1] in dict:
							dict[name]['kids'].append(line.split('"')[1])
						else:
							dict[str(nextid)]={}
							dict[str(nextid)]['event']=[]
							dict[str(nextid)]['kids']=[]
							dict[str(nextid)]['species']=[line.split('"')[1]]
							change=line.split('"')
							change[1]=str(nextid)
							xml[k]='"'.join(change)
							dict[name]['kids'].append(nextid)
							nextid+=1
					elif "<leaf" in line:
						kid=xml[k-2].split("<name>")[1].split("</name>")[0]
						dict[name]['kids'].append(kid)

				if leveldown<0:
					break
		if "<loss" in line:
			name=line.split('"')[1]
			if name not in dict:
				dict[name]={}
				dict[name]['event']=[]
			dict[name]['event'].append("loss")
		if "<leaf" in line:
			name=xml[j-2].split("<name>")[1].split("</name>")[0]
			if name not in dict:
				dict[name]={}
				dict[name]['species']=[]
				dict[name]['event']=[]
			dict[name]['species'].append(line.split('"')[1])
			dict[name]['event'].append("extant")
		if "<duplication" in line:
			name=line.split('"')[1]
			if name not in dict:
				name=str(nextid)
				nextid+=1
				dict[name]={}
				dict[name]['event']=[]
				dict[name]['kids']=[]
				dict[name]['species']=[line.split('"')[1]]
			dict[name]['event'].append("duplication")
			leveldown=0
			for k in range(j,len(xml)):
				line=xml[k]
				if "<clade>" in line:
					leveldown=leveldown+1
				if "</clade>" in line:
					leveldown=leveldown-1
				if leveldown == 1:
					if "<speciation" in line:
						if line.split('"')[1] in dict:
							dict[name]['kids'].append(line.split('"')[1])
						else:
							dict[str(nextid)]={}
							dict[str(nextid)]['event']=[]
							dict[str(nextid)]['kids']=[]
							dict[str(nextid)]['species']=[line.split('"')[1]]
							change=line.split('"')
							change[1]=str(nextid)
							xml[k]='"'.join(change)
							dict[name]['kids'].append(nextid)
							nextid+=1
					elif "<loss" in line:
						dict[name]['kids'].append(line.split('"')[1])
					elif "<duplication" in line:
						if line.split('"')[1] in dict:
							dict[name]['kids'].append(line.split('"')[1])
						else:
							dict[str(nextid)]={}
							dict[str(nextid)]['event']=[]
							dict[str(nextid)]['kids']=[]
							dict[str(nextid)]['species']=[line.split('"')[1]]
							change=line.split('"')
							change[1]=str(nextid)
							xml[k]='"'.join(change)
							dict[name]['kids'].append(nextid)
							nextid+=1
					elif "<leaf" in line:
						kid=xml[k-2].split("<name>")[1].split("</name>")[0]
						dict[name]['kids'].append(kid)

				if leveldown<0:
					break

"""

Get info as nodes with their names, events(speciation, duplication) and children node names. If (leaf,loss) instead have name , species and event (Extant,Glos)
To do this:
-Go through line by line and if line has an event(spec,dup,loss) get name from specieslocation=, If extant get name from name line 2 prior
-If name not already in dict create new dict with name
-add according event to dict, store as list so as to append in case of multiple events
-Continue by following clads so that when in one clad get name and repeat for second. If a speciation use location name if leaf use gene name



"""
read_xml_to_dict(xml_file,dict)
print(dict)
print(len(dict))


