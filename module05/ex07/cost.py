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



def cost_elem_(y, y_hat):
	"""
	Description:
	Calculates all the elements (y_pred - y)ˆ2 of the cost function.
	Args:
	y: has to be an numpy.ndarray, a vector.
	y_hat: has to be an numpy.ndarray, a vector.
	Returns:
	J_elem: numpy.ndarray, a vector of dimension (number of the training examples,1).
	None if there is a dimension matching problem between X, Y or theta.
	None if any argument is not of the expected type.
	Raises:
	This function should not raise any Exception.
	"""
	try :
		y[0] - y_hat[0]
	except:
		print("Invalid input")
		return
	if y.shape != y_hat.shape:
		print(f"Wrong sizes: y = {y.shape} vs yhat = {y_hat.shape}")
		return
	
	res = np.zeros(len(y))
	res = [ (a - b)**2 for a,b in zip(y, y_hat) ]
	return (res)






def cost_(y, y_hat):
	"""
	Description:
	Calculates the value of cost function.
	Args:
	y: has to be an numpy.ndarray, a vector.
	y_hat: has to be an numpy.ndarray, a vector.
	Returns:
	J_value : has to be a float.
	None if there is a dimension matching problem between X, Y or theta.
	None if any argument is not of the expected type.
	Raises:
	This function should not raise any Exception.
	"""
	return (np.sum(cost_elem_(y,y_hat)) / ( 2 * y.size))