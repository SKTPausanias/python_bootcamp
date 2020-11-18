#!/usr/bin/python

def ft_filter(function_to_apply, list_of_inputs):
	return [i for i in list_of_inputs if function_to_apply(i)]

if __name__ == '__main__':
	chars = "aBcDPPpeEeFgMm"
	print(list(ft_filter(str.isupper, chars)))
	print(list(filter(str.isupper, chars)))