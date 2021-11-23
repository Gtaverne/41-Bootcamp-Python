import numpy as np
from time import time
from math import exp
from math import log

class MyLogisticRegression():
	"""
	Description:
	My personnal logistic regression to classify things.
	"""
	def __init__(self, theta, alpha=0.001, max_iter=10000, eps = 1e-15):
		if alpha > 1 or alpha < 0:
			print("Invalid value of alpha")
			return
		if max_iter < 1:
			print("max_iter should be a positive integer")
			return
		self.alpha = alpha
		self.max_iter = int(max_iter)
		self.eps = eps
		if type(theta) != type(np.array([])):
			theta = np.array(theta)
		if theta.ndim == 1:
			self.theta = theta.reshape(theta.size, 1)
		else:
			self.theta = theta

	def fit_(self, x, y):
		if self.theta.ndim == 1:
			self.theta = self.theta.reshape(self.theta.size, 1)
		for i in range(self.max_iter):
			# if i % (self.max_iter/20) == 0:
			# 	print(f"i:{i} theta:\n", self.theta)
			self.theta = self.theta - self.alpha * self.log_gradient(x,y)
		return self.theta

	def sigmoid_(self, x):
		dim = x.shape
		if x.ndim == 0:
			return 1/(1+exp(-x))
		elif x.ndim != 1:
			x.reshape((-1,))
		res = 1 / ( 1 + np.exp (-x))
		return res.reshape(dim)


	def log_gradient(self, x, y):
		if y.ndim == 1:
			y.reshape((-1, 1))
		if x.ndim == 1:
			x.reshape((-1, 1))
		if x.shape[0] != y.shape[0]:
			print("arguments have different lengths")
			return
		if self.theta.ndim == 1:
			try:
				self.theta = self.theta.reshape(-1,1)
			except:
				print("self.Theta is not a n * 1 vector")
				return
		m = y.size
		if m == 0:
			return
		X = np.insert(x, 0, 1, axis=1)
		res = (1/m) * (np.transpose(X).dot(self.predict_(x) - y))
		#return (res.reshape((-1,)))
		return res

	def predict_(self, x):
		if x.ndim == 1:
			x = x.reshape(x.size, 1)
		res = np.insert(x, 0, 1, axis=1)
		if self.theta.ndim == 1:
			try:
				self.theta = self.theta.reshape(-1,1)
			except:
				print("self.Theta is not a n * 1 vector")
				return
		if res.shape[1] != self.theta.shape[0]:
			print("Mismatch between the shape of theta and x")
		ex = res.dot(self.theta)
		ex = self.sigmoid_(ex)
		return ex

	def loss_elem_(self, X, y):
		y_hat = self.predict_(X)
		try :
			y[0] - y_hat[0]
		except:
			print("Invalid input")
			return
		if y.ndim != 1:
			y = y.reshape(y.size)
		if y_hat.ndim != 1:
			y_hat = y_hat.reshape(y_hat.size)
		if y.shape != y_hat.shape:
			print(f"Wrong sizes: y = {y.shape} vs yhat = {y_hat.shape}")
			return
		res = np.zeros(len(y))
		res = [ a * log(b + self.eps) + (1-a)*log(1 - b -self.eps) for a,b in zip(y, y_hat) ]
		return (res)


	def loss_(self, x, y):
		y_hat = self.predict_(x)
		if y.ndim == 1:
			y.reshape((-1, 1))
		if y_hat.ndim == 1:
			y_hat.reshape((-1, 1))
		if y_hat.size != y.size:
			print("arguments have different lengths")
			return
		m = y.size
		ones = np.ones(y.shape[0]).reshape((-1,1))
		res = (-1 / m) * np.sum(y * np.log(y_hat + self.eps) + (ones - y)*np.log(ones - y_hat + self.eps))
		return res
