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

class Char:
	""" Class that create character for the game """

	def __init__(self, name, labyrinth, window):
		self.name = name
		self.labyrinth = labyrinth
		self.struc_x = 0
		self.struc_y = 14
		self.life = 100
		self.objects = [1,2]
		self.direction = "right"
		self.window = window

	def position_char(self):
		""" Method that returns a char's object position in pixels """
		self.x = self.struc_x * sprite_size
		self.y = self.struc_y * sprite_size
		return (self.x, self.y)

	def display_char(self):
		""" Method that displays a character """
		
		if self.name == "hero":
			hero_img = pygame.image.load(picture_hero).convert_alpha()
			hero_img = pygame.transform.scale(hero_img, (sprite_size, sprite_size))
			position = self.position_char()
			self.window.blit(hero_img, position)
		elif self.name == "guard":
			guard_img = pygame.image.load(picture_guard).convert_alpha()
			guard_img = pygame.transform.scale(guard_img, (sprite_size, sprite_size))
			self.struc_x = 13
			self.struc_y = 0
			position = self.position_char()
			self.window.blit(guard_img, position)

	def move(self, direction):
		""" Method that move the position of a char """
		if direction == "right":
			if ((self.struc_x < nb_sprite - 1) and (self.labyrinth.structure[self.struc_y][self.struc_x + 1] != "w")):
				self.struc_x += 1
		elif direction == "left":
			if ((self.struc_x > 0) and (self.labyrinth.structure[self.struc_y][self.struc_x -1] != "w")):
				self.struc_x -= 1
		elif direction == "up":
			if ((self.struc_y > 0) and (self.labyrinth.structure[self.struc_y - 1][self.struc_x] != "w")):
				self.struc_y -= 1
		elif direction == "down":
			if ((self.struc_y < nb_sprite - 1) and (self.labyrinth.structure[self.struc_y + 1][self.struc_x] != "w")):
				self.struc_y += 1
