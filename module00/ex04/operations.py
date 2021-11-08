#!usr/bin/python

import sys

if (len(sys.argv) != 3 or sys.argv[1].isdigit() == False ):
	if (len(sys.argv) > 3):
		print("InputError: too many arguments")
	print("Usage: python operations.py <number1> <number2>")
	print("Example:")
	print("	python operations.py 10 3")
elif (not (sys.argv[1].isdigit()) or not (sys.argv[2].isdigit())):
	print("InputError: only numbers")
	print("Usage: python operations.py <number1> <number2>")
	print("Example:")
	print("	python operations.py 10 3")
else:
	left =  int(sys.argv[1])
	right =  int(sys.argv[2])
	print("Sum:		", left + right)
	print("Difference:	", left - right)
	print("Product:	", left * right)
	if (right == 0):
		print("Quotient:	ERROR (div by zero)")
		print("Remainder:	ERROR (modulo by zero)")
	else:
		print("Quotient:	", left / right)
		print("Remainder:	", left %right)
