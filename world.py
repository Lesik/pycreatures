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
        pass

    def rem_thing(self, posx, posy):
        self.world.update({(posx, posy): None})

    def view_coordinate(self, row, col):
        if self.world[(row, col)] is None:
            print('.', end='')
        else:
            print(self.world[(row, col)], end='')

    def view_world(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.view_coordinate(row, col)
            print()

    def add_thing(self, posx, posy):
        self.world.update({(posx, posy): Thing()})

    def get_pos(self, posx, posy):
        pos = self.world[(posx, posy)]
        print(pos)


world = World(rows=10, cols=20)
world.add_thing(0, 15)
world.add_thing(9, 15)
world.rem_thing(9, 15)
world.view_world()
world.get_pos(0, 15)
