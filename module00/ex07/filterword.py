#!usr/bin/python
import string
import sys
import re

if (len(sys.argv) != 3 or not sys.argv[2].isdigit() or not isinstance(sys.argv[1], str)):
	print("error")
else:
	text = sys.argv[1]
	text = re.findall(r"[\w']+|[!\"#$%&'()*+,-./:;<=>?@\[\\\]^_\`{|}~]", text)
	print ([x for x in text if len(x) >= int(sys.argv[2])])

