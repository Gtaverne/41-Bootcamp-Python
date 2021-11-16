import matplotlib.pyplot as plt
import numpy as np

def predict_(x, theta):
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
	if x.ndim == 1:
		x = x.reshape(x.size, 1)
	res = np.insert(x, 0, 1, axis=1)
	#This may help us when going in higher dimensions
	# for i in range(2,theta.shape[0]):
	# 	print(i)
	# 	res = np.insert(res, res.shape[1], (x.reshape(x.size))**i, axis=1)
	return res.dot(theta)

def cost_(y, y_hat):
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

def plot_with_cost(x, y, theta):
	"""Plot the data and prediction line from three non-empty numpy.ndarray.
	Args:
	x: has to be an numpy.ndarray, a vector of dimension m * 1.
	y: has to be an numpy.ndarray, a vector of dimension m * 1.
	theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
	Returns:
	Nothing.
	Raises:
	This function should not raise any Exception.
	"""
	plt.plot(x, y, 'o')

	ypred = predict_(x, theta)
	for i in range(len(x)):
		plt.plot([x[i], x[i]], [ypred[i], y[i]], '--r')

	plt.plot(x, ypred)
	plt.title(f"Cost = {cost_(y,ypred)}")
	plt.show()


