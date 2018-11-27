#! /usr/bin/env python3
# coding: utf-8

#class.py
""" Python module that define all the classes needed for the game Help MacGyver to escape !"""

import pygame
from pygame.locals import *

from init import *

class Labyrinth:
	""" Class that create the structure of the boardgame form a file and allows to display with pygame """

	def __init__(self, file):
		""" Method that initialize a Labyrinth object """
		self.file = file
		self.structure = []

	def generate(self):
		""" Method that generates the structure of the labyrinth from a file template """
		with open(self.file, "r") as file:
			lab_structure = []
			for row in file:
				lab_row = []
				for char in row:
					if char != "\n":
						lab_row.append(char)
				lab_structure.append(lab_row)
			self.structure = lab_structure

	def display_lab(self, window):
		""" Method that displays the generated structure with the appropriate texture """

		wall = pygame.image.load(picture_wall).convert_alpha()
		wall = pygame.transform.scale(wall, (sprite_size, sprite_size))
		start = pygame.image.load(picture_start).convert_alpha()
		start = pygame.transform.scale(start, (sprite_size,sprite_size))
		goal = pygame.image.load(picture_goal).convert_alpha()
		goal = pygame.transform.scale(goal, (sprite_size,sprite_size))
		floor = pygame.image.load(picture_empty).convert_alpha()
		floor = pygame.transform.scale(floor,(sprite_size,sprite_size))

		n_row = 0
		for row in self.structure:
			n_sprite = 0
			for sprite in row:
				x = n_sprite * sprite_size
				y = n_row * sprite_size
				if sprite == "w":
					window.blit(wall, (x,y))
				elif sprite == "e":
					window.blit(floor, (x,y))
				elif sprite == "d":
					window.blit(start, (x,y))
				elif sprite == "a":
					window.blit(goal, (x,y))
				n_sprite += 1
			n_row += 1