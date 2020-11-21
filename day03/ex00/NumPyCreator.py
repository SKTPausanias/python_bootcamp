import numpy as np

class NumPyCreator():
	@staticmethod
	def from_list(lst, type=None):
		return np.array(lst, type)
	
	@staticmethod
	def from_tuple(tpl, type=None):
		return np.array(tpl, type)
	
	@staticmethod
	def from_iterable(itr, type=None):
		return np.array([i for i in itr], type)
	
	@staticmethod
	def from_shape(shape, value=0, type=None):
		return np.full(shape, value, type)

	@staticmethod
	def random(shape, type=None):
		return np.full(shape, np.random.random_sample(shape), type)
	
	@staticmethod
	def identity(n, type=None):
		return np.identity(n, type)

if __name__ == "__main__":
	print(NumPyCreator.from_list([[1, 2, 3], [6, 3, 4]]))
	print(NumPyCreator.from_tuple(("a", "b", "c")))
	print(NumPyCreator.from_iterable(range(5)))
	print(NumPyCreator.from_shape((3, 5)))
	print(NumPyCreator.random((3, 5)))
	print(NumPyCreator.identity(5))

