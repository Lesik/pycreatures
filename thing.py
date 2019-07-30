#!/usr/bin/env python3

""" Thing class.
"""

import random

__author__ = "me and my partner"
__email__ = "email@university"


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
