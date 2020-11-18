#!/usr/bin/python

def ft_map(function_to_apply, list_of_inputs):
	return [function_to_apply(i) for i in list_of_inputs]

if __name__ == '__main__':
    chars = "aBcDeFghiJk"
    print(ft_map(str.upper, chars))
    print(list(map(str.upper, chars)))
    print(ft_map(lambda n: 2 * n, range(5)))
    print(list(map(lambda n: n * n, range(5))))