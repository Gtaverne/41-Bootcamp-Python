from time import sleep
from time import time
import sys

def progress(lst):
	for i in lst:
		if i == 0:
			start = time()
		i = i+1
		lmax = len(lst)
		t = time() - start
		av = 100 * i / lmax

		if av != 0:
			ETA = (str(round(t * 100 / av - t, 2)))
		else:
			ETA = "inf"

		beg = "ETA: " + ETA +"s "
		sec = "["  + str(round(av,1)) + "%]"
		bar = "["
		lenbar = int(av / 4)
		for k in range(lenbar):
			bar += "="
		bar += ">"

		print(f"{beg :<12}{sec :<8}{bar :<27}] {i}/{lmax}  | elapsed time {round(t, 2)}", end = "\r")
		yield i


def loopfunc(func, args, cycles = 100, grain = 2, dump=True):
	ret = 0
	for elem in progress(range(cycles)):
		ret += elem % grain
		if dump:
			original_stdout = sys.stdout
			with open('dump.log', 'a') as f:
				sys.stdout = f
				func(args)
				sys.stdout = original_stdout
				f.close()
		else:
			func(args)
	print()
	print(ret)
