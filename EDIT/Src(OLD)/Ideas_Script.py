import pygame
from pygame.locals import *
import time
import random

class Images():
    m1 = pygame.image.load('..\\EDIT\\1.png')
    m2 = pygame.image.load('..\\EDIT\\2.png')
    m3 = pygame.image.load('..\\EDIT\\3.png')
    m4 = pygame.image.load('..\\EDIT\\4.png')
    m5 = pygame.image.load('..\\EDIT\\5.png')
    m6 = pygame.image.load('..\\EDIT\\6.png')
    m7 = pygame.image.load('..\\EDIT\\7.png')
    
class Variables():
    width = 500
    height = 500
    posx = 0
    posy = 250
    fps = 60
    xchange = 0
    ychange = 0
    gameDisplay=pygame.display.set_mode((width,height))
    black = (255, 255, 255)
    Exit = False
    clock = pygame.time.Clock()
    
def Walk():
    Variables.gameDisplay.fill(Variables.black)
    Variables.gameDisplay.blit(Images.m1, [Variables.posx, Variables.posy])
    pygame.display.update()
    time.sleep(0.125)
    Variables.posx += 10
    Variables.gameDisplay.fill(Variables.black)
    Variables.gameDisplay.blit(Images.m1, [Variables.posx, Variables.posy])
    pygame.display.update()
    time.sleep(0.0125)
    Variables.posx += 10
    Variables.gameDisplay.fill(Variables.black)
    Variables.gameDisplay.blit(Images.m3, [Variables.posx, Variables.posy])
    pygame.display.update()
    time.sleep(0.125)
    Variables.posx += 10
    Variables.gameDisplay.fill(Variables.black)
    Variables.gameDisplay.blit(Images.m4, [Variables.posx, Variables.posy])
    pygame.display.update()
    time.sleep(0.125)
    Variables.posx += 10
    Variables.gameDisplay.fill(Variables.black)
    Variables.gameDisplay.blit(Images.m5, [Variables.posx, Variables.posy])
    pygame.display.update()
    time.sleep(0.125)
    Variables.posx += 10
    Variables.gameDisplay.fill(Variables.black)
    Variables.gameDisplay.blit(Images.m6, [Variables.posx, Variables.posy])
    pygame.display.update()
    time.sleep(0.125)
    Variables.posx += 10
    Variables.gameDisplay.fill(Variables.black)
    Variables.gameDisplay.blit(Images.m7, [Variables.posx, Variables.posy])
    pygame.display.update()
    time.sleep(0.125)
    Variables.posx += 10
    
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('BoomNack_TEST')
    Variables.gameDisplay.fill(Variables.black)
    pygame.display.update()
    while Variables.Exit==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    Walk()
                elif event.key==pygame.K_SPACE:
                    Variables.Exit = True
                elif event.key==pygame.K_q:
                    Variables.posx = 0
                    Variables.posy = 250
    Variables.clock.tick(Variables.fps)
    
pygame.quit()
quit()
