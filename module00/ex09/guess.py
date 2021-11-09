import random
random.seed()

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")

i = random.randint(1,99)

def guessloop(val, i, nguess):
	if val == 42:
		print("blabla 42")
	if val == i:
		print("Congratulations, you've got it!")
		print("You won in", nguess, "attempts!")
		i = random.randint(1,99)
		return 0
	elif val > i:
		print("Too high!")
	else:
		print("Too low")
	return nguess

nguess = 0
while (1):
	tmp = input("What's your guess between 1 and 99?\n>> ")
	nguess += 1
	if not tmp.isdigit():
		if tmp == 'exit':
			print("Farewell")
			break
		print("write a number")
	elif int(tmp) > 99 or int(tmp) < 1:
		print("You're out of range")
	else:
		nguess = guessloop(int(tmp), i, nguess)
	