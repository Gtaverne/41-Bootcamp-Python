import numpy as np
from math import sqrt

def mean(a, nostfu = 0):
	l = len(a)
	if l == 0:
		return
	sm = sum(a)
	return sm / l

def var(a, nostfu = 0):
	l = len(a)
	if l == 0:
		return
	res = 0
	for x in a:
		res += (x - mean(a,nostfu= 0)) * (x - mean(a, nostfu=0)) / l
	#res = sum([(x - self.mean(a)) * (x - self.mean(a)) / l for x in a])

	return res

def std(a):
	l = len(a)
	if l == 0:
		return
	res = sqrt(var(a, nostfu = 0))
	return (res)


def zscore(x):
	"""Computes the normalized version of a non-empty numpy.array using the z-score standardization.
	Args:
	x: has to be an numpy.array, a vector.
	Return:
	x’ as a numpy.array.
	None if x is a non-empty numpy.array or not a numpy.array.
	None if x is not of the expected type.
	Raises:
	This function shouldn’t raise any Exception.
	"""
	mu = mean(x)
	sigma = std(x)
	return ((x - mu) / sigma)