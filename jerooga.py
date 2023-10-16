import pygame

class Jerooga:
    def __init__(self, screenWidth=1024, screenHeight=1024):
        self.pixelsPerBlock = 32
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screenSize = (screenWidth, screenHeight)

        pygame.init()
        self.window = pygame.display.set_mode(self.screenSize)

