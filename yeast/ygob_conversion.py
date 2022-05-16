#!/usr/bin/python

#will want to have a way to input desired file but for now using directly ygob_testfile.txt
f=open("ygob_testfile.txt",'r')
raw=f.readlines()
f.close()
print(raw[:10])
