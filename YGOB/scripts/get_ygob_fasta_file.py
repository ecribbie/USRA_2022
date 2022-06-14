import urllib.request as ur
import sys


def pull_file(url,output_name):
	f=ur.urlopen(url)
	file=f.readlines()
	f.close()
	
	g=open(output_name,"w")
	
	for line in file:
		g.write(line.decode("utf-8"))
	
	g.close
	
	return()



pull_file(sys.argv[1],sys.argv[2])

