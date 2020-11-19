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
		if not hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1
	
	def transfer(self, amount):
		self.value += amount

class Bank(object):
	def __init__(self):
		self.account = []
	
	def add(self, account):
		self.account.append(account)

	def iscorrupted(self, account):
		ret = True
		for i in account.__dict__:
			if i.startswith('zip') or i.startswith('addr'):
				ret = False
				break
		if ret is True:
			return ret	
		if len(account.__dict__) % 2 == 0:
			return True
		for i in account.__dict__:
			if i.startswith('b'):
				return True
		if 'name' not in account.__dict__:
			return True
		if 'id' not in account.__dict__:
			return True
		if 'value' not in account.__dict__:
			return True
		return ret

	def transfer(self, origin, dest, amount):
		orig = None
		dst = None
		for i in self.account:
			if i.name == origin or i.id == origin:
				orig = i
			if i.name == dest or i.id == dest:
				dst = i
		if orig is None or dst is None:
			print("Invalid account.")
			return False
		if self.iscorrupted(orig) is True or self.iscorrupted(dst) is True:
			print("Corrupted account")
			return False			
		if orig == dst:
			print("Invalid transaction")
			return False
		if orig.value < amount:
			print("Not enough money to make the transaction")
			return False
		
		orig.value -= amount
		dst.value += amount
		print("Transaction succesful:\n" + "\tFrom {} to {}.".format(dst.name, orig.name))
		return True

	def fix_account(self, account):
		acc = None
		for i in self.account:
			if i.name == account or i.id == account:
				acc = i
		if acc is None:
			print("Invalid account.")
		for i in acc.__dict__:
			if i.startswith('b'):
				del acc.__dict__[i]
				break
		if 'name' not in acc.__dict__:
			acc.__dict__.update(name="Default")
		if 'value' not in acc.__dict__:
			acc.__dict__.update(value=0)
		if 'id' not in acc.__dict__:
			acc.__dict__.update(id=acc.ID_COUNT)
			acc.ID_COUNT += 1
		if (self.iscorrupted(acc)):
			return False
		return True