#! /usr/bin/env python3
# coding: utf-8

#classes.py
""" Python module that define all the classes needed for the game Help MacGyver to escape !"""

import pygame
from pygame.locals import *

from init import *

class Labyrinth:
	""" Class that create the structure of the boardgame form a file and allows to display with pygame """

	def __init__(self, file, wall_img, floor_img, goal_img):
		""" Method that initialize a Labyrinth object """
		self.file = file
		self.wall_img = wall_img
		self.floor_img = floor_img
		self.goal_img = goal_img
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

		n_row = 0
		for row in self.structure:
			n_sprite = 0
			for sprite in row:
				x = n_sprite * sprite_size
				y = n_row * sprite_size
				if sprite == "w":
					window.blit(self.wall_img, (x,y))
				elif sprite == "e":
					window.blit(self.floor_img, (x,y))
				elif sprite == "d":
					window.blit(self.floor_img, (x,y))
				elif sprite == "a":
					window.blit(self.goal_img, (x,y))
				n_sprite += 1
			n_row += 1

class Char:
	""" Class that create character for the game """

	def __init__(self, name, char_img, labyrinth, window, pos_x, pos_y):
		self.name = name
		self.char_img = char_img
		self.labyrinth = labyrinth
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.life = 100
		self.objects = [1,2]
		self.direction = "right"
		self.window = window

	def position_char(self):
		""" Method that returns a char's object position in pixels """
		self.x = self.pos_x * sprite_size
		self.y = self.pos_y * sprite_size
		return (self.x, self.y)

	def display_char(self):
		""" Method that displays a character """
		self.window.blit(self.char_img, self.position_char())
		
	def move(self, direction):
		""" Method that move the position of a char """
		if direction == "right":
			if ((self.pos_x < nb_sprite - 1) and (self.labyrinth.structure[self.pos_y][self.pos_x + 1] != "w")):
				self.pos_x += 1
		elif direction == "left":
			if ((self.pos_x > 0) and (self.labyrinth.structure[self.pos_y][self.pos_x -1] != "w")):
				self.pos_x -= 1
		elif direction == "up":
			if ((self.pos_y > 0) and (self.labyrinth.structure[self.pos_y - 1][self.pos_x] != "w")):
				self.pos_y -= 1
		elif direction == "down":
			if ((self.pos_y < nb_sprite - 1) and (self.labyrinth.structure[self.pos_y + 1][self.pos_x] != "w")):
				self.pos_y += 1

class Objs:
	""" Class that create object Objs that will allow to create objects that the hero needs to pick up in the game """

	def __init__(self, name, img, position, window):
		self.name = name
		self.img = img
		self.position = position
		self.window = window

	def display_obj(self):
		self.window.blit(self.img, self.position)
