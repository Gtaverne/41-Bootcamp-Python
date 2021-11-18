from os import replace
from os.path import exists
from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import normalize
import math
from copy import deepcopy



class KmeansClustering:
	def __init__(self, max_iter=200, ncentroid=4):
		self.ncentroid = ncentroid # number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids		

		
	def fit(self, X=0):
		"""
		Run the K-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Returns:
		None.
		Raises:
		This function should not raise any Exception.
		"""
		if (X != 0):
			self.data = X
		self.height = self.data.shape[0]
		self.nparam = self.data.shape[1] - 1
		z = np.zeros((self.data.shape[0], 1))
		self.data = np.append(self.data, z, axis = 1)
		self.norm_dat = deepcopy(self.data)
		print(self.data.shape)


		#Normalisation, BE CAREFUL, YOU WILL ALSO HAVE TO NORMALIZE WHEN PREDICTING
		self.max = np.ones(self.nparam)
		self.min = np.zeros(self.nparam)
		# for i in range(self.nparam):
		# 	self.norm_dat[:, i + 1] = self.norm_dat[:, i + 1] * (np.max(self.norm_dat[:, i + 1])- np.min(self.norm_dat[:, i + 1])) + np.min(self.norm_dat[:, i + 1])
		# 	self.max[i] = np.max(self.norm_dat[:, i + 1])
		# 	self.min[i] = np.min(self.norm_dat[:, i + 1])

		#random initialisation of centroids
		init = np.random.choice(self.height, self.ncentroid, replace = False)
		print(init)
		self.centroids = self.norm_dat[init, 1:-1]
		
		#Initialization taking into account subject's hints
		# self.centroids[0, :] = [210, 100, 0.4] #belter
		# self.centroids[1, :] = [155, 110, 1.4] #earth
		# self.centroids[2, :] = [165, 60, 0.8] #venus
		# self.centroids[3, :] = [185, 90, 0.8] #mars
		
		print(self.centroids.shape)

		for _ in range(self.max_iter):
			#finds the nearest centroid
			self.norm_dat[:,4] = [self.indexmin(self.norm_dat[j,1:3]) for j in range(self.height)]
			for k in range(self.ncentroid):
				v = self.norm_dat[self.norm_dat[:, 4] == k]
				L = v.shape[0]
				for i in range(self.nparam):
					self.centroids[k][i] = sum(v[:,i + 1]) / L
				

		print(self.norm_dat.shape)
		print(self.norm_dat[:,4])
		

	def dataset_import(self, address):
		self.filename = address
		if (not exists(self.filename)):
			print("File not found")
			self.data = None
		else:
			self.data = genfromtxt(self.filename, delimiter=',')
			self.axis = self.data[0,:]
			self.data = np.delete(self.data, 0, 0)


	def dataset_plot(self):
		fig = plt.figure()

		ax = fig.add_subplot(111,projection='3d')

		if self.data.shape[1] < 5:
			x = self.data[1:,1]
			y = self.data[1:,2]
			z = self.data[1:,3]
			ax.scatter(x,y,z)
		else:
			for i in range(self.ncentroid):
				x = self.data[:,1][self.norm_dat[:, 4] == i]
				y = self.data[:,2][self.norm_dat[:, 4] == i]
				z = self.data[:,3][self.norm_dat[:, 4] == i]
				ax.scatter(x,y,z)

		plt.show()

	def distance(self, A, B):
		#Start with L1 distance
		tmp = 0
		for i in range(len(A)):
			tmp += math.sqrt((A[i] - B[i]) ** 2)
		return tmp

	def indexmin(self, A):
		tmp = [self.distance(A, X) for X in self.centroids]
		return (tmp.index(min(tmp)))

	def predict(self, X):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Returns:
		the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		11This function should not raise any Exception."""
		if X.shape[1] != self.nparam + 1:
			print(f"Invalid input, input should have {self.nparam} parameters (index included)")
			return
		npredict = X.shape[0]
		res = np.zeros((npredict, 1))
		#normalisation
		for i in range(self.nparam):
			X[:,i] = X[:,i] * (self.max[i] - self.min[i]) + self.min[i]
		for pt in range(npredict):
			res[pt] = self.indexmin(X[pt, 1:-1])

		return res