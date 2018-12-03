#! /usr/bin/env python3
# coding: utf-8

""" Module that define the class Game_objects """

class Game_objects:
	""" Class that create object Objs that will allow to create objects that the hero needs to pick up in the game """

	def __init__(self, name, img, position, window):
		self.name = name
		self.img = img
		self.position = position
		self.window = window

	def display_obj(self):
		self.window.blit(self.img, self.position)