from Main_Script import Const
from Main_Script import images
from Main_Script import save
from Main_Script import message_to_screen
from Main_Script import player
import Event_Script
import pygame
import time
import random

def game_menu():
    state = 1
    pygame.display.update()
    Const.counter = 1
    while Const.counter == 1:
        if state == 1:
            Const.gameDisplay.blit(images.menu_resume, [-3, 36])
        elif state == 2:
            Const.gameDisplay.blit(images.menu_save, [-3, 36])
        elif state == 3:
            Const.gameDisplay.blit(images.menu_options, [-3, 36])
        elif state == 4:
            Const.gameDisplay.blit(images.menu_quit, [-3, 36])

        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    if state < 4:
                        state += 1
                    elif state == 4:
                        state = 1
                elif event.key==pygame.K_UP:
                    if state > 1:
                        state -= 1
                    elif state == 1:
                        state = 4
                elif event.key==pygame.K_v:
                    if state == 1:
                        Const.counter = 0
                    elif state == 2:
                        save()
                        time.sleep(1)
                        Const.counter = 0
                    elif state == 3:
                        pass
                    elif state == 4:
                        pygame.quit()
                        quit()
                elif event.key==pygame.K_SPACE:
                    Const.counter = 0
        pygame.display.update()
    
