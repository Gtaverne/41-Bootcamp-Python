import numpy as np

class MyLinearRegression():
	def __init__(self, thetas, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		if type(thetas) == type(np.array([])):
			self.thetas = thetas
		else:
			self.thetas = np.array(thetas)
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
		X = np.insert(x, 0, 1, axis=1)
		res = (1 / y.size) * (np.transpose(X).dot(X.dot(self.thetas) - y))
		if Matrix == False:
			return (res.reshape((-1,))) #double think if you need a reshape here
		else:
			return (res)
	
	def fit_(self, x, y):

		if self.thetas.ndim == 1:
			self.thetas = self.thetas.reshape(self.thetas.size, 1)

		for i in range(self.max_iter):
			self.thetas = self.thetas - self.alpha * self.gradient(x,y)
		return self.thetas

	def predict_(self, x):
		if x.ndim == 1:
			x = x.reshape(x.size, 1)
		res = np.insert(x, 0, 1, axis=1)
		return res.dot(self.thetas)

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
		res = [ (a - b)**2 for a,b in zip(y, y_hat) ]
		return (res)


	def loss_(self, x, y_hat):
		y = self.predict_(x)
		if y.ndim == 1:
			y = y.reshape(y.size, 1)
		if y_hat.ndim == 1:
			y_hat = y_hat.reshape(y_hat.size, 1)
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
