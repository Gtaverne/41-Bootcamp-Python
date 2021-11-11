#logger.py

import time
import sys
import os

def log(func):
	def magic(*args):
		start = time.time()*1000
		res = func(*args)
		stop = time.time()*1000
		original_stdout = sys.stdout
		with open('machine.log', 'a') as f:
			sys.stdout = f
			T = stop - start
			print(f"( {os.getlogin()} ) Running: {func.__name__:<25} [ exec-time = ", end="")
			if T > 1000:
				print(round(T / 1000, 3), "s]")
			else:
				print(round(T, 3), "ms]")
			sys.stdout = original_stdout
			f.close()
		return res
	return magic

