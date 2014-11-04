import pygame
from global_data import *
from pygame.locals import K_RETURN

DIALOGUES = {}

def dialog(player, map, other_position, conversation):
    font_file = u'/usr/share/fonts/truetype/ttf-khmeros-core/KhmerOS.ttf'
    font_render = pygame.font.Font(font_file, 14)
    dialog_count = 0
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[K_RETURN]:
                    if dialog_count >= len(DIALOGUES[conversation]):
                        return
                    speech = DIALOGUES[conversation][dialog_count]
                    speech_ = font_render.render(speech[0]+': '+speech[1], True, pygame.Color(0, 0, 0))
                    width = speech_.get_width()+30
                    height = speech_.get_height()+30
                    border_top = screen_height-height-30
                    border_left = (screen_width/2)-(width/2)                    
                    rect = pygame.Rect(border_left, border_top, width, height)
                    
                    map.draw_map()
                    player.draw()
                    pygame.draw.rect(screen, pygame.Color(10, 10, 211), rect, 2)
                    
                    rect = pygame.Rect(border_left+2, border_top+2, width-4, height-4)
                    pygame.draw.rect(screen, pygame.Color(180, 180, 180, 128), rect)

                    dialog_count+=1
                    pygame.display.update()
                    pygame.time.Clock().tick(30)
                    
        
    
    """
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
    """ 
def load_dialog(file_name):
    dialog = open(u'data/conversation/%s.conv'%(file_name), 'r')
    DIALOGUES[file_name] = []
    for speech in dialog:
        speech_data = speech.split(';')
        DIALOGUES[file_name].append(speech_data)
