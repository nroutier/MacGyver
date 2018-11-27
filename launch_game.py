#! /usr/bin/env python3
# coding: utf-8

""" Main program to launch the game: Help MacGyver to escape !"""

import pygame
from pygame.locals import *

from init import *
from classes import *

def main():
    pygame.init()

    window = pygame.display.set_mode((window_size, window_size))
    pygame.display.set_caption(window_title)

    labyrinth = Labyrinth("level.txt")
    labyrinth.generate()
    labyrinth.display_lab(window)
    pygame.display.flip()

    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0

if __name__ == "__main__":
    main()