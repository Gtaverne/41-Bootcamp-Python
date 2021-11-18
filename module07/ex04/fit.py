import numpy as np

from gradient import gradient

def fit_(x, y, theta, alpha, max_iter):
	"""
	Description:
	Fits the model to the training dataset contained in x and y.
	Args:
	x: has to be a numpy.array, a matrix of shape m * n:
	(number of training examples, number of features).
	y: has to be a numpy.array, a vector of shape m * 1:
	(number of training examples, 1).
	theta: has to be a numpy.array, a vector of shape (n + 1) * 1:
	(number of features + 1, 1).
	alpha: has to be a float, the learning rate
	max_iter: has to be an int, the number of iterations done during the gradient descent
	Return:
	new_theta: numpy.array, a vector of shape (number of features + 1, 1).
	None if there is a matching shape problem.
	None if x, y, theta, alpha or max_iter is not of expected type.
	Raises:
	This function should not raise any Exception.
	"""
	if theta.ndim == 1:
		theta = theta.reshape(theta.size, 1)

	for i in range(max_iter):
		theta = theta - alpha * gradient(x,y,theta)
	return theta