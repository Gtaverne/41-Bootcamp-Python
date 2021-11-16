import numpy as np
import math

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
	dif = y - y_hat
	return(np.sum(dif * dif) / ( 2 * L))

def mse_(y, y_hat):
	"""
	Description:
	Calculate the MSE between the predicted output and the real output.
	Args:
	y: has to be a numpy.ndarray, a vector of dimension m * 1.
	y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
	Returns:
	mse: has to be a float.
	None if there is a matching dimension problem.
	Raises:
	This function should not raise any Exceptions.
	"""
	#On fera des tests a la con plus tard
	L = y.size
	dif = y - y_hat
	return(np.sum(dif * dif) / (L))

def rmse_(y, y_hat):
	"""
	Description:
	Calculate the RMSE between the predicted output and the real output.
	Args:
	y: has to be a numpy.ndarray, a vector of dimension m * 1.
	y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
	Returns:
	rmse: has to be a float.
	None if there is a matching dimension problem.
	Raises:
	This function should not raise any Exceptions.
	"""
	#On fera des tests a la con plus tard
	L = y.size
	dif = y - y_hat
	return(math.sqrt(np.sum(dif * dif)) / (L))

def mae_elem(y, y_hat):
	pass



def mae_(y, y_hat):
	"""
	Description:
	Calculate the MAE between the predicted output and the real output.
	Args:
	y: has to be a numpy.ndarray, a vector of dimension m * 1.
	y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
	Returns:
	mae: has to be a float.
	None if there is a matching dimension problem.
	Raises:
	This function should not raise any Exceptions.
	"""
	#On fera des tests a la con plus tard
	L = y.size
	
	return(np.sum(mae_elem(y,y_hat)) / (L))


def r2score_(y, y_hat):
	"""
	Description:
	Calculate the R2score between the predicted output and the output.
	Args:
	y: has to be a numpy.ndarray, a vector of dimension m * 1.
	28y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
	Returns:
	r2score: has to be a float.
	None if there is a matching dimension problem.
	Raises:
	This function should not raise any Exceptions.
	"""
	#On fera des tests a la con plus tard
	L = y.size
	dif = y - y_hat
	ymean = np.sum(y) / L
	return(1 - np.sum(dif * dif) / (np.sum((y - ymean) ** 2)))
