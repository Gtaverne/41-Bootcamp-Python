import numpy as np

def simple_predict(x, theta):
	"""Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
	Args:
	x: has to be an numpy.ndarray, a vector of dimension m * 1.
	theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
	Returns:
	y_hat as a numpy.ndarray, a vector of dimension m * 1.
	None if x or theta are empty numpy.ndarray.
	None if x or theta dimensions are not appropriate.
	Raises:
	This function should not raise any Exception.
	"""
	pwr = theta.shape[0]
	res = np.ones((x.shape[0], pwr))
	for i in range(1, pwr):
		tmp = np.array([ a * b for a,b in zip(res[:, i - 1], x)])
		res[:, i] = tmp
	
	return res.dot(theta)

