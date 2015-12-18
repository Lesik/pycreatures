#!/usr/bin/env python3

""" A world class that can contain things.
"""

from thing import Thing

__author__ = "6040608: Phillip Berger, 6082200: Oles Pidgornyy"
__email__ = "pidgornyy@informatik.uni-frankfurt.de," \
			"berger.phillip@hotmail.com"


class World:
	world = {}

	def __init__(self, rows=50, cols=50):
		""" Initialize the world.
		:param rows: height of the world
		:param cols: width of the world
		:return: nothing
		"""
		# code very self-explanatory due to well-choosen var names
		self.rows = rows
		del rows
		self.cols = cols
		del cols
		for row in range(self.rows):
			for col in range(self.cols):
				self.world.update({(row, col): None})

	def rem_thing(self, posy, posx):
		""" Removes an object from the worlds at given position.
		:param posy: y position of object
		:param posx: x position of object
		:return: nothing
		"""
		self.world.update({(posy, posx): None})

	def view_coordinate(self, row, col):
		""" Returns the object from a coordinate, '.' if None.
		:param row: y position of wanted object
		:param col: x position of wanted object
		:return: nothing
		"""
		if self.world[(row, col)] is None:
			return '.'
		else:
			return self.world[(row, col)]

	def view_world(self):
		""" Print whole world.
		:return: nothing
		"""
		# for every coordinate in world, view_coordinate() is run
		for row in range(self.rows):
			for col in range(self.cols):
				print(self.view_coordinate(row, col), end='')
			print()

	def add_thing(self, posy, posx):
		""" Adds a Thing() to given position.
		:param posy: y position of wanted object
		:param posx: x position of wanted object
		:return: nothing
		"""
		self.world.update({(posy, posx): Thing()})

	def get_cardpoint_pos(self, posy, posx, cardpoint):
		""" Return object at [cardinal direction] of given position
		"""
		offsetx = 0
		offsety = 0
		# set offset depending on cardinal direction
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


# Create a new world
world = World(rows=10, cols=20)
# Add a thing at x=15 y=0
world.add_thing(0, 15)
# Add a thing at x=15 y=9
world.add_thing(9, 15)
print("Object at x=15 y=0 is", world.view_coordinate(0, 15))
print("To the north of x=15 y=0 is", world.get_cardpoint_pos(0, 15, 0))
#print("To the north of x=15 y=1 is", world.get_cardpoint_pos(1, 15, 0))
print("Deleting object at x=15 y=9.")
world.rem_thing(9, 15)
print("To the north of x=15 y=0 is", world.get_cardpoint_pos(0, 15, 0))
# Print world
world.view_world()