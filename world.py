#!/usr/bin/env python3

"""Docstring
"""

import random

__author__ = "6082200: Oles Pidgornyy, 6040608: Phillip Berger"
__email__ = "pidgornyy@informatik.uni-frankfurt.de," \
						"berger.phillip@hotmail.com"


class World:

	world = {}

	def __init__(self, rows=50, cols=50):
		self.rows = rows
		del rows
		self.cols = cols
		del cols
		for row in range(self.rows):
			for col in range(self.cols):
				self.world.update({(row, col): None})
		pass

	def view_world(self):
		for row in range(self.rows):
			for col in range(self.cols):
				if self.world[(row,col)] == None:
					print('N', end="")
			print()

	def add_thing(self, posx, posy):
		pass

world = World(rows=10, cols=20)
world.view_world()