#!/usr/bin/env python
from operator import itemgetter
import sys

current_len = None
current_count = 0
vlen = None

# input comes from STDIN
for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        vlen, count = line.split('\t', 1)

        # convert count (currently a string) to int
        try:
                count = int(count)
        except ValueError:
                # count was not a number, so silently
                # ignore/discard this line
                continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: vlen) before it is passed to the reducer
        if current_len == vlen:
                current_count += count
        else:
                if current_len:
                        # write result to STDOUT
			# TODO: Students to produce <lineLength, count> output
                current_count = count
                current_len = vlen

# do not forget to output the last word if needed!
if current_len == vlen:
	# TODO: Students to produce <lineLength, count> output
