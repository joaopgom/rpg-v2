# -*- encoding: utf-8 -*-
from pygame import image


class Image():
    def __init__(self):
        self.textures = dict()
    
    #carrega a imagem e adiciona o arquivo e o surface em textures
    def load_texture(self, texture_name, file_location, color_key=None):
        image_file = image.load(file_location).convert_alpha()
        self.textures[texture_name] = [image_file, image_file.get_rect()]