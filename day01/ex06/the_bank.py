#!/usr/bin/python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mlaplana <mlaplana@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/17 20:31:27 by mlaplana          #+#    #+#              #
#    Updated: 2020/11/17 20:31:27 by mlaplana         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object):

	ID_COUNT = 1
	
	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		if hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1
	
	def transfer(self, amount):
		self.value += amount

class Bank(object):
	def __init__(self):
		self.account = []
	
	def add(self, account):
		self.account.append(account)

	def transfer(self, origin, dest, amount):
		orig = None
		dst = None
		for each in self.account:
			if each.name == origin or each.id == origin:
				orig = each
			if each.name == dest or each.id == dest:
				dst = each
		if orig is None or dst is None:
			print("Invalid account.")
			return
		if orig == dst:
			print("Invalid transaction")
			return
		if orig.value < amount:
			print("Not enough money to make the transaction")
			return
		
		orig.value -= amount
		dst.value += amount
		print("Transaction succesful:\n" + "\tFrom {} to {}.".format(dst.name, orig.name))

	#def fix_account(self, account):

print(len(Account.__dict__))
print(len(dir(Account)))