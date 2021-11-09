from book import Book
from recipe import Recipe

newrec = Recipe("A BRAND NEW RECIPE")

# newrec.initialize()
# print(str(newrec))

#We'll initialize it with a couple recipes, for fun

soup = Recipe("Soup", cooking_lvl = 1, cooking_time = 30, ingredients = ["carrot", "potatoes", "onion", "salt"], description = "Good stuff")

print(soup)
