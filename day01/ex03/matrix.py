#!/usr/bin/python3

class Matrix:
	def __init__(self, *args):
		try:
			if len(args) == 1 and type(args[0]) == list:
				self.matrix = [[]] * len(args[0])
				for i in args[0]:
					if (type(i) != list):
						raise ValueError
					for j in range(len(i)):
						self.matrix[i].append(j)
			else:
				raise ValueError
		except ValueError:
			print("Initialization error")

m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
                [0.0, 2.0, 4.0, 6.0]])

print(m1)