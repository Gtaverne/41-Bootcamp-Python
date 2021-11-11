from time import sleep
from time import time
import random

def ft_progress(lst):
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



listy = range(100)
ret = 0
print (len(listy))

for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	t = random.randint(1 , 10) /10
	t *= t * t
	sleep(t)
print()
print(ret)

