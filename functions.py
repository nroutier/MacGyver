#! /usr/bin/env python3
# coding: utf-8

""" Module that contains functions used for the game MacGyver """

import pygame
from pygame.locals import *

from init import *

def load_img(img):
    """ function that load and scale an image with Pygame """

    name = pygame.image.load(img).convert_alpha()
    name = pygame.transform.scale(name, (sprite_size, sprite_size))
    return name