#! /usr/bin/env python3
# coding: utf-8

""" Main program to launch the game: Help MacGyver to escape !"""

import random
import pygame
from pygame.locals import *

from init import *
from classes import *

def load_img(img):
    """ function that load and scale an image with Pygame """

    name = pygame.image.load(img).convert_alpha()
    name = pygame.transform.scale(name, (sprite_size, sprite_size))
    return name

def main():
    pygame.init()

    window = pygame.display.set_mode((window_size, window_size))
    pygame.display.set_caption(window_title)
    
    # Loading images with pygame
    wall_img = load_img(picture_wall)
    floor_img = load_img(picture_empty)
    goal_img = load_img(picture_goal)
    needle_img = load_img(picture_needle)
    ether_img = load_img(picture_ether)
    plastic_img = load_img(picture_plastic)
    hero_img = load_img(picture_hero)
    guard_img = load_img(picture_guard) 

    # Creating labyrinth
    labyrinth = Labyrinth("level.txt", wall_img, floor_img, goal_img)
    labyrinth.generate()

    # Creating characters
    hero = Char("hero", hero_img, labyrinth, window,0,14)
    guard = Char("guard", guard_img, labyrinth, window, 13, 0)

    # get available position in structure
    available_pos = []
    n_row = 0
    for row in labyrinth.structure:
        n_sprite = 0
        for sprite in row:
            x = n_sprite * sprite_size
            y = n_row * sprite_size
            if ((sprite == "e") and ((x, y) != hero.position_char()) and ((x,y) != guard.position_char())):
                available_pos.append((x, y))
            n_sprite += 1
        n_row += 1

    # get 3 random position for objs
    random_pos1 = random.choice(available_pos)
    available_pos.remove(random_pos1)
    random_pos2 = random.choice(available_pos)
    available_pos.remove(random_pos2)
    random_pos3 = random.choice(available_pos)
    available_pos.remove(random_pos3)

    # Creating Objects
    needle = Objs("needle", needle_img, random_pos1, window)
    ether = Objs("ether", ether_img, random_pos2, window)
    plastic = Objs("plastic", plastic_img, random_pos3, window)

    # Display game
    labyrinth.display_lab(window)
    hero.display_char()
    guard.display_char()
    needle.display_obj()
    ether.display_obj()
    plastic.display_obj()

    pygame.display.flip()

    # Event loop
    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    loop = 0
                elif event.key == K_RIGHT:
                    hero.move("right")
                elif event.key == K_LEFT:
                    hero.move("left")
                elif event.key == K_UP:
                    hero.move("up")
                elif event.key == K_DOWN:
                    hero.move("down")
        
        labyrinth.display_lab(window)
        if hero.life != 0:
            hero.display_char()
        else: loop = 0
        if hero.position_char() == guard.position_char():
            if plastic in hero.objects and needle in hero.objects and ether in hero.objects:
                guard.life = 0
                print("You killed the guard")
            else:
                hero.life = 0
                print("The guard killed you")
        elif guard.life != 0:
            guard.display_char()
        if needle not in hero.objects:
            needle.display_obj()
        if hero.position_char() == needle.position:
            hero.objects.append(needle)
        if ether not in hero.objects:
            ether.display_obj()
        if hero.position_char() == ether.position:
            hero.objects.append(ether)
        if plastic not in hero.objects:
            plastic.display_obj()
        if hero.position_char() == plastic.position:
            hero.objects.append(plastic)
        pygame.display.flip()

if __name__ == "__main__":
    main()