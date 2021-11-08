import sys
import string

def text_analyzer(text =""):
	"""This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text. Blablabla"""
	if text == "":
		print("What is the text to analyse?\n>>", end=" ")
		text = str(input())
	print("The text contains", len(text), "characters:")
	print("-", sum( x.isupper() for x in text), "upper letters")
	print("-", sum( x.islower() for x in text), "lower letters")
	print("-", sum( x in string.punctuation for x in text), "punctuation")
	print("-", sum( x == " " for x in text), "spaces")