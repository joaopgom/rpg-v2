# -*- encoding: utf-8 -*-


class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def get_position(self):
        return self.x, self.y
    
    def set_position(self, x, y):
        self.x = x
        self.y = y 