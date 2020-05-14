from Main_Script import Const
from Main_Script import message_to_screen
from Main_Script import images
from Main_Script import player
from pygame.locals import *
import Action_Script
import Menu_Script
import pygame
import random
import time

def walk(img1, img2, img3):
    if 1 >= Const.sec <= 3:
        display(img1)
    elif 4 >= Const.sec <= 6:
        display(img1)
    elif 7 >= Const.sec <= 9:
        display(img2)
    elif 10 >= Const.sec <= 12:
        display(img3)
    if Const.sec <= 9:                                  
        Const.sec += 1
    elif Const.sec > 9:
        Const.sec = 1
    time.sleep(0.01)
                
def display(img):
    Const.gameDisplay.blit(images.background, [0, 0])
    Const.gameDisplay.blit(img, [Const.lead_x,Const.lead_y])
    pygame.display.update()
def gameLoop():
    gameExit = False
    Const.gameDisplay.fill(Const.white)
    pygame.display.update
    while not gameExit:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    Const.lead_x_change=-Const.size
                    Const.lead_y_change=0
                    Const.pos = 3

                elif event.key==pygame.K_RIGHT:
                    Const.lead_x_change=Const.size
                    Const.lead_y_change=0
                    Const.pos = 2
    
                elif event.key==pygame.K_UP:
                    Const.lead_y_change=-Const.size
                    Const.lead_x_change=0
                    Const.pos = 4
                elif event.key==pygame.K_DOWN:
                    Const.lead_y_change=Const.size
                    Const.lead_x_change=0
                    Const.pos = 1
                    
                elif event.key==pygame.K_SPACE:
                    Menu_Script.game_menu()
                    
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    Const.lead_x_change=0
                    
                elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    Const.lead_y_change=0
    

        if Const.lead_x + Const.lead_x_change > -Const.size and Const.lead_x + Const.lead_x_change < (Const.width-33):
            Const.lead_x+=Const.lead_x_change
            
        if Const.lead_y + Const.lead_y_change > 46 and Const.lead_y + Const.lead_y_change < (Const.height-193):
            Const.lead_y+=Const.lead_y_change

        if Const.pos == 1:
            if Const.lead_y_change == 0:
                display(images.main1)
                
            else:
                walk(images.main2, images.main1, images.main3)
                
        elif Const.pos == 2:
            if Const.lead_x_change == 0:
                display(images.right1)
                
            else:
                walk(images.right2, images.right1, images.right3)
                
        elif Const.pos == 3:
            if Const.lead_x_change == 0:
                display(images.left1)
                
            else:
                walk(images.left2, images.left1, images.left3)
                
        elif Const.pos == 4:
            if Const.lead_y_change == 0:
                display(images.back1)
                
            else:
                walk(images.back2, images.back1, images.back3)
                
            
        if Const.lead_x_change != 0 or Const.lead_y_change != 0:
            if random.randrange(0, 200, 1) == 4:
                Const.lead_x_change = 0
                Const.lead_y_change = 0
                Const.Exit = 0
                Action_Script.action()
                
        Const.clock.tick(Const.FPS)









