# -*- encoding: utf-8 -*-

import pygame
import image

def create_screen(width, height):
    _screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Game :)')
    _screen.fill((255, 255, 255))
    return _screen

def load_map_tiles():
    pass

def load_texture(texture_name):
    pass
screen_width = 800
screen_height = 608

screen = create_screen(screen_width, screen_height)
texture_manager = image.Image()