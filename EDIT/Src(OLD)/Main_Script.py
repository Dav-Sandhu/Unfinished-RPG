import pygame
import Event_Script
from pygame.locals import *
import random
import time
import random
class rat():
    rat_health = float(random.randrange(100.0, 170.0, 10.0))
    rat_damage = 10
    rat_ExpGain = float(rat_health * 10)
class player():
    Level = 1
    Level_show = 1.0
    player_health = float(150 * (Level/1.5))
    player_attack = 50 * Level
    player_ability = 50
class images():
    rat = pygame.image.load('..\\images\\Battle_Sprites\\rat.png')
    boss1_1 = pygame.image.load('..\\images\\Sprites\\boss1.1.png')
    boss1_2 = pygame.image.load('..\\images\\Sprites\\boss1.2.png')
    boss1_3 = pygame.image.load('..\\images\\Sprites\\boss1.3.png')
    main1 = pygame.image.load('..\\images\\Sprites\\main1.png')
    main2 = pygame.image.load('..\\images\\Sprites\\main2.png')
    main3 = pygame.image.load('..\\images\\Sprites\\main3.png')
    back1 = pygame.image.load('..\\images\\Sprites\\back1.png')
    back2 = pygame.image.load('..\\images\\Sprites\\back2.png')
    back3 = pygame.image.load('..\\images\\Sprites\\back3.png')
    left1 = pygame.image.load('..\\images\\Sprites\\left1.png')
    left2 = pygame.image.load('..\\images\\Sprites\\left2.png')
    left3 = pygame.image.load('..\\images\\Sprites\\left3.png')
    right1 = pygame.image.load('..\\images\\Sprites\\right1.png')
    right2 = pygame.image.load('..\\images\\Sprites\\right2.png')
    right3 = pygame.image.load('..\\images\\Sprites\\right3.png')
    menu_save = pygame.image.load('..\\images\\Menus\Menu_Save.png')
    menu_options = pygame.image.load('..\\images\\Menus\\Menu_Options.png')
    menu_resume = pygame.image.load('..\\images\\Menus\\Menu_Resume.png')
    menu_quit = pygame.image.load('..\\images\\Menus\\Menu_Quit.png')
    intro = pygame.image.load('..\\images\\Intro\\intro.png')
    assassin = pygame.image.load('..\\images\\Menus\\class_assassin.png')
    mage = pygame.image.load('..\\images\\Menus\\class_mage.png')
    fighter = pygame.image.load('..\\images\\Menus\\class_fighter.png')
    archer = pygame.image.load('..\\images\\Menus\\class_archer.png')
    b1 = pygame.image.load('..\\images\\Battle\\Battle_Unselect.png')
    b2 = pygame.image.load('..\\images\\Battle\\Battle_Attack.png')
    b3 = pygame.image.load('..\\images\\Battle\\Battle_Ability.png')
    b4 = pygame.image.load('..\\images\\Battle\\Battle_Exit.png')
    b5 = pygame.image.load('..\\images\\Battle\\Battle_Inventory.png')
    b6 = pygame.image.load('..\\images\\Battle\\Battle_Odessey.png')
    b7 = pygame.image.load('..\\images\\Battle\\Battle_Player.png')
    b8 = pygame.image.load('..\\images\\Battle\\Battle_Info.png')
    background = pygame.image.load('..\\images\\Main\\Layout.png')
    inventory = pygame.image.load('..\\images\\Commands\\Inventory_Open.png')
    inventory2 = pygame.image.load('..\\images\\Commands\\Inventory_Open2.png')
    inventory3 = pygame.image.load('..\\images\\Commands\\Inventory_Open3.png')
    inventory4 = pygame.image.load('..\\images\\Commands\\Inventory_Open4.png')
    inventory5 = pygame.image.load('..\\images\\Commands\\Inventory_Open5.png')
    inventory6 = pygame.image.load('..\\images\\Commands\\Inventory_Open6.png')
    inventory7 = pygame.image.load('..\\images\\Commands\\Inventory_Open7.png')
    inventory8 = pygame.image.load('..\\images\\Commands\\Inventory_Open8.png')
    ability = pygame.image.load('..\\images\\Commands\\Ability_Open.png')
    temp = pygame.image.load('..\\images\\Commands\\Template.png')
