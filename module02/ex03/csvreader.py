from os.path import exists
from copy import deepcopy
import random

def generator(text, sep=" ", option=None):
	if not isinstance(text, str) or not (option in [None, "shuffle", "ordered", "unique"]):
		print("Error")
		return
	tmp = deepcopy(text)
	res = []
	while (tmp.find(sep) >= 0):
		res.append(tmp[:tmp.find(sep)])
		tmp = tmp[tmp.find(sep) + len(sep):]
	res.append(tmp)
	if option == "shuffle":
		rdn = []
		while len(rdn) < len(res):
			r = random.randint(0, len(res) - 1)
			if r not in rdn:
				rdn.append(r)
		res = [res[x] for x in rdn]
	elif option == "unique":
		res = list(dict.fromkeys(res))
	elif option == "ordered":
		res.sort()
	i = 0
	while i < len(res): 
		yield res[i]
		i += 1



class CsvReader(object):
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.header = header
		self.sep = sep
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		print("We get in there")

	def __enter__(self):
		if (not exists(self.filename)):
			print("File not found")
			self.file = None
		else:
			self.file = open(self.filename, 'r')
			mytext = self.file.read()
			i = 0
			self.data = []
			for oneline in generator(mytext, sep="\n"):
				if len(oneline) == 0:
					break
				self.data.append([])
				for word in generator(oneline, sep = self.sep):
					self.data[i].append(word)
				i += 1
			if self.sanitycheck():
				return
		return self

	def __exit__(self ,type, value, traceback):
		print("We close")
		if self.file:
			self.file.close()

	def sanitycheck(self):
		l = len(self.data[0])
		for line in self.data[1:]:
			if l != len(line):
				print("we have a problem")
				return (1)
		if self.header:
			self.header_val = deepcopy(self.data[0])
		i = 0
		while i < self.skip_top:
			self.data.pop(0)
			i += 1
		i = 0
		while i < self.skip_bottom:
			self.data.pop(len(self.data) - 1)
			i += 1



	def getdata(self):
		return self.data
	
	def getheader(self):
		if self.header == True:
			return self.header_val
		else:
			return


if __name__ == "__main__":
	with CsvReader('bad.csv') as file:
		if file == None:
			print("File is corrupted")

if __name__ == "__main__":
	with CsvReader('good.csv', header= True, skip_bottom=3) as file:
		data = file.getdata()
		print (data)
		header = file.getheader()
		print("First: ", header)

