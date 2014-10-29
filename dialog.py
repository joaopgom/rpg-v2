import pygame
from global_data import *

DIALOGUES = {}

def dialog(width, height, npc, text):
    #if npc.has_dialog or npg.current_dialog >= len(npc.dialogues):
    #    return None
    
    text_surfs = []
    
    rect = pygame.Rect(85, 92, 165, 44)
    #@screen.blit(pygame.image.load('/home/john/workspace/rpg-v2/images/grass.gif').convert_alpha(), (0, 0), rect)
    pygame.draw.rect(screen, pygame.Color(10,10,211), rect, 2)
    rect = pygame.Rect(87, 94, 161, 40)
    #pygame.draw.rect(screen, pygame.Color(180,180,180), rect)
    s = pygame.Surface((161, 40))
    s.set_alpha(128)
    s.fill((180, 180, 180))
    screen.blit(s, (87, 94))
    
    for text_line in text:
        t = pygame.font.Font(u'/usr/share/fonts/truetype/ttf-khmeros-core/KhmerOS.ttf', 14).render(text_line, True, pygame.Color(0, 0, 0)) 
        text_surfs.append(t)
        #print t.get_width()
        
    for s in text_surfs:
        screen.blit(s, (100, 100))
        
def load_dialog(file_name):
    dialog = open(u'data/conversation/%s.conv'%(file_name), 'r')
    for speech in dialog:
        print speech.split(';')
    pass