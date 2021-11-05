#!usr/bin/python

import sys

if (len(sys.argv) != 2 or sys.argv[1].isdigit() == False ):
	print("Error")
else:
	i =  int(sys.argv[1])


	if (i%2) == 0:
		print("I'm Even")
	elif (i%2) == 1:
		print("I'm Odd")
	else:
		print("Error")
