import numpy as np
from numpy.random import default_rng

def data_spliter(x, y, proportion):
	"""Shuffles and splits the dataset (given by x and y) into a training and a test set,
	while respecting the given proportion of examples to be kept in the training set.
	Args:
	x: has to be an numpy.array, a matrix of shape m * n.
	y: has to be an numpy.array, a vector of shape m * 1.
	proportion: has to be a float, the proportion of the dataset that will be assigned to the
	training set.
	Return:
	(x_train, x_test, y_train, y_test) as a tuple of numpy.array
	None if x or y is an empty numpy.array.
	None if x and y do not share compatible shapes.
	None if x, y or proportion is not of expected type.
	Raises:
	This function should not raise any Exception.
	"""
	if x.shape[0] != y.shape[0]:
		print("x and y have different lengths")
		return
	if proportion < 0 or proportion > 1:
		print("Proportion should be between 0 and 1")
	rng = default_rng()
	shuffler = rng.choice(x.shape[0], x.shape[0], replace = False)
	xs = np.array([x[i] for i in shuffler])
	ys = np.array([y[i] for i in shuffler])
	l = int(proportion * x.shape[0])
	x_train = xs[:l]
	x_test = xs[l:]
	y_train = ys[:l]
	y_test = ys[l:]
	return (x_train, x_test, y_train, y_test)