#!/usr/bin/env python3

""" Thing class.
"""

import random

__author__ = "6082200: Oles Pidgornyy, 6040608: Phillip Berger"
__email__ = "pidgornyy@informatik.uni-frankfurt.de," \
			"berger.phillip@hotmail.com"


class Thing:

	symbol = "T"

	def __init__(self):
		""" Do nothing yet.
		"""
		pass

	def __str__(self):
		""" Return own symbol.
		"""
		return self.symbol

	def get_age(self):
		return self.age

	def perform_action(self):
		self.age += 1