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
        self.player.move(100, 100)
        self.walk_speed = 3
        self.clock = pygame.time.Clock()
    
    """ Recebe o input do jogador e realiza a ação de acordo com a tecla pressionada """
    def player_input(self, key_pressed):
        #calcula qual será a posição futura do personagem no mapa
        x_, y_ = (self.map.camera.x*(-1)+self.player.x)/32, (self.map.camera.y*(-1)+self.player.y)/32
                
        if key_pressed[K_LEFT]:
            if self.map.map_tiles[x_-1][y_].can_walk:
                if not self.map.move(self.walk_speed, 0):
                    if not (self.player.x + self.walk_speed*(-1)) < 0:
                        self.player.move(self.walk_speed*(-1), 0)
            elif self.map.map_tiles[x_-1][y_].object is not None and self.map.map_tiles[x_-1][y_].object.type == 'PORTAL':
                print 'change map to: '+ self.map.map_tiles[x_][y_+1].object.name
            self.player.change_sprite(self.walk_speed*(-1), 0)
        elif key_pressed[K_RIGHT]:
            if self.map.map_tiles[x_+1][y_].can_walk:
                if not self.map.move(self.walk_speed*(-1), 0):
                    if not (self.player.x + self.walk_speed) > global_data.screen_width - (self.player.image.get_width()/4):
                        self.player.move(self.walk_speed, 0)
            elif self.map.map_tiles[x_+1][y_].object is not None and self.map.map_tiles[x_+1][y_].object.type == 'PORTAL':
                print 'change map to: '+ self.map.map_tiles[x_][y_+1].object.name
            self.player.change_sprite(self.walk_speed, 0)
        elif key_pressed[K_UP]:
            if self.map.map_tiles[x_][y_-1].can_walk:
                if not self.map.move(0, self.walk_speed):
                    if not (self.player.y + self.walk_speed*(-1)) < 0:
                        self.player.move(0, self.walk_speed*(-1))
            elif self.map.map_tiles[x_][y_-1].object is not None and self.map.map_tiles[x_][y_-1].object.type == 'PORTAL':
                print 'change map to: '+ self.map.map_tiles[x_][y_+1].object.name
            self.player.change_sprite(0, self.walk_speed*(-1))
        elif key_pressed[K_DOWN]:
            if self.map.map_tiles[x_][y_+1].can_walk:
                if not self.map.move(0, self.walk_speed*(-1)):
                    if not (self.player.y + self.walk_speed) > global_data.screen_height - (self.player.image.get_height()/4):
                        self.player.move(0, self.walk_speed)
            elif self.map.map_tiles[x_][y_+1].object is not None and self.map.map_tiles[x_][y_+1].object.type == 'PORTAL':
                print 'change map to: '+ self.map.map_tiles[x_][y_+1].object.name
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
            self.clock.tick(30)

if __name__ == '__main__':
    pygame.init()
    pygame.key.set_repeat(1, 10)
    game = Game()
    game.main_loop()