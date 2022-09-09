import sys
import os






count=0
file_dir=sys.argv[1]
for file in os.listdir(file_dir):
	print(file)
