from book import Book
from recipe import Recipe

newrec = Recipe("A BRAND NEW RECIPE")

# newrec.initialize()
# print(str(newrec))

#We'll initialize it with a couple recipes, for fun

soup = Recipe("soup", cooking_lvl = 2, cooking_time = 30, ingredients = ["carrot", "potatoes", "onion", "salt"], description = "Good stuff")

fruitsalad = Recipe("fruit salad", cooking_lvl = 1, cooking_time = 15, ingredients = ["apple", "banana", "orange", "cherry"], description = "Good sweet stuff", recipe_type = "dessert")

lelivre = Book("Goodstuff")
lelivre.add_recipe(soup)
lelivre.add_recipe(fruitsalad)

lelivre.get_recipes_by_types("dessert")


lelivre