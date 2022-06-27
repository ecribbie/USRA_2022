import sys
import os
import re

f=open(sys.argv[1])
files=f.readlines()
f.close()

for line in files:
	if line.split(".")[1].removesuffix("\n")=="log":
		if os.path.getsize("/".join(["log",line.removesuffix("\n")])) != 0:
			print(line.removesuffix("\n"))

		None
	else:
		g=open("/".join(["log",line.removesuffix("\n")]))
		l=g.readlines()
		g.close()

		if not re.search("00:00",l[-1]):
			print(line.removesuffix("\n"))
