from time import sleep

#We'll see later

def ft_progress(lst):
	print("ETA: ", end = "")
	for i in lst:
		yield i



listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.001)
print()
print(ret)

