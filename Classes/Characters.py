#! /usr/bin/env python3
# coding: utf-8

""" Module that define the class Characters """

from init import *

class Characters:
	""" Class that create character for the game """

	def __init__(self, name, char_img, labyrinth, window, pos_x, pos_y):
		self.name = name
		self.char_img = char_img
		self.labyrinth = labyrinth
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.life = 100
		self.objects = []
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
			if ((self.pos_x < nb_sprite - 1) and (self.labyrinth.structure[self.pos_y][self.pos_x + 1] != "w" and self.labyrinth.structure[self.pos_y][self.pos_x + 1] != "b")):
				self.pos_x += 1
		elif direction == "left":
			if ((self.pos_x > 1) and (self.labyrinth.structure[self.pos_y][self.pos_x -1] != "w" and self.labyrinth.structure[self.pos_y][self.pos_x -1] != "b")):
				self.pos_x -= 1
		elif direction == "up":
			if ((self.pos_y > 1) and (self.labyrinth.structure[self.pos_y - 1][self.pos_x] != "w" and self.labyrinth.structure[self.pos_y - 1][self.pos_x] != "b")):
				self.pos_y -= 1
		elif direction == "down":
			if ((self.pos_y < nb_sprite - 1) and (self.labyrinth.structure[self.pos_y + 1][self.pos_x] != "w" and self.labyrinth.structure[self.pos_y + 1][self.pos_x] != "b")):
				self.pos_y += 1