#!/usr/bin/python

import sys

f=open(sys.argv[1])

numIterationsToAverage=500
sum=0
i=0
for line in reversed(list(f)):
	val=line.split(" ")[-1]
	val=float(val)
	sum=sum+val
	i=i+1
	if i>=numIterationsToAverage:
		break

avg=sum/numIterationsToAverage
print sys.argv[1],",", avg
