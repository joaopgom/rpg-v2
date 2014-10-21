# -*- encoding: utf-8 -*-

import global_data
from position import Position
class Camera(Position):
    def __init__(self):
        Position.__init__(self)

    def move_camera(self, x, y, map_width, map_height):
        if x > 0 and self.x < 0 or x < 0 and (global_data.screen_width - (map_width*32)) < self.x:
            return True
        elif y > 0 and self.y < 0 or y < 0 and (global_data.screen_height - (map_height*32)) < self.y:
            return True
        return False

    def set_camera(self, x, y):
        self.set_position(self.x+x, self.y+y)

    def get_camera(self):
        return self.get_position()
