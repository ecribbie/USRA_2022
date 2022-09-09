import sys
import os


def get_values(line):
	return(line.split()[1:])


def get_lines(file):
	f=open(file)
	file_lines=f.readlines()
	f.close()
	lines=[]
	for line in file_lines:
		if not line.startswith(">"):
			lines.append(line)
	return(lines)



file_dir=sys.argv[1]
values=[]
for file in os.listdir(file_dir):
        lines=get_lines(file)
	for line in lines:
		line_values=get_values(line)
		values=values+line_values

print(len(values))
