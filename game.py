# -*- encoding: utf-8 -*-

import sys
import pygame
import global_data
from pygame import event, K_LEFT, K_RIGHT, K_UP, K_DOWN
from map import Map
from player import Player

class Game:
    def __init__(self):
        self.screen = global_data.screen        
        self.map = Map('WORLD_MAP')
        self.player = Player('L')
        self.walk_speed = 3
        
    def player_input(self, key_pressed):
        if key_pressed[K_LEFT]:
            if not self.map.move(self.walk_speed, 0):
                self.player.move(self.walk_speed*(-1), 0)
            self.player.change_sprite(self.walk_speed*(-1), 0)
        elif key_pressed[K_RIGHT]:
            if not self.map.move(self.walk_speed*(-1), 0):
                self.player.move(self.walk_speed, 0)
            self.player.change_sprite(self.walk_speed, 0)
        elif key_pressed[K_UP]:
            if not self.map.move(0, self.walk_speed):
                self.player.move(0, self.walk_speed*(-1))
            self.player.change_sprite(0, self.walk_speed*(-1))
        elif key_pressed[K_DOWN]:
            if not self.map.move(0, self.walk_speed*(-1)):
                self.player.move(0, self.walk_speed)
            self.player.change_sprite(0, self.walk_speed)

    def main_loop(self):
        while True:
            for ev in event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif ev.type == pygame.KEYDOWN:
                    self.player_input(pygame.key.get_pressed())
                self.map.draw_map()
                self.player.draw()
                pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    pygame.key.set_repeat(1, 10)
    game = Game()
    game.main_loop()