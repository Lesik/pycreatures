#!/usr/bin/env python3

"""Docstring
"""

__author__ = "6082200: Oles Pidgornyy, 6040608: Phillip Berger"
__email__ = "pidgornyy@informatik.uni-frankfurt.de," \
						"berger.phillip@hotmail.com"


from thing import Thing


class Corn(Thing):

	symbol = "§"
	seed_cycle = 6

	def perform_action(self):
		pass