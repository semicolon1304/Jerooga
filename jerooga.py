import pygame

# Texture dictionary
type2Texture = {"water": pygame.image.load("Textures/Water.gif"), "land": pygame.image.load("Textures/Land.gif"), "net": pygame.image.load("Textures/Net.gif")}

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

# Tile class to be stored in the board 2d list, it should represent each type of block
class Tile:
    def __init__(self, state = "water"):
        self.state = state

    # Returns pygame texture
    def getTexture(self):
        return type2Texture[self.state]
    
class Jeroo(Tile):
    # TODO: Write this class
    pass
