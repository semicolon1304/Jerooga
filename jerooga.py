import pygame

# Texture dictionary
type2Texture = {"water": pygame.image.load("Textures/Water.gif")}

class Jerooga:
    def __init__(self, screenWidth=644, screenHeight=644):
        self.pixelsPerBlock = 28
        # each block is self.pixelsPerBlock x self.pixelsPerBlock
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screenSize = (screenWidth, screenHeight)

        # Board is the play area, it is a 2d list, screenWidth//pixelsPerBlock x screenHeight//pixelsPerBlock
        board = [[Tile() for x in range(screenWidth // self.pixelsPerBlock)] for y in range(screenHeight // self.pixelsPerBlock)]

        # Jeroos should be stored in a list for easy iteration in loops
        self.jeroos = []

        # Pygame will initialize in the init for Jerooga, the screen will be updated each time something on the board is changed, for instance moving a jeroo
        pygame.init()
        self.window = pygame.display.set_mode(self.screenSize)

#
class Tile:
    def __init__(self, type = "water"):
        self.type = type

    def getTexture(self):
        return type2Texture[self.type]

