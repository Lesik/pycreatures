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

	def get_coordinate(self, row, col):
		if self.world[(row, col)] is None:
			return '.'
		else:
			return self.world[(row, col)]

	def view_world(self):
		for row in range(self.rows):
			for col in range(self.cols):
				print(self.get_coordinate(row, col), end='')
			print()

	def add_thing(self, posx, posy):
		self.world.update({(posx, posy): Thing()})


def get_pos(self, posx, posy):
    print(self.world[(posx, posy)])


def get_cardpoint_pos(self, posx, posy, cardpoint):
    if cardpoint == 0:
        if posy == 0:
            print(self.world[(posx, self.rows)])
        else:
            print(self.world[(posx, posy - 1)])
    else:
        pass


world = World(rows=10, cols=20)
print("      Empty world:")
world.view_world()
world.add_thing(0, 15)
print("      Added Thing at 0, 15:")
world.view_world()
world.add_thing(9, 15)
print("      Added Thing at 9, 15:")
world.view_world()
world.rem_thing(9, 15)
print("      Removed Thing at 9, 15:")
world.view_world()