# -*- encoding: utf-8 -*-

import sys
import pygame
import global_data
from pygame import event
from map import Map

class Game:
    def __init__(self):
        self.screen = global_data.screen        
        self.map = Map('WORLD_MAP')

    def main_loop(self):
        while True:
            for ev in event.get():
                if ev.type == pygame.QUIT:            
                    pygame.quit()
                    sys.exit()

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.main_loop()