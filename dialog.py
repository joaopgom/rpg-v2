import time
from pygame.locals import K_RETURN
from global_data import *


DIALOGUES = {}


def dialog(player, map, other_position, conversation):
    """

    :param player: is the main player that will be drawed on map
    :param map: the current map
    :param other_position:
    :param conversation: conversation that have to be loaded
    :return: void
    """
    font_file = u'/usr/share/fonts/truetype/ttf-khmeros-core/KhmerOS.ttf'
    font_render = pygame.font.Font(font_file, 14)
    dialog_count = 0
    while True:
        """open box dialog, create dialog box, close box pass """
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[K_RETURN]:
                    if dialog_count >= len(DIALOGUES[conversation]):
                        return
                    speech = DIALOGUES[conversation][dialog_count]

                    speech_ = font_render.render(speech[0]+': '+speech[1], True, pygame.Color(255, 255, 255))

                    width = speech_.get_width()+30
                    height = speech_.get_height()+30
                    border_top = screen_height-height-30
                    border_left = (screen_width/2)-(width/2)                    
                    rect = pygame.Rect(border_left, border_top, width, height)
                    
                    map.draw_map()
                    player.draw()
                    pygame.draw.rect(screen, pygame.Color(200, 200, 200), rect, 2)
                    
                    rect = pygame.Rect(border_left+2, border_top+2, width-4, height-4)
                    pygame.draw.rect(screen, pygame.Color(10, 10, 211), rect)
                    screen.blit(speech_, (border_left+15, border_top+15))
                    dialog_count += 1
                    pygame.display.update()
                    pygame.time.Clock().tick(30)
                    time.sleep(1)


def load_dialog(file_name):
    """

    :param file_name: conversation's file name
    """
    dialog = open(u'data/conversation/%s.conv' % file_name, 'r')
    DIALOGUES[file_name] = []
    for speech in dialog:
        speech_data = speech.split(';')
        DIALOGUES[file_name].append(speech_data)
