import sys

xml_file=sys.argv[1]
outfile=sys.argv[2]
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
							dict[name]['kids'].append(str(nextid))
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
				dict[name]['species']=[]
			dict[name]['species'].append(name)
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
							dict[name]['kids'].append(str(nextid))
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



def get_tree(dict):
	list=[]
	pardict={}
	keys=dict.keys()
	for key1 in keys:
		for key2 in keys:
			if dict[key2]['event'][0] not in ['loss','extant']:
				if key1 in dict[key2]['kids']:
					pardict[key1]=key2
		if key1 not in pardict:
			list.append(key1)
	for key in pardict:
		if pardict[key]=='0':
			list.append(key)

	tree=''.join(["(","*",list[1],"*",",","*",list[2],"*",")",";"])
	todo=[list[1],list[2]]
	while len(todo) != 0:
		for key in todo:
			if dict[key]['event'][0] not in ['loss','extant']:
				tree=tree.replace(''.join(["*",key,"*"]),''.join(["(","*",dict[key]['kids'][0],"*",",","*",dict[key]['kids'][1],"*",")","*",key,"*"]))
				todo.remove(key)
				if dict[dict[key]['kids'][0]]['event'][0] not in ['loss','extant']:
					todo.append(dict[key]['kids'][0])
				if dict[dict[key]['kids'][1]]['event'][0] not in ['loss','extant']:
					todo.append(dict[key]['kids'][1])
	return(tree)
newtree=get_tree(dict)


def add_info(tree,dict):
	for key in dict:
		if dict[key]['event'][0] == 'loss':
			tree=tree.replace(''.join(["*",key,"*"]),''.join(["loss|",dict[key]['species'][0],":1.0","[&&NHX:D=?:Ev=Glos:S=",dict[key]['species'][0],":ND=",key,"]"]))
		elif dict[key]['event'][0] == 'extant':
			tree=tree.replace(''.join(["*",key,"*"]),''.join([key,"|",dict[key]['species'][0],":1.0","[&&NHX:D=?:Ev=Extant:S=",dict[key]['species'][0],":ND=",key,"]"]))
		elif dict[key]['event'][0] == 'speciation':
			tree=tree.replace(''.join(["*",key,"*"]),''.join([":1.0[&&NHX:D=?:Ev=Spec:S=",dict[key]['species'][0],":ND=",key,"]"]))
		elif dict[key]['event'][0] == 'duplication':
			 tree=tree.replace(''.join(["*",key,"*"]),''.join([":1.0[&&NHX:D=y:Ev=GDup:S=",dict[key]['species'][0],":ND=",key,"]"]))

	return(tree)
fulltree=add_info(newtree,dict)

g=open(outfile,'w')
g.write(fulltree)
g.close()

