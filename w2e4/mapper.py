#!/usr/bin/env python
import sys

doneFirst = 0

# input comes from STDIN (standard input)
for line in sys.stdin:
        
	# ignore the first line of data (the header line)
	if doneFirst == 0:
		doneFirst = 1
		continue

	# remove leading and trailing whitespace
        line = line.strip()
	# split the line by empty space
	cols = line.split("\t")
	
	# produce the key and value
	key = cols[1] + '\t' + cols[2]
	value = cols[0] + '\t' + cols[3] + '\t' + cols[4]
	
	# now output the key and value
       	print '%s,%s' % (cols[1], cols[2])
