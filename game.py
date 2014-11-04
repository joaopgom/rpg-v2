# -*- encoding: utf-8 -*-

import sys
import pygame
import global_data
import dialog
from pygame import event, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_RETURN
from map import Map
from player import Player

class Game:
    def __init__(self):
        self.screen = global_data.screen        
        self.map = Map('WORLD_MAP')
        #self.current_map = 'WORLD_MAP'
        self.maps = {}
        self.maps[self.map.name] = self.map
        self.player = Player('L')
        self.player.move(100, 100)
        self.walk_speed = 3
        self.clock = pygame.time.Clock()
        self.last_input = None
    
    def check_map_width(self, x):
        if x >= len(self.map.map_tiles):
            return len(self.map.map_tiles)-1
        elif x < 0:
            return 0
        return x
    
    def check_map_height(self, y):
        if y >= len(self.map.map_tiles[0]):
            return len(self.map.map_tiles[0])-1
        elif y < 0:
            return 0
        return y
    
    def key_return(self):
        x_, y_ = 0, 0
        if self.last_input[K_LEFT]:
            x_ = self.check_map_width((self.map.camera.x*(-1)+self.player.x)/32) 
            y_ = self.check_map_height((self.map.camera.y*(-1)+self.player.y+42)/32)                
        elif self.last_input[K_RIGHT]:
            x_ = self.check_map_width((self.map.camera.x*(-1)+self.player.x+24)/32)
            y_ = self.check_map_height((self.map.camera.y*(-1)+self.player.y+42)/32)
        elif self.last_input[K_UP]:
            x_ = self.check_map_width((self.map.camera.x*(-1) + self.player.x+16)/32)
            y_ = self.check_map_height((self.map.camera.y*(-1) + self.player.y+16*(1))/32)
        elif self.last_input[K_DOWN]:
            x_ = self.check_map_width((self.map.camera.x*(-1) + self.player.x+16)/32)
            y_ = self.check_map_height((self.map.camera.y*(-1) + self.player.y+48)/32)
        if self.map.map_tiles[x_][y_].object is not None and self.map.map_tiles[x_][y_].object.type == 'NPC':
            if self.map.map_tiles[x_][y_].object.has_dialog:
                file_name = u'%s_%s'%(self.player.name, self.map.map_tiles[x_][y_].object.name)
                if file_name.upper() not in dialog.DIALOGUES:
                    dialog.load_dialog(file_name.upper())
                dialog.dialog(self.player, self.map, self.map.map_tiles[x_][y_].object.get_position(), file_name)
    
    def move_left(self, x_, y_):
        if self.map.map_tiles[x_][y_].can_walk:
            if not self.map.move(self.walk_speed, 0):
                if not (self.player.x + self.walk_speed*(-1)) < 0:
                    self.player.move(self.walk_speed*(-1), 0)
        self.player.change_sprite(self.walk_speed*(-1), 0)
    
    def move_right(self, x_, y_):
        if self.map.map_tiles[x_][y_].can_walk:
            if not self.map.move(self.walk_speed*(-1), 0):
                if not (self.player.x + self.walk_speed) > global_data.screen_width - (self.player.image.get_width()/4):
                    self.player.move(self.walk_speed, 0)
        self.player.change_sprite(self.walk_speed, 0)

    def move_up(self, x_, y_):
        if self.map.map_tiles[x_][y_].can_walk:
            if not self.map.move(0, self.walk_speed):
                if not (self.player.y + self.walk_speed*(-1)) < 0:
                    self.player.move(0, self.walk_speed*(-1))
        elif self.map.map_tiles[x_][y_].object is not None:# and self.map.map_tiles[x_][y_].object.type == 'PORTAL':
            self.object_map_collider(self.map.map_tiles[x_][y_].object, x_, y_)
        self.player.change_sprite(0, self.walk_speed*(-1))

    def move_down(self, x_, y_):
        if self.map.map_tiles[x_][y_].can_walk:
            if not self.map.move(0, self.walk_speed*(-1)):
                if not (self.player.y + self.walk_speed) > global_data.screen_height - (self.player.image.get_height()/4):
                    self.player.move(0, self.walk_speed)
        self.player.change_sprite(0, self.walk_speed)

    def object_map_collider(self, object, X_, Y_):
        if object.type == 'PORTAL':
            if not self.map.map_tiles[x_][y_].object.name in self.maps:
                self.maps[self.map.map_tiles[x_][y_].object.name] = Map(self.map.map_tiles[x_][y_].object.name) 
            self.map = self.maps[self.map.map_tiles[x_][y_].object.name]

    """ Recebe o input do jogador e realiza a ação de acordo com a tecla pressionada """
    def player_input(self, key_pressed):
        """
        calcula qual será a posição futura do personagem em relação ao mapa geral usando a posição da 
        camera em relação ao mapa e do personagem e do personagem em relação a camera
        """
        #x_, y_ = (self.map.camera.x*(-1)+self.player.x)/32, (self.map.camera.y*(-1)+self.player.y)/32
         
        if key_pressed[K_RETURN]:
            self.key_return()
        
        elif key_pressed[K_LEFT]:
            x_ = self.check_map_width((self.map.camera.x*(-1)+self.player.x)/32) 
            y_ = self.check_map_height((self.map.camera.y*(-1)+self.player.y+42)/32)
            self.move_left(x_, y_)

        elif key_pressed[K_RIGHT]:
            x_ = self.check_map_width((self.map.camera.x*(-1)+self.player.x+24)/32)
            y_ = self.check_map_height((self.map.camera.y*(-1)+self.player.y+42)/32)
            self.move_right(x_, y_)

        elif key_pressed[K_UP]:
            x_ = self.check_map_width((self.map.camera.x*(-1) + self.player.x+16)/32)
            y_ = self.check_map_height((self.map.camera.y*(-1) + self.player.y+16*(1))/32)
            self.move_up(x_, y_)

        elif key_pressed[K_DOWN]:
            x_ = self.check_map_width((self.map.camera.x*(-1) + self.player.x+16)/32)
            y_ = self.check_map_height((self.map.camera.y*(-1) + self.player.y+48)/32)
            self.move_down(x_, y_)
            
        self.last_input = key_pressed

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