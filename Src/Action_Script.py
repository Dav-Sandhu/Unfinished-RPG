import pygame
from Main_Script import Const
from Main_Script import message_to_screen
from Main_Script import images
from Main_Script import player
from Main_Script import rat
import random
import time
def Display(N1, N2, N3, N4, img, full):
    Const.gameDisplay.fill(Const.black)
    Const.gameDisplay.blit(img, [0, 0])
    Const.gameDisplay.blit(images.knight, [150, 100])
    pygame.draw.rect(Const.gameDisplay, Const.green, [237, 11, N1, 12])
    pygame.draw.rect(Const.gameDisplay, Const.lawn_green, [237, 11, N1, 4])
    pygame.draw.rect(Const.gameDisplay, Const.green, [236, 12, 1, 10])
    pygame.draw.rect(Const.gameDisplay, Const.lawn_green, [236, 12, N1, 2])
    pygame.draw.rect(Const.gameDisplay, Const.green, [235, 13, 1, 8])
    pygame.draw.rect(Const.gameDisplay, Const.green, [234, 14, 1, 6])
    pygame.draw.rect(Const.gameDisplay, Const.green, [54, 494, N2, 14])
    pygame.draw.rect(Const.gameDisplay, Const.lawn_green, [54, 494, N2, 3])
    message_to_screen(str(N4), Const.black, [89, 497], 20)
    message_to_screen(str(N3), Const.black, [370, 13], 20)
    if Const.percent == 294 and full == 1:
        pygame.draw.rect(Const.gameDisplay, Const.green, [531, 12, 1, 10])
        pygame.draw.rect(Const.gameDisplay, Const.lawn_green, [531, 12, 1, 3])
        pygame.draw.rect(Const.gameDisplay, Const.green, [532, 13, 1, 8])
        pygame.draw.rect(Const.gameDisplay, Const.lawn_green, [532, 13, 1, 1])
        pygame.draw.rect(Const.gameDisplay, Const.green, [533, 14, 1, 6])
    pygame.display.update()
    time.sleep(0.05)
def health(char):
    if char == "rat":
        while Const.loss < (Const.dmg*294.0):
            if rat.rat_health - Const.loss > 0:
                Display(Const.percent - Const.loss, Const.percent2, rat.rat_health-Const.loss2, player.player_health, images.b1, 0)
                Const.loss += (player.player_attack * 0.05)*2.94
                Const.loss2 = Const.loss/2.94
            else:
                Const.loss = 0
                Const.loss2 = 0
                break
        if rat.rat_health - Const.loss2 > 0:
            Const.percent -= (Const.dmg*294.0)
            rat.rat_health-=player.player_attack
        else:
            rat.rat_health = 0
            Const.percent = 0
    elif char == "player":     
        while Const.loss <= 10:
            Display(Const.percent, Const.percent2 - Const.loss, rat.rat_health, player.player_health-Const.loss2, images.b1, 1)
            Const.loss += 1
            Const.loss2 = rat.rat_damage*(0.1*(Const.loss))
        player.player_health-=rat.rat_damage
        Const.percent2 -= (110.0*(0.1*player.Level))
    Const.loss = 0
    Const.loss2 = 0
def animation(img):
    Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, img, 1)
    time.sleep(0.0005)
    Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, images.b1, 1)

