# -*- encoding: utf-8 -*-

import pygame
import global_data
from camera import Camera
from position import Position

MAP_LIST = dict(WORLD_MAP=[True, 50, 30, 30], MIDGARD=[False, 0, 30, 30], HOUSE=[False, 0, 19, 25], WORLD_MAP_BATTLE=[False, 0, 19, 25])


class MapTile:
    def __init__(self):
        self.name = ''
        self.can_walk = False
        self.position = [0, 0]
        self.image = None
        self.rect = None
        self.object = None

    def draw_piece(self, camera):
        global_data.screen.blit(global_data.texture_manager.textures[self.name][0],
                                (int(self.position[0]) + camera.get_position()[0],
                                 camera.get_position()[1] + int(self.position[1])),
                                self.rect)
        if self.object is not None:
            global_data.screen.blit(self.object.image[0], (
                self.position[0] + camera.get_position()[0], camera.get_position()[1] + self.position[1]), self.object.rect)
            """
            global_data.screen.blit(global_data.texture_manager.textures[self.name][0], \
                                (int(self.position[0]) + camera.get_position()[0], camera.get_position()[1] + int(self.position[1])), \
                                pygame.Rect(100, 1000, 32, 32))
            """


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

        self.map_tiles = [[MapTile() for i in range(self.map_pieces_length[0])] for j in
                          range(self.map_pieces_length[1])]
        self.load_map()

    def load_map(self):
        map_data = open('data/maps/' + self.name + '.map', 'r')
        for y in range(self.map_pieces_length[0]):
            for x in range(self.map_pieces_length[1]):
                data = map_data.readline().replace('\n', '').split(';')

                self.map_tiles[x][y].name = data[0]
                self.map_tiles[x][y].can_walk = True if data[1] == 'True' else False
                self.map_tiles[x][y].image_position = (int(data[2]), int(data[3]))
                if self.name not in global_data.texture_manager.textures:
                    global_data.texture_manager.load_texture(self.map_tiles[x][y].name, 'images/' + data[6], -1)
                self.map_tiles[x][y].image = global_data.texture_manager.textures[self.map_tiles[x][y].name]
                self.map_tiles[x][y].position = (int(data[5]), int(data[4]))
                self.map_tiles[x][y].rect = pygame.Rect(int(data[2]), int(data[3]), 32, 32)
                self.map_tiles[x][y].object = None
                if data[7] != '' and data[8] != '' and data[9] != '' and data[10] != '':  # and data[11] != '':
                    self.map_tiles[x][y].object = ObjectMap()
                    self.map_tiles[x][y].object.set_position(int(data[5]), int(data[4]))
                    self.map_tiles[x][y].object.name = data[10]
                    self.map_tiles[x][y].object.type = data[11]
                    self.map_tiles[x][y].object.has_dialog = True if data[12] == 'True' else False
                    if data[9] not in global_data.texture_manager.textures:
                        global_data.texture_manager.load_texture(data[9], 'images/' + data[9], -1)
                    self.map_tiles[x][y].object.image = global_data.texture_manager.textures[data[9]]
                    self.map_tiles[x][y].object.rect = pygame.Rect(int(data[7]), int(data[8]), 32, 32)
                else:
                    self.map_tiles[x][y].object = None
        map_data.close()

    def draw_map(self):
        for x in range(self.map_pieces_length[0]):
            for y in range(self.map_pieces_length[1]):
                self.map_tiles[y][x].draw_piece(self.camera)

    def move(self, x, y):
        if self.camera.move_camera(x, y, self.map_pieces_length[0], self.map_pieces_length[1]):
            self.camera.set_camera(x, y)
            return True
        return False


class ObjectMap(Position):
    def __init__(self):
        Position.__init__(self)
        self.rect = None
        self.image = None
        self.name = None
        self.type = None
        self.has_dialog = False
