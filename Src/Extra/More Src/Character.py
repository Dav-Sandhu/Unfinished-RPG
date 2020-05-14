import pygame
import random

class characters():
    
    def __init__(self):
        pass
    def player(self):
        self.level = 1
        self.health = float(150 * (self.level/1.5))
        self.attack = 50 * self.level
    def knight(self):
        self.health = float(random.randrange(100.0, 170.0, 10.0))
        self.attack = 10
        self.exp = float(self.health * 10)