def action():
    Const.counter = 1
    Const.function = True
    if Const.load == True:
        Const.percent2*=(player.player_health/(player.Level*100))
        Const.load = False
    Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, images.b1, 1)
    rat.rat_ExpGain = rat.rat_health * 10
    Const.dmg = player.player_attack / rat.rat_health
    while Const.Exit == 0:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                    if Const.function == True:
                        Const.function = False
                        Const.counter = 2
                        animation(images.b4)
                        Const.Exit = 1
                        Const.percent = 294.0
                        message_to_screen("you ran away", Const.black, [200, 250], 25)
                        rat.rat_health = float(random.randrange(100, 170, 10))
                        pygame.display.update()
                        time.sleep(1)
                elif event.key==pygame.K_v:
                    if Const.function == True:
                        Const.function = False
                        Const.counter = 2
                        animation(images.b3)
                        Const.gameDisplay.blit(images.ability , [192, 144])
                        pygame.display.update()
                        while Const.commands == 0:
                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                    pygame.quit()
                                    quit()
                                elif event.type==pygame.KEYDOWN:
                                    if event.key==pygame.K_v:
                                        Const.commands = 1
                        Const.commands = 0
                        animation(images.b3)
                        Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, images.b1, 1)
                elif event.key==pygame.K_z:
                    if Const.function == True:
                        Const.function = False
                        Const.counter = 2
                        inventory_images_list = [images.inventory, images.inventory2, images.inventory3, images.inventory4, images.inventory5, images.inventory6, images.inventory7, images.inventory8]
                        animation(images.b5)
                        Const.gameDisplay.blit(images.inventory , [192, 144])
                        pygame.display.update()
                        Num = 0
                        Num2 = 0
                        Num3 = 0
                        while Const.commands == 0:
                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                    pygame.quit()
                                    quit()
                                elif event.type==pygame.KEYDOWN:
                                    if event.key==pygame.K_z:
                                        Const.commands = 1
                                    if event.key==pygame.K_LEFT:
                                        if Num == 0:
                                            Num = 7
                                        else:
                                            Num -= 1
                                    elif event.key==pygame.K_RIGHT:
                                        if Num == 7:
                                            Num = 0
                                        else:
                                            Num += 1
                                    Const.gameDisplay.blit(inventory_images_list[Num] , [192, 144])
                                    pygame.display.update()
                        Const.commands = 0
                        animation(images.b5)
                        Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, images.b1, 1)
                elif event.key==pygame.K_c:
                    if Const.function == True:
                        Const.function = False
                        Const.counter = 2
                        if rat.rat_health >= player.player_attack:
                            animation(images.b2)
                            health("rat")
                            Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, images.b1, 1)
                        elif player.player_attack > rat.rat_health > 0:
                            health("rat")
                            rat.rat_health = 0
                            Const.percent = 0
                            Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, images.b1, 0)
                        if rat.rat_health <= 0:
                            Const.percent = 0
                            Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, images.b1, 0)
                            pygame.display.update()
                            Const.Exp += rat.rat_ExpGain
                            Const.percent = 294.0
                            Const.Cy += 0.3
                            Const.counter = 1
                            Const.function = False
                            Const.gameDisplay.fill(Const.black)
                            message_to_screen("You Win + "+str(rat.rat_ExpGain)+" EXP", Const.white, [200, 250], 50)
                            message_to_screen("Cy + $0.3", Const.white, [200, 275], 24)
                            pygame.display.update()
                            time.sleep(2)
                            rat.rat_health = float(random.randrange(100.0, 170.0, 10.0))
                            Const.Exit = 1
                            if Const.Exp >= Const.limit:
                                if player.Level < 50:
                                    player.Level_show += 1.0
                                    player.Level += 1
                                    Const.Exp -= Const.limit
                                    Const.limit += Const.limit*0.1
                                    Const.percent2 = 110.0
                                    player.player_health = 100.0 * player.Level_show
                                    player.player_attack = 50.0 * player.Level_show
                                    Const.gameDisplay.fill(Const.black)
                                    message_to_screen("congratulations ", Const.white, [Const.width/2.25, Const.height/1.75], 50)
                                    message_to_screen("you are now level "+str(player.Level)+"!", Const.white, [Const.width/2.25, Const.height/2], 50)
                                    pygame.display.update()
                                    time.sleep(2)
                            break
                    
                        if Const.Exit != 1:
                            health("player")
                            Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, images.b1, 1)
                            if player.player_health == 0:
                                Const.gameDisplay.fill(Const.blue)
                                message_to_screen("you lose", Const.white, [Const.width/2.25, Const.height/1.75], 25)
                                time.sleep(2)
                                pygame.display.update()
                                pygame.quit()
                                quit()
            if Const.counter == 1:
                Const.function = True
            elif Const.counter == 2:
                Const.counter = 1
