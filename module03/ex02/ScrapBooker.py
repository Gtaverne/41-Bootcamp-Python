import numpy as np


class ScrapBooker():
	def crop(self, array, dimensions, position = (0 , 0)):
		sz = array.shape
		res = array
		# if dimensions[0] + position[0] > sz[0] or dimensions[1] + position[1] > sz[1]:		
		if dimensions[0] > sz[0] or dimensions[1]  > sz[1]:
			print("Dimensions + position too big for size")
			return
		res = res[position[0]:position[0] + dimensions[0],\
			position[1]:position[1] + dimensions[1]]
		return res	
		

	def thin(self, array, n, axis = 0):
		if n < 1:
			return
		axis = 1 - axis
		res = array
		# res = np.delete(res, slice(None, None, n), axis)
		i = n - 1
		while( i < res.shape[axis]):
			res = np.delete(res, i, axis)
			i += n - 1
		return res

	def juxtapose(self, array, n, axis = 0):
		res = array
		if n == 0:
			return
		while(n - 1):
			res = np.concatenate((res, array), 1 - axis)
			n -=1
		return res

	def mosaic(self, array, dimension):
		res = array
		res = self.juxtapose(res, dimension[0], 0)
		res = self.juxtapose(res, dimension[1], 1)
		return res