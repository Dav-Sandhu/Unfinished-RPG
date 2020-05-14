import pygame
from pygame.locals import *
import time
import random
import pickle

class application():

    def __init__(self):
        self.width = 1000
        self.height = 500
        self.posx = 0
        self.posy = 250
        self.xchange = 0
        self.ychange = 0
        self.counter = 1
        self.c = False
        self.gameDisplay = pygame.display.set_mode((self.width, self.height))
        self.white = (255, 255, 255)
        self.Exit = False
        self.Exit2 = False
        self.img()
    def img(self):
        self.m1 = pygame.image.load('..\\..\\EDIT\\1.png')
        self.m2 = pygame.image.load('..\\..\\EDIT\\2.png')
        self.m3 = pygame.image.load('..\\..\\EDIT\\3.png')
        self.m4 = pygame.image.load('..\\..\\EDIT\\4.png')
        self.m5 = pygame.image.load('..\\..\\EDIT\\5.png')
        self.m6 = pygame.image.load('..\\..\\EDIT\\6.png')
        self.m7 = pygame.image.load('..\\..\\EDIT\\7.png')
        self.p1 = pygame.image.load('..\\..\\EDIT\\pos\\pos1.png')
        self.p2 = pygame.image.load('..\\..\\EDIT\\pos\\pos2.png')
        self.p3 = pygame.image.load('..\\..\\EDIT\\pos\\pos3.png')
        self.p4 = pygame.image.load('..\\..\\EDIT\\pos\\pos4.png')
        self.p5 = pygame.image.load('..\\..\\EDIT\\pos\\pos5.png')
        self.p6 = pygame.image.load('..\\..\\EDIT\\pos\\pos6.png')
        self.p7 = pygame.image.load('..\\..\\EDIT\\pos\\pos7.png')
        self.p8 = pygame.image.load('..\\..\\EDIT\\pos\\pos8.png')
        self.b1 = pygame.image.load('..\\..\\EDIT\\b1.png')
        self.b2 = pygame.image.load('..\\..\\EDIT\\b2.png')
        self.t = pygame.image.load('..\\..\\EDIT\\title.png')
    def walk(self, image):
        self.image = image
        self.gameDisplay.fill(self.white)
        #self.gameDisplay.blit(self.s1, [self.posx-300, self.posy-500])
        self.gameDisplay.blit(self.image, [self.posx, self.posy])
        pygame.display.update()
        time.sleep(0.125)
        self.posx += 1
    def fight(self):
        self.gameDisplay.fill(self.white)
        self.gameDisplay.blit(self.p1, [250, 250])
        pygame.display.update()
        self.counter = 1
        while self.counter == 1:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.Exit = True
                    pygame.quit()
                    quit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c and self.c==False:
                        self.c = True
                        self.gameDisplay.blit(self.p2, [250, 250])
                        pygame.display.update()
                        time.sleep(0.1)
                        self.gameDisplay.blit(self.p3, [250, 250])
                        pygame.display.update()
                        time.sleep(0.1)
                        self.gameDisplay.blit(self.p4, [250, 250])
                        pygame.display.update()
                    elif event.key==pygame.K_v and self.c==False:
                        self.gameDisplay.blit(self.p7, [250, 250])
                        pygame.display.update()
                        time.sleep(0.1)
                        self.gameDisplay.blit(self.p8, [250, 250])
                        pygame.display.update()
                        time.sleep(0.1)
                        self.gameDisplay.blit(self.p1, [250, 250])
                        pygame.display.update()
                    elif event.key==pygame.K_x and self.c==True:
                        self.gameDisplay.blit(self.p5, [250, 250])
                        pygame.display.update()
                        time.sleep(0.1)
                        self.gameDisplay.blit(self.p6, [250, 250])
                        pygame.display.update()
                        time.sleep(0.1)
                        self.gameDisplay.blit(self.p4, [250, 250])
                        pygame.display.update()
                    elif event.key==pygame.K_c and self.c==True:
                        self.gameDisplay.blit(self.p3, [250, 250])
                        pygame.display.update()
                        time.sleep(0.1)
                        self.gameDisplay.blit(self.p2, [250, 250])
                        pygame.display.update()
                        time.sleep(0.1)
                        self.gameDisplay.blit(self.p1, [250, 250])
                        pygame.display.update()
                        self.c=False
                    elif event.key==pygame.K_q:
                        self.counter = 0
                        break
        self.counter = 1
        self.ctr()
    def mode1(self):
        self.gameDisplay.fill(self.white)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.Exit2 = True
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    while self.counter <= 7:
                        if self.counter == 1:
                            self.walk(self.m1)
                        elif self.counter == 2:
                            self.walk(self.m2)
                        elif self.counter == 3:
                            self.walk(self.m3)
                        elif self.counter == 4:
                            self.walk(self.m4)
                        elif self.counter == 5:
                            self.walk(self.m5)
                        elif self.counter == 6:
                            self.walk(self.m6)
                        elif self.counter == 7:
                            self.walk(self.m7)
                        self.counter += 1
                    self.counter = 1
                elif event.key==pygame.K_w:
                    self.posx = 0
                elif event.key==pygame.K_q:
                    self.Exit2 = True
                    self.gameDisplay.blit(self.t, [0,0])
                    pygame.display.update()

    def ctr(self):
        self.gameDisplay.blit(self.t, [0,0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.Exit = True
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    while self.Exit2 == False:
                        self.mode1()
                elif event.key==pygame.K_q:
                    self.Exit = True
                elif event.key==pygame.K_2:
                    self.fight()

    def run(self):
        pygame.init()
        pygame.display.set_caption('BoomNack_TEST')
        while self.Exit == False:
            self.ctr()
        pygame.quit()
        quit()

                
if __name__ == "__main__":
    app = application()
    app.run()
    
