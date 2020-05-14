from Main_Script import Const
from Main_Script import message_to_screen
from Main_Script import images
from Main_Script import player
from Main_Script import load
from Main_Script import cutscenes
from Main_Script import classes
from pygame.locals import *
import Action_Script
import Menu_Script
import pygame
import random
import time

def title_menu():
    counter = 1
    while counter == 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            mouse = pygame.mouse.get_pos()
            if (200+Const.shapeW) > mouse[0] > Const.shapeW and 149 > mouse[1] > 50:
                pygame.draw.rect(Const.gameDisplay, Const.light_grey, [Const.shapeW, 50, 200, 99])
                message_to_screen("START", Const.black, [Const.shapeW+40, 80], 50)
                pygame.display.update(Const.shapeW+40, 80, 25, 50)
                if event.type==MOUSEBUTTONDOWN:
                    pygame.draw.rect(Const.gameDisplay, Const.grey, [Const.shapeW, 50, 200, 99])
                    message_to_screen("START", Const.black, [Const.shapeW+40, 80], 50)
                    pygame.display.update(Const.shapeW+40, 80, 25, 50)
                    time.sleep(0.1)
                    pygame.draw.rect(Const.gameDisplay, Const.light_grey, [Const.shapeW, 50, 200, 99])
                    message_to_screen("START", Const.black, [Const.shapeW+40, 80], 50)
                    pygame.display.update(Const.shapeW+40, 80, 25, 50)
                    time.sleep(0.1)
                    counter = 0
                    cutscenes()
            else:
                pygame.draw.rect(Const.gameDisplay, Const.white, [Const.shapeW, 50, 200, 99])
                message_to_screen("START", Const.black, [Const.shapeW+40, 80], 50)
                pygame.display.update(Const.shapeW+40, 80, 25, 50)
            mouse = pygame.mouse.get_pos()
            if (200+Const.shapeW) > mouse[0] > Const.shapeW and 273 > mouse[1] > 174:
                pygame.draw.rect(Const.gameDisplay, Const.light_grey, [Const.shapeW, 174, 200, 99])
                message_to_screen("QUIT", Const.black, [Const.shapeW+40, 204], 50)
                pygame.display.update(Const.shapeW+40, 204, 25, 50)
                if event.type==MOUSEBUTTONDOWN:
                    pygame.draw.rect(Const.gameDisplay, Const.grey, [Const.shapeW, 174, 200, 99])
                    message_to_screen("QUIT", Const.black, [Const.shapeW+40, 204], 50)
                    pygame.display.update(Const.shapeW+40, 204, 25, 50)
                    time.sleep(0.1)
                    pygame.draw.rect(Const.gameDisplay, Const.light_grey, [Const.shapeW, 174, 200, 99])
                    message_to_screen("QUIT", Const.black, [Const.shapeW+40, 204], 50)
                    pygame.display.update(Const.shapeW+40, 204, 25, 50)
                    time.sleep(0.1)
                    pygame.quit()
                    quit()
            else:
                pygame.draw.rect(Const.gameDisplay, Const.white, [Const.shapeW, 174, 200, 99])
                message_to_screen("QUIT", Const.black, [Const.shapeW+40, 204], 50)
                pygame.display.update(Const.shapeW+40, 204, 25, 50)
            mouse = pygame.mouse.get_pos()
            if (200+Const.shapeW) > mouse[0] > Const.shapeW and 397 > mouse[1] > 298:
                pygame.draw.rect(Const.gameDisplay, Const.light_grey, [Const.shapeW, 298, 200, 99])
                message_to_screen("LOAD", Const.black, [Const.shapeW+40, 327], 50)
                pygame.display.update(Const.shapeW+40, 327, 25, 50)
                if event.type==MOUSEBUTTONDOWN:
                    pygame.draw.rect(Const.gameDisplay, Const.grey, [Const.shapeW, 298, 200, 99])
                    message_to_screen("LOAD", Const.black, [Const.shapeW+40, 327], 50)
                    pygame.display.update(Const.shapeW+40, 327, 25, 50)
                    time.sleep(0.1)
                    pygame.draw.rect(Const.gameDisplay, Const.light_grey, [Const.shapeW, 298, 200, 99])
                    message_to_screen("LOAD", Const.black, [Const.shapeW+40, 327], 50)
                    pygame.display.update(Const.shapeW+40, 327, 25, 50)
                    time.sleep(0.1)
                    try:
                        Const.load = True
                        load()
                        gameLoop()
                    except:
                        pass
            else:
                pygame.draw.rect(Const.gameDisplay, Const.white, [Const.shapeW, 298, 200, 99])
                message_to_screen("LOAD", Const.black, [Const.shapeW+40, 327], 50)
                pygame.display.update(Const.shapeW+40, 327, 25, 50)
