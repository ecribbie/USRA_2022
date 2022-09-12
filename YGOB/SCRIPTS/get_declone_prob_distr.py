import sys
import os
import math

def get_values(line,list):
	for num in line.split()[1:]:
		list.append(float(num))
		if math.isnan(float(num)):
			print(num," returns NaN when converted to float on line ",line," of file ", file, flush=True)
	return(list)


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
	file_path=os.path.join(file_dir,file)
	lines=get_lines(file_path)
	for line in lines:
		values=get_values(line,values)


import plotext as plt

plt.hist(values,25)
plt.title("Frequency Distribution of Deoclone Probabilities")
plt.show()

