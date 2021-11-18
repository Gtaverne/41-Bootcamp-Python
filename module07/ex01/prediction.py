import numpy as np


def simple_predict(x, theta):
	"""Computes the prediction vector y_hat from two non-empty numpy.ndarray.
	Args:
	x: has to be an numpy.ndarray, a vector of dimensions m * 1.
	theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
	Returns:
	y_hat as a numpy.ndarray, a vector of dimension m * 1.
	None if x or theta are empty numpy.ndarray.
	None if x or theta dimensions are not appropriate.
	Raises:
	This function should not raise any Exception.
	"""
	if theta.ndim == 1:
		theta = theta.reshape(theta.size, 1)
	if x.ndim == 1:
		x = x.reshape(x.size, 1)
	res = np.insert(x, 0, 1, axis=1)
	# we might have to reshape it
	ex = res.dot(theta)
	if ex.shape[1] == 1:
		return ex.reshape((-1,))
	else:
		return ex