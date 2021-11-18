import numpy as np



def gradient(x, y, theta):
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
	if x.shape[0] != y.shape[0] :
		print("incorrect inputs, x and y don't have the same length")
		return
	if theta.ndim == 1:
		try:
			theta = theta.reshape(-1,1)
		except:
			print("Theta is not a n * 1 vector")
			return
	X = np.insert(x, 0, 1, axis=1)
	res = (1 / y.size) * (np.transpose(X).dot(X.dot(theta) - y))
	return (res.reshape((-1,))) #double think if you need a reshape here
	
