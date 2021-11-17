import numpy as np
from time import time

class MyLinearRegression():
	"""
	Description:
	My personnal linear regression class to fit like a boss.
	"""
	def __init__(self, thetas, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		if type(thetas) == type(np.array([])):
			self.thetas = thetas
		else:
			self.thetas = np.array(thetas)

		

	def gradient(self, x, y, verbose=False):

		if type(x) != type(np.array([])) or type(y) != type(np.array([])):
			print("incorrect inputs, x and y are not even numpy arrays")
			return
		if x.ndim == 1:
			x = x.reshape(x.size, 1)
		if y.ndim == 1:
			y = y.reshape(y.size, 1)
		if x.shape != y.shape :
			print("incorrect inputs, x and y have different dimensions")
			return
		if self.thetas.shape != (2, 1):
			try:
				self.thetas = self.thetas.reshape(2,1)
			except:
				print(f"self.Thetas is not a 2 * 1 vector: {self.thetas.shape}")
				return
		X = np.insert(x, 0, 1, axis=1)
		res = (1 / y.size) * (np.transpose(X).dot(X.dot(self.thetas) - y))
		if verbose:
			print(X.dot(self.thetas))
			print(res.shape)
		return (res) #double think if you need a .reshape(2) here

	def fit_(self, x, y, verbose = False):	
		if self.thetas.ndim == 1:
			self.thetas = self.thetas.reshape(self.thetas.size, 1)

		if verbose:
			ret = 0
			listy = range(self.max_iter)
			for elem in self.ft_progress(listy):
				ret += elem
				self.thetas = self.thetas - self.alpha * self.gradient(x,y)
			print()

		else:
			for i in range(self.max_iter):
				if verbose:
					print(f"i: {i} , self.thetas = {self.thetas}")
				self.thetas = self.thetas - self.alpha * self.gradient(x,y)
		return self.thetas


	def predict_(self, x):
		if x.ndim == 1:
			x = x.reshape(x.size, 1)
		res = np.insert(x, 0, 1, axis=1)
		return res.dot(self.thetas)

	@staticmethod
	def loss_elem_(y, y_hat):
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
		res = [ (a - b)**2 for a,b in zip(y, y_hat) ]
		return (res)


	@staticmethod
	def loss_(y, y_hat):
		if y.ndim != 1:
			y = y.reshape(y.size)
		if y_hat.ndim != 1:
			y_hat = y_hat.reshape(y_hat.size)
		L = y.size
		dif = y - y_hat
		return(np.sum(dif * dif) / ( 2 * L))

	@staticmethod
	def ft_progress(lst):
		for i in lst:
			if i == 0:
				start = time()
			i = i+1
			lmax = len(lst)
			t = time() - start
			av = 100 * i / lmax

			if av != 0:
				ETA = (str(round(t * 100 / av - t, 2)))
			else:
				ETA = "inf"

			beg = "ETA: " + ETA +"s "
			sec = "["  + str(round(av,1)) + "%]"
			bar = "["
			lenbar = int(av / 4)
			for k in range(lenbar):
				bar += "="
			bar += ">"

			print(f"{beg :<12}{sec :<8}{bar :<27}] {i}/{lmax}  | elapsed time {round(t, 2)}", end = "\r")
			yield i		
