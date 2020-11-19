import time
from random import randint
from string import capwords
from functools import wraps
import getpass

def log(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		ret = func(*args, **kwargs)
		ex_time = time.time() - start
		if int(ex_time) > 0:
			t = "s"
		else:
			ex_time *= 1000
			t = "ms"
		f = open("machine.log", "a")
		f.write("({})Running: {}    [ exec-time = {} {} ]\n".format(
			getpass.getuser(),
			(capwords(func.__name__.replace('_', ' '))).ljust(13),
			round(ex_time, 3),
			str(t).ljust(2)))
		f.close()	
		return ret
	return wrapper

class CoffeeMachine():

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