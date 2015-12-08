#!/usr/bin/env python3

"""Docstring
"""

__author__ = "6082200: Oles Pidgornyy, 6040608: Phillip Berger"
__email__ = "pidgornyy@informatik.uni-frankfurt.de," \
						"berger.phillip@hotmail.com"


from thing import Thing

class Mouse(Thing):

	symbol = "M"

	offspring_interval = 12
	age_current = 0
	age_max = 25
	hunger_current = 0
	hunger_max = 7


	def __init__(self):
		pass

	def perform_action(self):
		self.age_current += 1

	def is_dead(self):
		if self.age_current >= self.age_max:
			return True
		return False