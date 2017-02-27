#!/usr/bin/env python
import sys


last_group = None
# input comes from STDIN
for line in sys.stdin:
        # remove leading and trailing whitespace
        val = line.strip()

	(month,temp) = val.split(",")
	group = month
	if last_group != group:
		print val
		last_group = group
