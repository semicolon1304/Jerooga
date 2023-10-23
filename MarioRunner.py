import pygame
from pygame.locals import * 
from Wall import * 
from Mario import *

'''
    fish fish
 fish fish fish fish fish
fish fish fish fish fish 
 fish fish fish fish fish
    fish fish fish
'''
alonzo = Mario(5,558)
wall = Wall(750, 550)

pygame.init()
myDisplay = pygame.display.set_mode((800,600))
myDisplay.fill((255,255,255))
clock = pygame.time.Clock()
center = myDisplay.get_rect().center

end = True
huh = False
counter = 0
while end:
    pygame.display.update()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            end = False
            pygame.quit()

        if event.type == KEYDOWN and event.key == K_SPACE:
            if alonzo.yPos == 558: alonzo.jump()
        
        if alonzo.xPos > 753 : alonzo.xPos = 753
        if alonzo.yPos > 558 : alonzo.yPos = 558
        
    if alonzo.collision(wall):
        huh = True
        while huh:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    huh = False
                    pygame.quit()
            print(end="")
        end = False

    if alonzo.yPos < 558: alonzo.changeY(1)
    if wall.xPos > -49 : wall.changeX(-5)
    if wall.xPos <= -49 : wall.xPos = 750
        
    myDisplay.fill((255,255,255))
    alonzo.draw(myDisplay)
    wall.draw(myDisplay)
    print(alonzo.collision(wall))
