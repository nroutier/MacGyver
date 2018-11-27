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

    hero = Char("hero", labyrinth, window)
    hero.display_char()

    guard = Char("guard", labyrinth, window)
    guard.display_char()

    pygame.display.flip()

    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = 0
                elif event.key == K_RIGHT:
                    hero.move("right")
                elif event.key == K_LEFT:
                    hero.move("left")
                elif event.key == K_UP:
                    hero.move("up")
                elif event.key == K_DOWN:
                    hero.move("down")
        labyrinth.display_lab(window)
        hero.display_char()
        guard.display_char()
        pygame.display.flip()

if __name__ == "__main__":
    main()