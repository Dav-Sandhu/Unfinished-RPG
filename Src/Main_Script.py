import pygame
import Event_Script
from pygame.locals import *
import random
import time
import random
import pickle
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
    knight = pygame.image.load('..\\images\\Battle_Sprites\\knight.png')
    boss1_1 = pygame.image.load('..\\images\\Sprites\\boss1.1.png')
    boss1_2 = pygame.image.load('..\\images\\Sprites\\boss1.2.png')
    boss1_3 = pygame.image.load('..\\images\\Sprites\\boss1.3.png')
    mage = pygame.image.load('..\\images\\Sprites\\mage.png')
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
    wizard = pygame.image.load('..\\images\\Sprites\\wizard.png')
    killer = pygame.image.load('..\\images\\Sprites\\assassin.png')
    menu_save = pygame.image.load('..\\images\\Menus\Menu_Save.png')
    menu_options = pygame.image.load('..\\images\\Menus\\Menu_Options.png')
    menu_resume = pygame.image.load('..\\images\\Menus\\Menu_Resume.png')
    menu_quit = pygame.image.load('..\\images\\Menus\\Menu_Quit.png')
    intro = pygame.image.load('..\\images\\Intro\\intro.png')
    assassin = pygame.image.load('..\\images\\Menus\\class_assassin.png')
    classmage = pygame.image.load('..\\images\\Menus\\class_mage.png')
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
    background2 = pygame.image.load('..\\images\\Main\\Layout2.png')
    profile = pygame.image.load('..\\images\\Main\\Layout_menu.png')
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
    title = pygame.image.load('..\\images\\Intro\\Dragon Menu.png')
def message_to_screen(msg,color,measure,big):
    font=pygame.font.Font("nineteen font.ttf", big)
    screen_text=font.render(msg, True, color)
    Const.gameDisplay.blit(screen_text, measure)
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
    counter = False
    Exp = 0
    limit = 5000
    percent = 294.0
    percent2 = 110.0
    percent3 = 400.0
    percent4 = 100.0
    function = True
    sequence = 1
    set_pos = 500
    clock = pygame.time.Clock()
    shapeW = (width/2)-100
    loss = 0
    loss2 = 0
    dmg = 0
    commands = 0
    Class = 0
    Cy = 0.0
    quest1 = True
    load = False
    
    gameDisplay=pygame.display.set_mode((width,height))
def save():
    health = open("..\\save\\health.txt", 'wb')
    level = open("..\\save\\level.txt", 'wb')
    levelshow = open("..\\save\\levelshow.txt", 'wb')
    leadx = open("..\\save\\leadx.txt", 'wb')
    leady = open("..\\save\\leady.txt", 'wb')
    exp = open("..\\save\\exp.txt", 'wb')
    pos = open("..\\save\\pos.txt", 'wb')
    pickle.dump(player.player_health , health)
    pickle.dump(player.Level, level)
    pickle.dump(player.Level_show, levelshow)
    pickle.dump(Const.lead_x, leadx)
    pickle.dump(Const.lead_y, leady)
    pickle.dump(Const.Exp, exp)
    pickle.dump(Const.pos, pos)
    health.close()
    level.close()
    levelshow.close()
    leadx.close()
    leady.close()
    exp.close()
    pos.close()
def load():
    load1 = open("..\\save\\health.txt",'rb')
    load2 = open("..\\save\\level.txt", 'rb')
    load3 = open("..\\save\\levelshow.txt", 'rb')
    load4 = open("..\\save\\leadx.txt", 'rb')
    load5 = open("..\\save\\leady.txt", 'rb')
    load6 = open("..\\save\\exp.txt", 'rb')
    load7 = open("..\\save\\pos.txt", 'rb')
    player.player_health = pickle.load(load1)
    player.Level = pickle.load(load2)
    player.Level_show = pickle.load(load3)
    Const.lead_x = pickle.load(load4)
    Const.lead_y = pickle.load(load5)
    Const.Exp = pickle.load(load6)
    Const.pos = pickle.load(load7)
    load1.close()
    load2.close()
    load3.close()
    load4.close()
    load5.close()
    load6.close()
    load7.close()
def classes():
    select = 1
    while Const.Exit == 0:
        if select == 1:
            Const.gameDisplay.blit(images.archer, [0,0])
        elif select == 2:
            Const.gameDisplay.blit(images.classmage, [0,0])
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
                if event.key==pygame.K_LEFT:
                    if select != 1:
                        select -= 1
                    else:
                        select = 4
                    pygame.display.update()
                elif event.key==pygame.K_RIGHT:
                    if select != 4:
                        select += 1
                    else:
                        select = 1
                    pygame.display.update()
                elif event.key==pygame.K_v:
                    if select == 1:
                        Const.Class = 1
                    elif select == 2:
                        Const.Class = 2
                    elif select == 3:
                        Const.Class = 3
                    elif select == 4:
                        Const.Class = 4
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
    message_to_screen("Boomnack Presents", Const.white, [Const.width/2.5,Const.height/2], 25)
    pygame.display.update()
    time.sleep(2)
    Const.gameDisplay.fill(Const.black)
    Const.gameDisplay.blit(images.title, [0,0])
    pygame.display.update()
    counter = 1
    while counter == 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                counter = 0
                break
    counter = 1
    Const.gameDisplay.fill(Const.black)
    pygame.draw.rect(Const.gameDisplay, Const.white, [Const.shapeW, 50, 200, 99])
    pygame.draw.rect(Const.gameDisplay, Const.white, [Const.shapeW, 174, 200, 99])
    pygame.draw.rect(Const.gameDisplay, Const.white, [Const.shapeW, 298, 200, 99])
    message_to_screen("START", Const.black, [Const.shapeW+40, 80], 50)
    message_to_screen("QUIT", Const.black, [Const.shapeW+40, 204], 50)
    message_to_screen("LOAD", Const.black, [Const.shapeW+40, 327], 50)
    message_to_screen("Boomnack", Const.white, [0, (Const.height-25)], 25)
    pygame.display.update()
    Event_Script.title_menu()

    Const.clock.tick(Const.FPS)
    
    pygame.quit()
    quit()
