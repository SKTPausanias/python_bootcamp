#!/usr/bin/python3

class Matrix:
	def __init__(self, *args):
		try:
			self.data = []
			if len(args) == 1 and type(args[0]) == list:
				for i in range(len(args[0])):
					self.data.append([])
				n = 0
				for i in args[0]:
					if (type(i) != list):
						raise ValueError
					for j in i:
						self.data[n].append(float(j))
					n += 1
				self.shape = (len(args[0]), len(self.data[0]))
			elif len(args) == 1 and type(args[0]) == tuple and len(args[0]) == 2:
				self.shape = args[0]
				for i in range(self.shape[0]):
					self.data.append([])
					for j in range(self.shape[1]):
						self.data[i].append(0.0)
			elif len(args) == 2 and type(args[0]) == list and type(args[1]) == tuple and len(args[0]) == args[1][0]:
				self.data = args[0]
				self.shape = args[1]
			else:
				raise ValueError
		except ValueError:
			print("Initialization error")
	
	def __str__(self):
		txt = "Matrix = "
		txt += "".join(str(self.data))
		return txt

	def __repr__(self):
		txt = "Matrix ="
		txt += " { data: " + "".join(str(self.data))
		txt += " , shape: " + "".join(str(self.shape)) + " }"
		return txt

lst = [[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]]

m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
                [0.0, 2.0, 4.0, 6.0]])

m2 = Matrix((3, 3))

m3 = Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]], (3, 3))

print(m1)
print(m2)
print(m3)