import copy

cookbook = {
	"sandwich": {},
	"cake": {},
	"salad" : {},
	}

emptydic = {
	"ingredients": [],
	"meal": "",
	"prep_time": 0,
}

sand_dic = copy.deepcopy(emptydic)
sand_dic["ingredients"].extend(["ham", "bread", "cheese", "tomatoes"])
sand_dic["meal"] = "lunch"
sand_dic["prep_time"] = 10
cookbook["sandwich"] = sand_dic

cake_dic = copy.deepcopy(emptydic)
cake_dic["ingredients"].extend(["flour", "sugar", "egg"])
cake_dic["meal"] = "dessert"
cake_dic["prep_time"] = 60
cookbook["cake"] = cake_dic

salad_dic = copy.deepcopy(emptydic)
salad_dic["ingredients"].extend(["avocado", "arugula", "tomatoes", "spinach"])
salad_dic["meal"] = "lunch"
salad_dic["prep_time"] = 15
cookbook["salad"] = salad_dic

val = -1

def printoptions():
	print("Please select an option by typing the corresponding number:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")

def print_recipe(recipe):
	if (recipe in cookbook):
		print("Ingredient list:", ' '.join(cookbook[recipe]["ingredients"]))
		print("To be eaten for", cookbook[recipe]["meal"])
		print("Takes", cookbook[recipe]["prep_time"], "minutes cooking")
	else:
		print("unavailable recipe")
	print()

def del_recipe(recipe):
	sure = input(f"Are you sure you want to delete {recipe}? [yes/no] ")
	if sure == "yes":
		del cookbook[recipe]

def add_recipe():
	i = 0
	print("Write recipe name")
	rec_name = input()
	print(rec_name)
	str = input(f"Are you sure you want to create {rec_name}? [yes/no] ")
	if str == "yes":
		cookbook[rec_name] = copy.deepcopy(emptydic)
		j = 0
		ing = []
		while (j == 0):
			print("Write ingredients")
			ing.append(input(" >> "))
			print("Ingredients: ", end = "")
			for i in ing:
				print(i, end= " ")
			print()
			str = input(f"Are you done? [yes/no] ")
			if str == "yes":
				cookbook[rec_name]["ingredients"] = ing
				break
		print("Which meal is it")
		ml = input()
		print(f"It is a {ml}")
		cookbook[rec_name]["meal"] = ml
		print("How long does it take?")
		tm = input()
		print(f"It takes {tm} minutes")
		if (not tm.isdigit()):
			tm = 0
		cookbook[rec_name]["prep_time"] = int(tm)
		print_recipe(rec_name)
		checkout = input(f"Are we done? [yes/no] ")
		if checkout == "yes":
			return
		else:
			del cookbook[rec_name]
			return




val = '0'
while (val != '5'):
	printoptions()
	val = input(">> ")
	if (not val.isdigit() or int(val) > 5 or int(val) < 0):
		print("'", val, "' is not a valable input, please make some effort")
	elif (int(val) == 1):
		add_recipe()
	elif (int(val) == 2):
		del_recipe(input("Which recipe do you want to delete? >>> "))
	elif (int(val) == 3):
		print_recipe(input("Which recipe do you want to print? >>> "))
	elif (int(val) == 4):
		for i in cookbook:
			print(i)
			print_recipe(i)
	else:
		print("This is the end")
print("Good bye")
