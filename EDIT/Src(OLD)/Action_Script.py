import pygame
from Main_Script import Const
from Main_Script import message_to_screen
from Main_Script import images
from Main_Script import player
from Main_Script import rat
import random
import time
def Display(N1, N2, N3, N4, img, full):
    Const.gameDisplay.blit(img, [0, 0])
    Const.gameDisplay.blit(images.rat, [150, 100])
    pygame.draw.rect(Const.gameDisplay, Const.green, [237, 11, N1, 12])
    pygame.draw.rect(Const.gameDisplay, Const.lawn_green, [237, 11, N1, 4])
    pygame.draw.rect(Const.gameDisplay, Const.green, [236, 12, 1, 10])
    pygame.draw.rect(Const.gameDisplay, Const.lawn_green, [236, 12, N1, 2])
    pygame.draw.rect(Const.gameDisplay, Const.green, [235, 13, 1, 8])
    pygame.draw.rect(Const.gameDisplay, Const.green, [234, 14, 1, 6])
    pygame.draw.rect(Const.gameDisplay, Const.green, [54, 494, N2, 14])
    pygame.draw.rect(Const.gameDisplay, Const.lawn_green, [54, 494, N2, 3])
    message_to_screen(str(N4), Const.black, [89, 494], 20)
    message_to_screen(str(N3), Const.black, [370, 11], 20)
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
        Const.percent2 -= (110.0*(0.1*player.Level_show))
    Const.loss = 0
    Const.loss2 = 0
def animation(img):
    Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, img, 1)
    time.sleep(0.0005)
    Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, images.b1, 1)

def action():
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
                    animation(images.b4)
                    Const.Exit = 1
                    Const.percent = 294.0
                    message_to_screen("you ran away", Const.black, [200, 250], 25)
                    rat.rat_health = float(random.randrange(100, 170, 10))
                    pygame.display.update()
                    time.sleep(1)
                if event.key==pygame.K_v:
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
                    Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, images.b1, 1)
                if event.key==pygame.K_z:
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
                                elif event.key==pygame.K_LEFT:
                                    if Num == 0:
                                        Num = 7
                                    else:
                                        Num -= 1
                                    Const.gameDisplay.blit(inventory_images_list[Num] , [192, 144])
                                    pygame.display.update()
                                elif event.key==pygame.K_RIGHT:
                                    if Num == 7:
                                        Num = 0
                                    else:
                                        Num += 1
                                    Const.gameDisplay.blit(inventory_images_list[Num] , [192, 144])
                                    pygame.display.update()
                                elif event.key==pygame.K_v:
                                    Const.gameDisplay.blit(images.temp , [196+(Num2*48), 237+(Num3*48)])
                                    pygame.display.update()
                                elif event.key==pygame.K_x:
                                    if Num2 == 7:
                                        Num2 = 0
                                    else:
                                        Num2 += 1
                                elif event.key==pygame.K_y:
                                    if Num3 == 3:
                                        Num3 = 0
                                    else:
                                        Num3 += 1
                    Const.commands = 0
                    Display(Const.percent, Const.percent2 , rat.rat_health, player.player_health, images.b1, 1)
                elif event.key==pygame.K_c:
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
                        message_to_screen("you win + "+str(rat.rat_ExpGain)+" EXP", Const.black, [200, 250], 25)
                        pygame.display.update()
                        time.sleep(0.5)
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
                                message_to_screen("congratulations ", Const.white, [Const.width/2.25, Const.height/1.75], 25)
                                message_to_screen("you are now level "+str(player.Level)+"!", Const.white, [Const.width/2.25, Const.height/2], 25)
                                pygame.display.update()
                                time.sleep(0.5)
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