def health_bar():
    pygame.draw.rect(Const.gameDisplay, Const.green, [184, 12, (Const.percent3*((player.player_health)/(100*player.Level))), 12]) 
def text_box(msg):
    pygame.draw.rect(Const.gameDisplay, Const.black, [(Const.width/4)-100, Const.height/4, 550, 50])
    message_to_screen(msg, Const.white, [(Const.width/4)-100, Const.height/4], 50)
    pygame.display.update()
    Const.counter = False
    while Const.counter == False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                    Const.counter = True
                    break
"""def block(n1, n2):
    if Const.lead_x+n1-126>(Const.width/4)>Const.lead_x+n1-161:
        Const.lead_y_change = 0
    if Const.lead_y+n2-96>(Const.height/4)>Const.lead_y+n2-191:
        Const.lead_x_change = 0
def block_call():
    block(200, 0)
    block(-300, 200)
    block(300, -100)"""
def event_check(n1, n2):
        if (((Const.height/4)>Const.lead_y+n1 and Const.pos == 4)
        or ((Const.height/4)<Const.lead_y+n1 and Const.pos == 1)
        or ((Const.width/4)<Const.lead_x+n2 and Const.pos == 2)
        or ((Const.width/4)>Const.lead_x+n2 and Const.pos == 3)):
            Const.counter = True
        else:
            Const.counter = False
def call_event():
    if Const.pos == 1:
        display(images.main1, False)
    elif Const.pos == 2:
        display(images.right1, True)
    elif Const.pos == 3:
        display(images.left1, True)
    elif Const.pos == 4:
        display(images.back1, True)
    event_check(0, 200)
    if ((Const.height/4)+50>Const.lead_y>(Const.height/4)-50
    and (Const.width/4)+50>Const.lead_x+200>(Const.width/4)-50
    and Const.counter==True):
        if Const.quest1 == 1:
            text_box("Mogan Magic: please deliver this to Lord Sinbad")
            text_box("You have recieved the secret scroll!")
            Const.quest1 = 2
        elif Const.quest1 == 2:
            text_box("Did you do what I asked?")
        elif Const.quest1 == 3:
            text_box("You've done your task well my friend...")
    event_check(200, -300)
    if ((Const.height/4)+50>Const.lead_y+200>(Const.height/4)-50
    and (Const.width/4)+50>Const.lead_x-300>(Const.width/4)-50
    and Const.counter==True):
        if Const.quest1 == 1:
            text_box("Sinbad: In my day, we fought dragons!")
        elif Const.quest1 == 2:
            text_box("Sinbad: Oh! for me?")
            text_box("...")
            text_box("Sinbad: Thank you for this message")
            Const.quest1 = 3
        elif Const.quest1 == 3:
            text_box("Sinbad: How's it going?")
    event_check(-100, 300)
    if ((Const.height/4)+50>Const.lead_y-100>(Const.height/4)-50
    and (Const.width/4)+50>Const.lead_x+300>(Const.width/4)-50
    and Const.counter==True):
        text_box("Assassin: Be careful who you speak to...")
        if Const.quest1 == 3:
            text_box("Assassin: I've been hearing rumors...")
    Const.lead_x_change = 0
    Const.lead_y_change = 0
    Const.counter = False
