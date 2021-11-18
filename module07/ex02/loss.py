import numpy as np

def loss_(y, y_hat):
	"""Computes the half mean squared error of two non-empty numpy.ndarray, without any for
	, →
	loop. The two arrays must have the same dimensions.
	Args:
	y: has to be an numpy.ndarray, a vector.
	y_hat: has to be an numpy.ndarray, a vector.
	Returns:
	The half mean squared error of the two vectors as a float.
	None if y or y_hat are empty numpy.ndarray.
	None if y and y_hat does not share the same dimensions.
	Raises:
	This function should not raise any Exceptions.
	"""
	#On fera des tests a la con plus tard
	L = y.size
	res = y - y_hat
	return(np.sum(res * res) / ( 2 * L))