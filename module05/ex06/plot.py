import matplotlib.pyplot as plt
import numpy as np

def predict(x, theta):
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

def plot(x, y, theta):
	"""Plot the data and prediction line from three non-empty numpy.ndarray.
	Args:
	x: has to be an numpy.ndarray, a vector of dimension m * 1.
	y: has to be an numpy.ndarray, a vector of dimension m * 1.
	theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
	Returns:
	Nothing.
	Raises:
	This function should not raise any Exceptions.
	"""
	plt.plot(x, y, 'o')

	abs = np.linspace(np.min(x), np.max(x), 100)
	y = predict(abs, theta)
	plt.plot(abs, y)
	plt.show()