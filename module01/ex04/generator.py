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


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
	print(word)

print("\nNOW IT IS SHUFFLED")
for word in generator(text, sep=" ", option="shuffle"):
	print(word)

print("\nNOW IT IS ORDERED")
for word in generator(text, sep=" ", option="ordered"):
	print(word)


print("\nNOW IT IS ONLY UNIQUE ELEMENTS")
for word in generator("bla bla bla blo", sep=" ", option="unique"):
	print(word)

print("\nNOW IT IS SHOULD NOT WORK")
for word in generator(1.2541235, sep=" ", option=""):
	print(word)