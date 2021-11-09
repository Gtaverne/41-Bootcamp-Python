from recipe import Recipe
from datetime import datetime


class Book:
	"""The book class"""
	
	def __init__(self, name,):
		self.name = name
		now = datetime.now()
		self.last_update = now.strftime("%d/%m/%Y %H:%M:%S")
		self.creation_date = now.strftime("%d/%m/%Y %H:%M:%S")
		self.recipe_list = {}

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		try:
			print(self.recipe_list[name])
			return self.recipe_list[name]
		except:
			print ("No such recipe")
			return 

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		pass

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		self.recipe_list[recipe.name] = recipe
		now = datetime.now()
		self.last_update = now.strftime("%d/%m/%Y %H:%M:%S")