def message_to_screen(msg,color,measure,big):
    font=pygame.font.SysFont(None, big)
    screen_text=font.render(msg, True, color)
    Const.gameDisplay.blit(screen_text, measure)
    pygame.display.update()

class Const:
   
    Dark_blue=(0,0,200)
    Dark_green=(0,200,0)
    white=(255,255,255)
    light_grey=(220,230,230)
    grey=(200,200,200)
    black=(0,0,0)
    red=(255,0,0)
    lawn_green = (124 ,255, 0)
    green=(0,255,0)
    forest_green=(34,139,34)
    blue=(0,0,255)
    thistle=(216, 191, 216)
   
    size=4
    height=576
    width=768
    FPS=60
    lead_x=300
    lead_y=300
    lead_x_change=0
    lead_y_change=0
    pos = 1
    sec = 1
    Num = 0
    Exit = 0
    Exp = 0
    limit = 5000
    percent = 294.0
    percent2 = 110.0
    sequence = 1
    set_pos = 500
    clock = pygame.time.Clock()
    shapeW = (width/2)-100
    loss = 0
    loss2 = 0
    dmg = 0
    commands = 0
    Class = 0
    
    gameDisplay=pygame.display.set_mode((width,height))
    
def classes():
    select = 1
    while Const.Exit == 0:
        if select == 1:
            Const.gameDisplay.blit(images.archer, [0,0])
        elif select == 2:
            Const.gameDisplay.blit(images.mage, [0,0])
        elif select == 3:
            Const.gameDisplay.blit(images.fighter, [0,0])
        elif select == 4:
            Const.gameDisplay.blit(images.assassin, [0,0])         
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    if select != 1:
                        select -= 1
                    else:
                        select = 4
                    pygame.display.update()
                elif event.key==pygame.K_DOWN:
                    if select != 4:
                        select += 1
                    else:
                        select = 1
                    pygame.display.update()
                elif event.key==pygame.K_v:
                    if select == 1:
                        Const.class_archer = 1
                    elif select == 2:
                        Const.class_mage = 1
                    elif select == 3:
                        Const.class_fighter == 1
                    elif select == 4:
                        Const.class_assassin = 1
                    Const.Exit = 1
                    Event_Script.gameLoop()

def cutscenes():
    if Const.sequence == 1:
        while Const.set_pos > -1184:
            Const.gameDisplay.fill(Const.white)
            Const.gameDisplay.blit(images.intro, [0, Const.set_pos])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_v:
                        Const.set_pos -=3000
                        
            pygame.display.update()
            time.sleep(0.1)
            Const.set_pos -= 3
        classes()
                    
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Boomnack')
    message_to_screen("BoomNack Presents", Const.white, [Const.width/2.5,Const.height/2], 25)
    pygame.display.update()
    time.sleep(2)
    Const.gameDisplay.fill(Const.black)
    pygame.draw.rect(Const.gameDisplay, Const.white, [Const.shapeW, 50, 200, 99])
    pygame.draw.rect(Const.gameDisplay, Const.white, [Const.shapeW, 174, 200, 99])
    pygame.draw.rect(Const.gameDisplay, Const.white, [Const.shapeW, 298, 200, 99])
    message_to_screen("START", Const.black, [Const.shapeW+40, 80], 50)
    message_to_screen("QUIT", Const.black, [Const.shapeW+40, 204], 50)
    message_to_screen("LOAD", Const.black, [Const.shapeW+40, 327], 50)
    message_to_screen("BoomNack", Const.white, [0, (Const.height-25)], 25)
    pygame.display.update()
    
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
                    
            else:
                pygame.draw.rect(Const.gameDisplay, Const.white, [Const.shapeW, 298, 200, 99])
                message_to_screen("LOAD", Const.black, [Const.shapeW+40, 327], 50)
                pygame.display.update(Const.shapeW+40, 327, 25, 50)

    Const.clock.tick(Const.FPS)
    
    pygame.quit()
    quit()
