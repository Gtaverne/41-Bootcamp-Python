import numpy as np
from time import time
import matplotlib.pyplot as plt


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

		

	def predict_(self, x):
		if x.ndim == 1:
			x = x.reshape(x.size, 1)
		res = np.insert(x, 0, 1, axis=1)
		return res.dot(self.thetas)

	def predict_plot(self, x, theta):
		if x.ndim == 1:
			x = x.reshape(x.size, 1)
		res = np.insert(x, 0, 1, axis=1)
		return res.dot(theta)

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
		return(np.sum(dif * dif) / (L))

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
		plt.title(f"Cost = {self.loss_(y,ypred)}")
		plt.show()

	def lossplot(self, x, y, n_theta0=6):
		if self.thetas[0] > 0:
			theta_0range = [self.thetas[0] * 0.9, self.thetas[0] * 1.1]
		else:
			theta_0range = [self.thetas[0] *1.1, self.thetas[0] * 0.9]
		
		if self.thetas[1] > 0:
			theta_1range = [self.thetas[1] * 0.7, self.thetas[1] * 1.6]
		else:
			theta_1range = [self.thetas[1] *1.6, self.thetas[1] * 0.7]

		abs = np.arange(theta_1range[0], theta_1range[1], (theta_1range[1] - theta_1range[0]) /100)
		ncurv = np.arange(theta_0range[0], theta_0range[1], (theta_0range[1] - theta_0range[0]) /n_theta0)
		print(self.thetas.shape)
		for i in ncurv:

			ord = [self.loss_(y, self.predict_plot(x, np.array([i, t1]).reshape((2,1)))) for t1 in abs]
			plt.plot(abs, ord, "-b")
		plt.ylim(20,140)
		plt.show()