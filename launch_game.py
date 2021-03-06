#! /usr/bin/env python3
# coding: utf-8

""" Main program to launch the game: Help MacGyver to escape !"""

import random
import pygame
from pygame.locals import *

from init import *
import Classes
from Classes.Labyrinth import Labyrinth
from Classes.Characters import Characters
from Classes.Game_objects import Game_objects

# Funtions

def load_img(img, ratio):
    """ function that load and scale an image with Pygame """

    name = pygame.image.load(img).convert_alpha()
    name = pygame.transform.scale(name, (ratio, ratio))
    return name

# Main

def main():
    pygame.init()

    window = pygame.display.set_mode((window_size, window_size))
    pygame.display.set_caption(window_title)
    
    # Loading images with pygame
    wall_img = load_img(picture_wall, sprite_size)
    floor_img = load_img(picture_empty, sprite_size)
    goal_img = load_img(picture_goal, sprite_size)
    needle_img = load_img(picture_needle, sprite_size)
    ether_img = load_img(picture_ether, sprite_size)
    plastic_img = load_img(picture_plastic, sprite_size)
    hero_img = load_img(picture_hero, sprite_size)
    hero2_img = load_img(picture_hero, int(sprite_size/1.5))
    guard_img = load_img(picture_guard, sprite_size)
    guard2_img = load_img(picture_guard, int(sprite_size/1.5))
    bg_img = load_img(picture_bg, sprite_size)
    seringe_img = load_img(picture_seringe, sprite_size)
    life100_img = load_img(picture_life100, int(sprite_size/1.5))
    life0_img = load_img(picture_life0, int(sprite_size/1.5))
    gameover_img = load_img(picture_gameover, 15 * sprite_size)
    finish_img = load_img(picture_finish, 15 * sprite_size)

    # Creating labyrinth
    labyrinth = Labyrinth("level.txt", wall_img, floor_img, goal_img, bg_img)
    labyrinth.generate()

    # Creating characters
    hero = Characters("hero", hero_img, labyrinth, window,1,15)
    guard = Characters("guard", guard_img, labyrinth, window, 14, 1)

    # get available position in structure
    available_pos = labyrinth.get_strucpos("e")
    available_pos.remove(guard.position_char())

    # get 3 random position for objs
    needle_pos = random.choice(available_pos)
    available_pos.remove(needle_pos)
    ether_pos = random.choice(available_pos)
    available_pos.remove(ether_pos)
    plastic_pos = random.choice(available_pos)

    # Creating Objects
    needle = Game_objects("needle", needle_img, needle_pos, window)
    ether = Game_objects("ether", ether_img, ether_pos, window)
    plastic = Game_objects("plastic", plastic_img, plastic_pos, window)

    # Display game
    labyrinth.display_lab(window)
    window.blit(hero2_img, (0,0))
    window.blit(life100_img, (1* sprite_size, 0))
    window.blit(guard2_img, (3 * sprite_size,0))
    window.blit(life0_img, (4 * sprite_size, 0))
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
        window.blit(hero2_img, (0,0))
        window.blit(guard2_img, (3 * sprite_size,0))

        if plastic in hero.objects and needle in hero.objects and ether in hero.objects:
            window.blit(seringe_img, (0, 2 * sprite_size))
            if hero.position_char() == labyrinth.get_strucpos("a"):
                window.blit(finish_img, (1 * sprite_size, 1 * sprite_size))
        if hero.life != 0:
            hero.display_char()
            window.blit(life100_img, (1 * sprite_size, 0))
        else: 
            window.blit(life0_img, (1 * sprite_size, 0))
            window.blit(gameover_img, (1 * sprite_size, 1 * sprite_size))
        if guard.life != 0:
            guard.display_char()
            window.blit(life100_img, (4 * sprite_size, 0))
        else:
            window.blit(life0_img, (4 * sprite_size, 0))
        if hero.position_char() == guard.position_char():
            if plastic in hero.objects and needle in hero.objects and ether in hero.objects:
                guard.life = 0
            else:
                hero.life = 0 
        if hero.position_char() == needle.position:
            hero.objects.append(needle)
        if needle in hero.objects:
            needle.position = (0, 4 * sprite_size)
        needle.display_obj()
        if hero.position_char() == ether.position:
            hero.objects.append(ether)
        if ether in hero.objects:
            ether.position = (0, 5 * sprite_size)
        ether.display_obj()
        if hero.position_char() == plastic.position:
            hero.objects.append(plastic)
        if plastic in hero.objects:
            plastic.position = (0, 6 * sprite_size)
        plastic.display_obj()
        pygame.display.flip()

if __name__ == "__main__":
    main()