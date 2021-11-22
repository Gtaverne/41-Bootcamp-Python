import numpy as np
from time import time
import matplotlib.pyplot as plt
from polynomial_model import add_polynomial_features

class MyLinearRegression():
	def __init__(self, theta = [[1], [1]], alpha=0.001, max_iter=100000):
		self.alpha = alpha
		self.max_iter = max_iter
		if type(theta) == type(np.array([])):
			self.thetas = theta
		else:
			self.thetas = np.array(theta)
		print(self.thetas.shape)

	def gradient(self, x, y, Matrix=True):

		if type(x) != type(np.array([])) or type(y) != type(np.array([])):
			print("incorrect inputs, x and y are not even numpy arrays")
			return
		if x.ndim == 1:
			x = x.reshape(x.size, 1)
		if y.ndim == 1:
			y = y.reshape(y.size, 1)
		if x.shape[0] != y.shape[0] :
			print("incorrect inputs, x and y don't have the same length")
			return
		if self.thetas.ndim == 1:
			try:
				self.thetas = self.thetas.reshape(-1,1)
			except:
				print("self.Thetas is not a n * 1 vector")
				return
		res = (1 / y.size) * (np.transpose(x).dot(x.dot(self.thetas) - y))
		if Matrix == False:
			return (res.reshape((-1,))) #double think if you need a reshape here
		else:
			return (res)
	
	def fit_(self, x, y, Verbose = False):

		print(x)
		if self.thetas.ndim == 1:
			self.thetas = self.thetas.reshape(self.thetas.size, 1)
		alphvec = np.array([self.alpha / (10 ** (int(1.8*i))) for i in range(self.thetas.size)]).reshape((-1,1))
		print (alphvec)
		if Verbose == False:
			for i in range(self.max_iter):
				#for some reasons, on high dimensions (x**3 and more), you get an exploding gradient. So I built a vector of decreasing weights to limit the impact of high order coefficients
				self.thetas = self.thetas - alphvec * self.gradient(x,y)
		else :
			print(self.thetas.size)
			continuous_x = np.arange(1,10.01, 0.001).reshape(-1,1)
			continuous_x_cont = add_polynomial_features(continuous_x, self.thetas.size -1)
			lst = range(1000)
			for i in self.ft_progress(lst):
				for _ in range(1 + int(self.max_iter / 1000)):
					self.thetas = self.thetas - alphvec * self.gradient(x,y)
				#plt.plot(continuous_x, self.predict_(continuous_x_cont), color="orange")
		return self.thetas

	def predict_(self, x):
		if x.ndim == 1:
			x = x.reshape(x.size, 1)
		return x.dot(self.thetas)


	def mse_elem_(self, X, y):
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
		res = [ (a - b)**2 for a,b in zip(y, y_hat) ]
		return (res)


	def mse_(self, x, y_hat):
		y = self.predict_(x)
		if y.ndim == 1:
			y = y.reshape(y.size, 1)
		if y_hat.ndim == 1:
			y_hat = y_hat.reshape(y_hat.size, 1)
		L = y.size
		dif = y - y_hat
		return(np.sum(dif * dif) / ( L)) 

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

	def plot(self, x, y):
		plt.plot(x, y, 'o')

		ypred = self.predict_(x)
		if len(x) < 50:
			for i in range(len(x)):
				plt.plot([x[i], x[i]], [ypred[i], y[i]], '--r')

		plt.plot(x, ypred)
		plt.title(f"Cost = {self.mse_(y,ypred)}")
		plt.pause(0.05)
		plt.show()
