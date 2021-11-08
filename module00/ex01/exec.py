#!usr/bin/python

import sys


s = sys.argv
tmp = ''

for x in s[1:-1:] :
	tmp += x +' '
tmp += s[-1]
tmp = (tmp[::-1])
tmp = [x.upper() if x.islower() else x.lower() for x in tmp ]
print(''.join(tmp))