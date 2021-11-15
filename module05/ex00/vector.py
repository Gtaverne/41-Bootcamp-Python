class Vector():
	def __init__(self, arr):
		self.val = arr

	def __str__(self):
		txt = "["
		for i in self.val[:-1]:
			txt += str(i) + ", "
		txt += str(self.val[-1]) + "]"
		return txt

	def __add__(self, other):
		if (isinstance(other, Vector)):
			if len(other.val) != len(self.val):
				print ("Error: You're trying to add vectors of different size")
				return
			return (Vector([x+y for x, y in zip(self.val, other.val)]))
		else:
			return (Vector([x+other for x in self.val]))

	def __radd__(self, other):
		if other == 0:
			return self
		else:
			return self.__add__(other)

	def __sub__(self, other):
		if (isinstance(other, Vector)):
			if len(other.val) != len(self.val):
				print ("Error: You're trying to substract vectors of different sizes")
				return
			return (Vector([x-y for x, y in zip(self.val, other.val)]))
		else:
			return (Vector([x-other for x in self.val]))

	def __rsub__(self, other):
		return Vector([other - x for x in self.val])

# sub : vectors and scalars, can have
	def __truediv__(self, other):
		if (isinstance(other, Vector)):
			print ("Error: You're trying to divide 2 vectors")
			return
		try:
			return Vector([x / other for x in self.val])
		except:
			print("Error: Division by zero")
			return
	def __rtruediv__(self, other):
		print ("Error: You're trying to divide a scalar by a vector")
		return
	
	def __mul__(self, other):
		if (isinstance(other, Vector)):
			if len(other.val) != len(self.val):
				print ("Error: You're trying to multiply vectors of different sizes")
				return
			return (sum([x * y for x, y in zip(self.val, other.val)]))
		else:
			print("here we are")
			res = [el * other for el in self.val]
			return (Vector(res))

	def __rmul__(self, other):
		return self * other


	def __repr__(self):
		txt = ""
		txt = "Vector(" + str(self) + ")"
		return txt