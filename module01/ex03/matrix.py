from copy import deepcopy

class Matrix():
	def __init__(self, *args):
		self.mat = []
		self.lines = 0
		for i in args:
			self.lines += 1
			self.mat.append(i)
		self.columns = len(self.mat[0])
		if self.lines > 1:
			for i in self.mat[1:]:
				if self.columns != len(i):
					print("Invalid matrix, all lines don't have the same size")


	def __str__(self):
		txt = "["
		for i in self.mat[:-1]:
			txt += str(i) + ",\n"
		txt += str(self.mat[-1]) + "]"
		return txt

	def __add__(self, other):
		if isinstance(other, Matrix):
			if other.columns == self.columns and other. lines == self.lines:
				res = deepcopy(self)
				for i in range(res.lines):
					res.mat[i] = [a + b for a, b in zip(self.mat[i], other.mat[i])]
				return res
			elif other.columns == 1:
				if other.lines == 1:
					return self + other.mat[0][0]
				else:
					print("Error: Invalid addition")
					return
			else:
				print("Error: Invalid addition")
				return
		else:
			res = deepcopy(self)
			for i in range(res.lines):
				res.mat[i] = [a + other for a in self.mat[i]]
			return res

	def __radd__(self, other):
		if other == 0:
			return self
		else:
			return self + other

	def __sub__(self, other):
		if isinstance(other, Matrix):
			if other.columns == self.columns and other. lines == self.lines:
				res = deepcopy(self)
				for i in range(res.lines):
					res.mat[i] = [a - b for a, b in zip(self.mat[i], other.mat[i])]
				return res
			elif other.columns == 1:
				if other.lines == 1:
					return self - other.mat[0][0]
				else:
					print("Error: Invalid addition")
					return
			else:
				print("Error: Invalid addition")
				return
		else:
			res = deepcopy(self)
			for i in range(res.lines):
				res.mat[i] = [a - other for a in self.mat[i]]
			return res

	def __rsub__(self, other):
		print("You're substracting a scalar by a matrix, don.t")
		
	# # sub : vectors and matrices, can have errors with vectors and matrices.
	def __truediv__(self, other):
		if isinstance(other, Matrix):
			if other.columns == 1 and other.lines ==1:
				return self / other.mat[0][0]
			print("You cannot divide by a matrix")
			return
		else:
			res = deepcopy(self)
			try:
				for i in range(res.lines):
					res.mat[i] = [a / other for a in self.mat[i]]
				return res
			except:
				print("Don't divide by zero")
				return


	def __rtruediv__(self, other):
		print("You cannot divide by a matrix")
# # div : only scalars.
# __mul__
# __rmul__
# # mul : scalars, vectors and matrices , can have errors with vectors and matrices.
# # if we perform Matrix * Vector (dot product), return a Vector.
# __str__
# __repr__