import numpy as np



def predict_(x, theta):
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
	if x.ndim == 1:
		x = x.reshape(x.size, 1)
	res = np.insert(x, 0, 1, axis=1)
	return res.dot(theta)


def simple_gradient(x, y, theta):
	"""Computes a gradient vector from three non-empty numpy.array, without any for-loop.
	The three arrays must have compatible shapes.
	Args:
	x: has to be an numpy.array, a vector of shape m * 1.
	y: has to be an numpy.array, a vector of shape m * 1.
	theta: has to be an numpy.array, a 2 * 1 vector.
	Return:
	The gradient as a numpy.array, a vector of shape 2 * 1.
	None if x, y, or theta are empty numpy.array.
	None if x, y and theta do not have compatible shapes.
	None if x, y or theta is not of the expected type.
	Raises:
	This function should not raise any Exception.
	"""
	if type(x) != type(np.array([])) or type(y) != type(np.array([])):
		print("incorrect inputs, x and y are not even numpy arrays")
		return
	if x.ndim == 1:
		x = x.reshape(x.size, 1)
	if y.ndim == 1:
		y = y.reshape(y.size, 1)
	if x.shape != y.shape :
		print("incorrect inputs, x and y have different dimensions")
		return
	if theta.shape != (2, 1):
		try:
			theta = theta.reshape(2,1)
		except:
			print("Theta is not a 2 * 1 vector")
			return
	J = predict_(x, theta)
	vec = np.insert(x, 0, 1, axis=1)
	res = np.sum(((J - y)* (vec)), axis=0) / J.size
	return(res)

	
