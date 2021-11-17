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
	if x.shape != y.shape :
		print("incorrect inputs, x and y have different dimensions")
		return
	if theta.shape != (2, 1):
		try:
			theta = theta.reshape(2,1)
		except:
			print("Theta is not a 2 * 1 vector")
			return
	X = np.insert(x, 0, 1, axis=1)
	print(X.dot(theta))
	res = (1 / y.size) * (np.transpose(X).dot(X.dot(theta) - y))
	print(res.shape)
	return (res) #double think if you need a reshape(2) here
	