def walk(img1, img2, img3, pos):
    if 1 >= Const.sec <= 3:
        display(img1, pos)
    elif 4 >= Const.sec <= 6:
        display(img1, pos)
    elif 7 >= Const.sec <= 9:
        display(img2, pos)
    elif 10 >= Const.sec <= 12:
        display(img3, pos)
    if Const.sec <= 9:                                  
        Const.sec += 1
    elif Const.sec > 9:
        Const.sec = 1
    time.sleep(0.01)
def display(img, pos):
    Const.gameDisplay.fill(Const.white)
    Const.gameDisplay.blit(images.background2, [Const.lead_x,Const.lead_y])
    if pos == False:
        Const.gameDisplay.blit(img, [Const.width/4, Const.height/4])
    Const.gameDisplay.blit(images.mage, [Const.lead_x+200,Const.lead_y])
    Const.gameDisplay.blit(images.wizard, [Const.lead_x-300,Const.lead_y+200])
    Const.gameDisplay.blit(images.killer, [Const.lead_x+300,Const.lead_y-100])
    if pos == True:
        Const.gameDisplay.blit(img, [Const.width/4, Const.height/4])
    Const.gameDisplay.blit(images.background, [0, 0])
    message_to_screen(("x:"+str(-Const.lead_x)+"y:"+str(Const.lead_y)), Const.black, [0,0], 50)
    health_bar()
    pygame.display.update()
def gameLoop():
    gameExit = False
    Const.gameDisplay.fill(Const.white)
    pygame.display.update()
    while not gameExit:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if Const.function == True:
                        Const.lead_x_change=Const.size
                        Const.lead_y_change=0
                        Const.pos = 3
                        Const.function = False

                elif event.key==pygame.K_RIGHT:
                    if Const.function == True:
                        Const.lead_x_change=-Const.size
                        Const.lead_y_change=0
                        Const.pos = 2
                        Const.function = False
                        
                elif event.key==pygame.K_UP:
                    if Const.function == True:
                        Const.lead_y_change=Const.size
                        Const.lead_x_change=0
                        Const.pos = 4
                        Const.function = False
                        
                elif event.key==pygame.K_DOWN:
                    if Const.function == True:
                        Const.lead_y_change=-Const.size
                        Const.lead_x_change=0
                        Const.pos = 1
                        Const.function = False
                        
                elif event.key==pygame.K_SPACE:
                    if Const.function == True:
                        Const.function = False
                        Const.lead_x_change=0
                        Const.lead_y_change=0
                        Menu_Script.game_menu()
                        Const.size = 4
                        
                elif event.key==pygame.K_x:
                    call_event()               
                if event.key==pygame.K_LSHIFT:
                    Const.size = 10   
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LSHIFT:
                    Const.size = 4
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    Const.lead_x_change=0   
                elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    Const.lead_y_change=0
        #block_call()
        Const.lead_x+=Const.lead_x_change
        Const.lead_y+=Const.lead_y_change
        if Const.pos == 1:
            if Const.lead_y_change == 0:
                display(images.main1, False)
                
            else:
                walk(images.main2, images.main1, images.main3, False)
                
        elif Const.pos == 2:
            if Const.lead_x_change == 0:
                display(images.right1, True)
                
            else:
                walk(images.right2, images.right1, images.right3, True)
                
        elif Const.pos == 3:
            if Const.lead_x_change == 0:
                display(images.left1, True)
                
            else:
                walk(images.left2, images.left1, images.left3, True)
                
        elif Const.pos == 4:
            if Const.lead_y_change == 0:
                display(images.back1, True)
                
            else:
                walk(images.back2, images.back1, images.back3, True)
        Const.function = True
                          
        if Const.lead_x_change != 0 or Const.lead_y_change != 0:
            if random.randrange(0, 200, 1) == 4:
                Const.lead_x_change = 0
                Const.lead_y_change = 0
                Const.Exit = 0
                Const.function = False
                Const.size = 4
                Action_Script.action()

  
            
            
        Const.clock.tick(Const.FPS)








