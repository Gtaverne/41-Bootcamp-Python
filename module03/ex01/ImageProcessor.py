import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt


class ImageProcessor():
	def load(self, path):
		self.path = path
		img = imread(path)
		shp = img.shape
		print(f"Loading image of dimensions {shp[0]} x {shp[1]} ")
		return img

	def display(self, array):
		imgplot = plt.imshow(array)
		plt.show()
		return imgplot


