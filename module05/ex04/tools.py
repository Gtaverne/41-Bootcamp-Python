import numpy as np

def add_intercept(x):
	"""Adds a column of 1's to the non-empty numpy.ndarray x.
	Args:
	x: has to be an numpy.ndarray, a vector of dimension m * 1.
	Returns:
	X as a numpy.ndarray, a vector of dimension m * 2.
	None if x is not a numpy.ndarray.
	None if x is a empty numpy.ndarray.
	Raises:
	This function should not raise any Exception.
	"""
	ons = np.ones((x.shape[0]))
	if x.ndim > 1:
		res = np.insert(x, 0, ons, axis=1)
		return res
	else:
		res = np.stack((ons, x), axis=1)
		return res