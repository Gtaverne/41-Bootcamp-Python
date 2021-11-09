class Recipe:
	def __init__(self, name, cooking_lvl=1, cooking_time=10, ingredients=[], description="", recipe_type="lunch"):
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = ""
		txt = self.name + "\nCooking level: " + \
		str(self.cooking_lvl) + "\nCooking time: " + \
		str(self.cooking_time) + "\ningredients:"
		for i in self.ingredients:
			txt += " " + i
		txt += "\nDescription: " + self.description + \
			"\nRecipe type: " + self.recipe_type

		return txt

	def initialize(self):
		self.name = input("Write the real namme\n>>")
		lvl_tmp = input("Write the level\n>> ")
		if (not lvl_tmp.isdigit()):
			self.cooking_lvl = 0
		else:
			self.cooking_lvl = abs(int(lvl_tmp))
		ck_tmp = input("Write the cooking time\n>> ")
		if (not ck_tmp.isdigit()):
			self.cooking_time = 0
		else:
			self.cooking_time = abs(int(ck_tmp))
		j = 0
		ing = []
		while (j == 0):
			ing.append(input("Write ingredients\n>> "))
			print("Ingredients: ", end = "")
			for i in ing:
				print(i, end= " ")
			print()
			str = input(f"Are you done? [yes/no] >> ")
			if str == "yes":
				self.ingredients = ing
				break
		self.description = input("Now write the description\n >> ")
		tpe = input("Is it:\n1- a lunch\n2- a dessert\n3- a starter?\n>> ")
		if tpe == "1":
			self.recipe_type = "lunch"
		elif tpe == "2":
			self.recipe_type = "dessert"
		elif tpe == "3":
			self.recipe_type = "starter"
		else:
			print("You can't write properly a number between 1 and 3, let's say it's a lunch")
			self.recipe_type = "lunch"
		print((self))
		check = input("Are you happy with it? [yes/no/retry] ")
		if check == "retry":
			self.initialize()
		elif check == "no":
			self = Recipe("Nothingburger")

