import pygame

type2Texture = {"water": pygame.image.load("Textures/Water.gif")}

class Jerooga:
    def __init__(self, screenWidth=644, screenHeight=644):
        self.pixelsPerBlock = 28
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screenSize = (screenWidth, screenHeight)

        board = [[Tile() for x in range(screenWidth // self.pixelsPerBlock)] for y in range(screenHeight // self.pixelsPerBlock)]

        self.jeroos = []

        pygame.init()
        self.window = pygame.display.set_mode(self.screenSize)

class Tile:
    def __init__(self, type = "water"):
        self.type = type

    def getTexture(self):
        return type2Texture[self.type]

