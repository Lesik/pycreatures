#!/usr/bin/env python3

"""Docstring
"""

from thing import Thing

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

	def rem_thing(self, posx, posy):
		self.world.update({(posx, posy): None})

	def view_coordinate(self, row, col):
		if self.world[(row, col)] is None:
			return '.'
		else:
			return self.world[(row, col)]

	def view_world(self):
		for row in range(self.rows):
			for col in range(self.cols):
				print(self.view_coordinate(row, col), end='')
			print()

	def add_thing(self, posx, posy):
		self.world.update({(posx, posy): Thing()})

	def get_cardpoint_pos(self, posy, posx, cardpoint):
		offsetx = 0
		offsety = 0
		if (cardpoint == 0):
			offsety = -1
		elif (cardpoint == 1):
			offsetx = 1
		elif (cardpoint == 2):
			offsety = 1
		elif (cardpoint == 3):
			offsetx = -1

		if posx == 0:
			return self.world[(posy, self.cols - 1)]
		elif posy == 0:
			return self.world[(self.rows - 1, posx)]
		else:
			return self.world[(posy + offsety, posx + offsetx)]


world = World(rows=29, cols=79)
world.add_thing(0, 15)
world.add_thing(9, 15)
world.add_thing(5, 5)
world.rem_thing(9, 15)
world.view_world()
print(world.view_coordinate(0, 15))
print(world.get_cardpoint_pos(0, 15, 0))
print(world.get_cardpoint_pos(1, 15, 0))
print(world.get_cardpoint_pos(5, 4, 1))
