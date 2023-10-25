import pygame
from pygame.locals import *
'''
    fish fish
 fish fish fish fish fish
fish fish fish fish fish 
 fish fish fish fish fish
    fish fish fish
'''
class Mario():
    def __init__(self, xPos=0, yPos=0):
        self.xPos = xPos
        self.yPos = yPos
        self.img = pygame.image.load("Resources/sora.png")
        self.width = self.getRect()[2]
        self.height = self.getRect()[3]

    def __str__(self):
        return f"Position=({self.xPos},{self.yPos})"

    def changeX(self, value):
        self.xPos += value

    def changeY(self, value):
        self.yPos += value

    def jump(self):
        self.changeY(-100)

    def draw(self, window):
        window.blit(self.img, (self.xPos, self.yPos))
    
    def getRect(self):
        rect = self.img.get_rect()
        return (self.xPos, self.yPos, rect[2], rect[3])
    
    def collision(self, block):
        return ((block.yPos + block.height >= self.yPos and block.yPos <= self.yPos + self.height) and (block.xPos + block.width >= self.xPos and block.xPos <= self.xPos + self.width))