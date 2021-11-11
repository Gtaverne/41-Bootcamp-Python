from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce


import random

def moinsdix(val):
	return val - 10

def iseven(val):
	if val % 2 == 0 :
		return True
	return False

def ft_max( a, b):
	if a > b:
		return a
	return b

lst = random.sample(range(100), 10)

print(lst)

print()
mapl = ft_map(moinsdix, lst)
print(mapl)

print()
filterlist = ft_filter(iseven, lst)
print(filterlist)

print()
reducelist = ft_reduce(ft_max, lst)
print(reducelist)