# -*- encoding: utf-8 -*-

import pygame
import image


def create_screen(width, height):
    _screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Game :)')
    _screen.fill((255, 255, 255))
    return _screen

screen_width = 800
screen_height = 608

#tela que é exibida
screen = create_screen(screen_width, screen_height)

#todas as texturas são carregadas e armazenadas no texture_manager
texture_manager = image.Image()