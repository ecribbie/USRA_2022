import sys

f=open(sys.argv[1])
tree1=f.readlines()
f.close()

if len(tree1)>1:
	print("Error tree1 not one line")
	exit()
tree1=tree1[0]

f=open(sys.argv[2])
tree2=f.readlines()
f.close()

if len(tree2)>1:
	print("Error tree2 not one line")
	exit()
tree2=tree2[0]


def get_nodes(t1,t2):
	node1=t1.split("|")[-1].split(":")[0]
	node2=t2.split("|")[-1].split(":")[0]
	return(node1,node2)

def get_sub_tree(t1,t2):
	sub_tree=0
	node1,node2=get_nodes(t1,t2)
	if node1 in t2:
		sub_tree=1
	if node2 in t1:
		if sub_tree==1:
			print("Error, root node of each tree in other tree")
			exit()
		else:
			sub_tree=2
	return(sub_tree,node1,node2)

def get_parent(tree,node):
	level=0
	start=tree.rindex(node)
	for i in range(start,len(tree)):
		if tree[i]=="(":
			level=level-1
		if tree[i]==")":
			level=level+1
		if level==1:
			parent=tree[i:].split("|")[1].split(":")[0]
			break
	return(parent)



def get_parent_specie(tree,node):
	level=0
	start=tree.rindex(node)
	for i in range(start,len(tree)):
		if tree[i]=="(":
			level=level-1
		if tree[i]==")":
			level=level+1
		if level==1:
			parent_specie=tree[i:].split("S=")[1].split(":")[0]
			break
	return(parent_specie)


def get_sister(tree,node):
	level=0
	leave_marker=0
	prior_marker=1
	start=tree.rindex(node)
	for i in range(start,len(tree)):
		if tree[i]=="(":
			level=level-1
			leave_marker=1
		if tree[i]==")":
			level=level+1
			leave_marker=1
		if level==0 and leave_marker==1 and tree[i+1]!="(" and tree[i+1]!=")":
			sister=tree[i:].split("|")[1].split(":")[0]
			prior_marker=0
			break
		if tree[i]==",":
			leave_marker=1
		if level>0:
			break
	if prior_marker==1:
		leave_marker=0
		level=0
		for i in range(start,0,-1):
			if tree[i]=="(":
				level=level+1
				leave_marker=1
			if tree[i]==")":
				level=level-1
				leave_marker=1
			if level==0 and leave_marker==1 and tree[i-1]!="(" and tree[i-1]!=")":
				sister=tree[:i].split("|")[-1].split(":")[0]
				break
			if tree[i]==",":
				leave_marker=1
	return(sister)


def get_sister_specie(tree,node):
	level=0
	leave_marker=0
	prior_marker=1
	start=tree.rindex(node)
	for i in range(start,len(tree)):
		if tree[i]=="(":
			level=level-1
			leave_marker=1
		if tree[i]==")":
			level=level+1
			leave_marker=1
		if level==0 and leave_marker==1 and tree[i+1]!="(" and tree[i+1]!=")":
			sister_specie=tree[i:].split("S=")[1].split(":")[0]
			prior_marker=0
			break
		if tree[i]==",":
			leave_marker=1
		if level>0:
			break
	if prior_marker==1:
		leave_marker=0
		level=0
		for i in range(start,0,-1):
			if tree[i]=="(":
				level=level+1
				leave_marker=1
			if tree[i]==")":
				level=level-1
				leave_marker=1
			if level==0 and leave_marker==1 and tree[i-1]!="(" and tree[i-1]!=")":
				sister_specie=tree[:i].split("S=")[-1].split(":")[0]
				break
			if tree[i]==",":
				leave_marker=1

	return(sister_specie)


def make_tree(tree,parent,parent_specie,parent_ND,sister,sister_specie,sister_ND):
	new_tree=''.join(["(",tree[:-1],",loss|",sister,":1.0[&&NHX:D=?:Ev=GLos:S=",sister_specie,":ND=",sister_ND,"])None|",parent,":1.0[&&NHX:D=?:Ev=Spec:S=",parent_specie,":ND=",parent_ND,"];"])
	return(new_tree)




def get_new_tree(big_tree,small_tree,node,next_id):
	parent=get_parent(big_tree,node)
	parent_specie=get_parent_specie(big_tree,node)
	sister=get_sister(big_tree,node)
	sister_specie=get_sister_specie(big_tree,node)
	new_tree=make_tree(small_tree,parent,parent_specie,str(int(next_id)-1),sister,sister_specie,str(next_id))
	return(new_tree)



def run_iteration(tree1,tree2,next_id):
	sub_tree,node1,node2=get_sub_tree(tree1,tree2)
	if sub_tree==1:
		tree1=get_new_tree(tree2,tree1,node1,next_id)
		tree2=tree2
	elif sub_tree==2:
		tree1=tree1
		tree2=get_new_tree(tree1,tree2,node2,next_id)
	else:
		print("Error did not find subtree")
		exit()
	return(tree1,tree2)




count=0
node1,node2=get_nodes(tree1,tree2)
next_id=-1
while node1 != node2:
	tree1,tree2=run_iteration(tree1,tree2,next_id)
	node1,node2=get_nodes(tree1,tree2)
	next_id=next_id-2
	count=count+1
	if count>20:
		print("Error too many iterations required, double check tree inputs")
		exit()

#g=open('test1.nhx','w')
#g.write(new_tree)
#g.close()
#g=open('test2.nhx','w')
#g.write(other_tree)
#g.close()
print(tree1,"~",tree2)
