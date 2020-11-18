#!/usr/bin/python
from operator import add, mul
from functools import reduce

def ft_reduce(function_to_apply, list_of_inputs):
	initializer = None
	it = iter(list_of_inputs)
	try:
		initializer = next(it)
	except StopIteration:
		raise TypeError('reduce() of empty sequence with no initial value')	
	ret = initializer
	for i in it:
		ret = function_to_apply(ret, i)
	return ret

if __name__ == '__main__':
    print("ft_reduce:   " + str(ft_reduce(add, range(10))))
    print("reduce   :   " + str(reduce(add, range(10))))
    print("ft_reduce:   " + str(ft_reduce(mul, range(1, 5))))
    print("reduce   :   " + str(reduce(mul, range(1, 5))))