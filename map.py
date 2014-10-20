# -*- encoding: utf-8 -*-
import pygame
import global_data
from pygame import Rect
from camera import Camera


MAP_LIST = {'WORLD_MAP':[True, 50, 30, 30],
             'MIDGARD':[False, 0, 30, 30]            
            }



class MapTile:
    def __init__(self):
        self.name = ''
        self.can_walk = False
        self.position = [0, 0]
        self.image = None
        self.rect = None
        self.object = None
        
    def draw_piece(self, camera):
        global_data.screen.blit(global_data.texture_manager.textures[self.name][0], \
                                (int(self.position[0]) + camera.get_position()[0], camera.get_position()[1] + int(self.position[1])), \
                                self.rect)

class Map:
    def __init__(self, name):
        self.name = name
        self.current_piece = None
        self.has_enemy = MAP_LIST[self.name][0]
        self.enemy_freq = MAP_LIST[self.name][1]        
        self.camera = Camera()
        self.map_pieces = None
        self.map_pieces_length = [int(MAP_LIST[self.name][2]), 
                                  int(MAP_LIST[self.name][3])]
        self.map_tiles = [[MapTile() for i in range(self.map_pieces_length[0])] for j in range(self.map_pieces_length[1])]
        self.load_map()
        
    def load_map(self):
        map_data = open('data/maps/'+self.name+'.map', 'r')
        for x in range(self.map_pieces_length[0]):
            for y in range(self.map_pieces_length[1]):
                data = map_data.readline().replace('\n', '').split(';')
                self.map_tiles[x][y].name = data[0]
                self.map_tiles[x][y].can_walk = data[1]
                self.map_tiles[x][y].image_position = (data[2], data[3])
                if self.name not in global_data.texture_manager.textures:
                    global_data.texture_manager.load_texture(self.map_tiles[x][y].name, 'images/'+data[6],  -1)
                self.map_tiles[x][y].image = global_data.texture_manager.textures[self.map_tiles[x][y].name]
                self.map_tiles[x][y].position = (data[4], data[5])
                self.map_tiles[x][y].rect = pygame.Rect(int(data[2]), int(data[3]), 32, 32)
                self.map_tiles[x][y].object = None
        map_data.close()
        
    def draw_map(self):
        for x in range(self.map_pieces_length[0]):
            for y in range(self.map_pieces_length[1]):
                self.map_tiles[x][y].draw_piece(self.camera)
        
    def move(self, x, y):
        if self.camera.move_camera(x, y, self.map_pieces_length[0], self.map_pieces_length[1]):
            self.camera.set_camera(x, y)
            return True
        return False
                