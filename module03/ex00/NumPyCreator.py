import numpy as np

class NumPyCreator():
	def from_list(self, lst):
		return np.array(lst)

	def from_tuple(self, tpl):
		return np.array(tpl)


	def from_iterable(self, itr):
		#return np.fromiter(itr) #requires type, I don't know how to get it
		return np.array(list(itr))

	def from_shape(self, shape, value = 0):
		return (np.full(shape, value))


	def random(self, shape):
		return (np.random.uniform(0, 1, shape))

	def identity(self, n):
		return (np.identity(n))