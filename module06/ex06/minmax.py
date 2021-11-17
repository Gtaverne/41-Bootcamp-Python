import numpy as np


def minmax(x):
	"""Computes the normalized version of a non-empty numpy.array using the min-max standardization.
	Args:
	x: has to be an numpy.array, a vector.
	Return:
	x’ as a numpy.array.
	None if x is a non-empty numpy.array or not a numpy.array.
	None if x is not of the expected type.
	Raises:
	This function shouldn’t raise any Exception.
	"""
	ma = np.max(x)
	mi = np.min(x)

	return((x - mi) / (ma - mi))