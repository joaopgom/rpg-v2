# -*- encoding: utf-8 -*-

import pygame
import global_data
from position import Position

CREATURES_LOADED = {'Cloud':{'hp': 50, 'mp': 20, 'level': 1, 'attack': 100, 'attack_m': 30, '_def': 80, 'def_m': 40, '_class': 'WARRIOR'},
                    'L':{'hp': 50, 'mp': 20, 'level': 1, 'attack': 100, 'attack_m': 30, '_def': 80, 'def_m': 40, '_class': 'WARRIOR'}}

def load_creature(name):
    pass

class Creature(Position):
    def __init__(self, name):
        Position.__init__(self)
        self.name = name
        load_creature(self.name)
        self.hp = CREATURES_LOADED[self.name]['hp']
        self.mp = CREATURES_LOADED[self.name]['mp']
        self.level = CREATURES_LOADED[self.name]['level']
        self.attack = CREATURES_LOADED[self.name]['attack']
        self.attack_m = CREATURES_LOADED[self.name]['attack_m']
        self._class = CREATURES_LOADED[self.name]['_class']
        self._def = CREATURES_LOADED[self.name]['_def']
        self.def_m = CREATURES_LOADED[self.name]['def_m']
        self.selfie = None

class Player(Creature):
    def __init__(self, name):
        Creature.__init__(self, name)
        self.weapon = None
        self.armor = None
        self.legs = None
        self.rings = None
        self.armlet = None
        self.items = []
        self.in_battle = False
        global_data.texture_manager.load_texture(self.name, 'images/character/%s/%s.png'%(self.name.upper(), self.name.upper()), -1)
        self.image = global_data.texture_manager.textures[self.name][0]
        self.sprites = [[None for x in range(4)] for y in range(4)]
        self.direction = [0, 0]
        self.load_sprites()

    def draw(self):
        global_data.screen.blit(self.image, self.get_position(), self.sprites[self.direction[0]][self.direction[1]])

    def load_sprites(self):
        for x in range(4):
            for y in range(4):
                self.sprites[x][y] = pygame.Rect((self.image.get_width()/4)*y, 
                                                 (self.image.get_height()/4)*x, 
                                                 self.image.get_width()/4,
                                                 self.image.get_height()/4)

    def change_sprite(self, x, y):
        if x > 0 and y == 0:
            self.direction[0] = 2
        elif x < 0 and y == 0:
            self.direction[0] = 1
        elif x == 0 and y > 0:
            self.direction[0] = 0
        elif x == 0 and y < 0:
            self.direction[0] = 3
        if x != 0 or y != 0:
            self.direction[1] = self.direction[1]+1 if self.direction[1] < 3 else 0

    def move(self, x, y):        
        self.set_position(self.x+x, self.y+y)
        
