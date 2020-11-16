#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlaplana <mlaplana@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/16 18:51:57 by mlaplana          #+#    #+#              #
#    Updated: 2020/11/16 18:51:57 by mlaplana         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator():
	@staticmethod
	def zip_evaluate(coefs, words):
		try:
			if len(coefs) != len(words):
				raise ValueError
			zipp = zip(words, coefs)
			ret = 0
			for w, c in zipp:
				ret += len(w) * c
			return ret
		except ValueError:
			return -1
	
	@staticmethod
	def enumerate_evaluate(coefs, words):
		try:
			if len(coefs) != len(words):
				raise ValueError
			ret = 0
			for i, w in enumerate(words):
				ret += len(w) * coefs[i]
			return ret
		except ValueError:
			return -1
