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
		tmp = array[::-1]
		
		sz = array.shape
		for col in range(3):
			for i in range(sz[0]):
				for j in range(sz[1]):
					array[i,j,col] = self.levelfinder(array[i,j,col], levels)

		return (array)

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
