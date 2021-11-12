import numpy as np

class ColorFilter():
	def invert(self, array):
		array[:,:,:-1] = 1 - array[:,:,:-1]
		return (array)

	def to_blue(self, array):
		array[:,:,0] = 0 * array[:,:,0]
		array[:,:,1] = 0 * array[:,:,1]
		return array
		
	def to_green(self, array):
		array[:,:,0] = 0 * array[:,:,0]
		array[:,:,2] = 0 * array[:,:,2]
		return array
	
	def to_red(self, array):
		array[:,:,1] = 0 * array[:,:,1]
		array[:,:,2] = 0 * array[:,:,2]
		return array

	def to_celluloid(self, array, levels = 4):
		sz = array.shape
		for col in range(3):
			for i in range(sz[0]):
				for j in range(sz[1]):
					array[i,j,col] = self.levelfinder(array[i,j,col], levels)
		return (array)

	def to_grayscale(self, array, type = 'weighted'):
		tmp = array[:,:,-1]
		sz = array.shape
		res = np.zeros((sz[0], sz[1]))
		if type == "m":
			for i in range(3):
				res += array[:,:,i]
			res = res * 1/3
		elif type == "weighted":
			res = 0.299 * array[:,:,0] + 0.587 * array[:,:,1] + 0.114 * array[:,:,2]
		array[:,:,0] = res
		array[:,:,1] = res
		array[:,:,2] = res
		return array

	def levelfinder(self, val, levels):
		rg = list(range(levels + 1))
		flevel = [x / levels for x in rg]
		i = 0
		try:
			while (val >= flevel[i] ):
				if val >= 1:
					return 1
				i += 1
		except:
			print(val, flevel)
		return flevel[i]


	def juxtapose(self, array, n, axis = 0):
		res = array
		if n == 0:
			return
		while(n - 1):
			res = np.concatenate((res, array), 1 - axis)
			n -=1
		return res
