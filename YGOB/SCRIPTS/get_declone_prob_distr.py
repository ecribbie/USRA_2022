import sys
import os
import math

def get_values(line,list):
	for num in line.split()[1:]:
		if math.isnan(float(num)):
			break
		if num== '0':
			continue
		list.append(float(num))
	return(list)


def get_lines(file):
	f=open(file)
	file_lines=f.readlines()
	f.close()
	lines=[]
	for line in file_lines:
		if not line.startswith(">"):
			lines.append(line)
	return(lines[2:])



file_dir=sys.argv[1]
values=[]
for file in os.listdir(file_dir):
	file_path=os.path.join(file_dir,file)
	lines=get_lines(file_path)
	for line in lines:
		values=get_values(line,values)


import plotext as plt
import numpy as np
bins= np.arange(0,1.01,0.02)
data_bins=np.digitize(values,bins)
bin_counts=[]
for i in range(1,len(bins)):
	ind = [j for j, x in enumerate(data_bins) if x == i]
	bin_counts.append(len(ind))

cum_count=[]
for i in range(len(bin_counts)):
	cum_count.append(sum(bin_counts[i:]))
print(cum_count)

plt.plot(cum_count)
plt.title("Cumulative Frequency Distribution of Declone Probabilities")
plt.show()

