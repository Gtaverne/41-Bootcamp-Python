from os import getuid
import time
from random import randint
import sys
import os


class CoffeeMachine():
	
	def log(func):
		def magic(self, *args):
			start = time.time()*1000
			res = func(self, *args)
			stop = time.time()*1000
			original_stdout = sys.stdout
			with open('machine.log', 'a') as f:
				sys.stdout = f
				T = stop - start
				#print("(",os.getlogin(), ")", "Running: ", func.__name__, "[ exec-time = ", end=""
				print(f"( {os.getlogin()} ) Running: {func.__name__:<25} [ exec-time = ", end="")
				if T > 1000:
					print(round(T / 1000, 3), "s]")
				else:
					print(round(T, 3), "ms]")
				sys.stdout = original_stdout
				f.close()
			return res
		return magic
	
	
	
	water_level = 100
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
	
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")



if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	
	machine.make_coffee()
	machine.add_water(70)
		
		
		
		