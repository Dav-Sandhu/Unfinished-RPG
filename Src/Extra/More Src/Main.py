import pygame
import os
import sys

class message_to_screen(msg, color, measure, big):
    def __init__(self):
        self.msg = msg
        self.color = color
        self.measure = measure
        self.big = big
        font=pygame.font.Font("nineteen font.ttf", self.big)
        screen_text=font.render(self.msg, True, self.color)
        self.window.blit(screen_text, self.measure)

class game(self):    
    def __init__(self):
        pygame.init()
        self.load_images()
        
        self.height=576
        self.width=768
        
        self.window = pygame.display.set_mode((width,height))
        
        self.white=(255,255,255)
        self.black=(0,0,0)
        self.lawn_green = (124 ,255, 0)
        self.green=(0,255,0)
        
        pygame.display.set_caption('Boomnack')

    def load_images(self):
        self.images = {}

        for root, dirs, files in os.walk("images/"):
            for name in files:
                if name.endswith(".png"):
                    self.images[name[:-4]] = pygame.image.load(
                        os.path.realpath(os.path.join(root,name)))
                    
    
    def run(self):
        message_to_screen("Boomnack Presents", self.white,
            [self.width/2.5,self.height/2], 25)
        pygame.display.update()
        time.sleep(2)
        self.window.fill(self.black)
        

if __name__ == "__main__":
    playGame = game()
    playGame.run()
    
