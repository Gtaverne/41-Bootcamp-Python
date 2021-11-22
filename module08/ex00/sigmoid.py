import numpy as np
from math import exp

def sigmoid_(x):
	"""
	Compute the sigmoid of a vector.
	Args:
	x: has to be an numpy.array, a vector
	Return:
	The sigmoid value as a numpy.array.
	None otherwise.
	Raises:
	This function should not raise any Exception.
	"""
	dim = x.shape
	if x.ndim == 0:
		return 1/(1+exp(-x))
	elif x.ndim != 1:
		x.reshape((-1,))
	res = 1 / ( 1 + np.exp (-x))
	return res.reshape(dim)

