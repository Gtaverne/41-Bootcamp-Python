#!usr/bin/python

import sys


s = sys.argv
tmp = ''

for x in s[1:-1:] :
	tmp += x +' '
tmp += s[-1]
tmp = (tmp[::-1]).upper()
print(tmp)