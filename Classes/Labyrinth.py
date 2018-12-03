#! /usr/bin/env python3
# coding: utf-8

""" Module that define the class Labyrinth """

from init import *

class Labyrinth:
	""" Class that create the structure of the boardgame form a file and allows to display with pygame """

	def __init__(self, file, wall_img, floor_img, goal_img, bg_img):
		""" Method that initialize a Labyrinth object """
		self.file = file
		self.wall_img = wall_img
		self.floor_img = floor_img
		self.goal_img = goal_img
		self.bg_img = bg_img
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
				elif sprite == "b":
					window.blit(self.bg_img, (x,y))
				n_sprite += 1
			n_row += 1

	def get_strucpos(self, char):
		""" Method to return the coord(s) of the matching character in the structure """
		strucpos = []
		n_row = 0
		for row in self.structure:
			n_sprite = 0
			for sprite in row:
				x = n_sprite * sprite_size
				y = n_row * sprite_size
				if sprite == char:
					strucpos.append((x,y))
				n_sprite += 1
			n_row += 1
		if len(strucpos) == 1:
			return strucpos[0]
		else:
			 return strucpos
