import sys

def get_parent(tree,index):
	sub_tree=tree[int(index)+1:]
	parent=sub_tree.split(":")[0]
	return(parent)

def get_child1(tree,index):
	sub_tree=tree[:int(index)-1]
	child1=sub_tree.split(")")[-1].split("(")[-1].split(",")[-1].split(":")[0]
	return(child1)
def get_child2(tree,index):
	level=0
	sub_tree=tree[:int(index)-1]
	for i in range(len(sub_tree)-1,-1,-1):
		if sub_tree[i]==")":
			level=level-1
		if sub_tree[i]=="(":
			level=level+1
		if sub_tree[i]=="," and level==0:
			child2=sub_tree[:i-1].split(")")[-1].split("(")[-1].split(",")[-1].split(":")[0]
			return(child2)
def get_parent_dict(tree):
	parent_dict={}
	for i in range(len(tree)):
		if tree[i]==")":
			parent=get_parent(tree,i)
			parent_dict[parent]=i
	return(parent_dict)

def get_tree_list(tree):
	tree_list=[]
	parent_dict=get_parent_dict(tree)
	for parent in parent_dict:
		child1=get_child1(tree,parent_dict[parent])
		child2=get_child2(tree,parent_dict[parent])
		line1='\t'.join([parent,child1])
		line2='\t'.join([parent,child2])
		tree_list.append(line1)
		tree_list.append(line2)
	return(tree_list)

def write_tree(tree,output_file):
	tree_list=get_tree_list(tree)
	out=open(output_file,'w')
	for line in tree_list:
		out.write(line)
		out.write("\n")
	out.close()

f=open(sys.argv[1])
tree=f.readlines()[0]
f.close()
output_file=sys.argv[2]
write_tree(tree,output_file)
