import pygame
from Tile import Tile

class Jerooga:
    def __init__(self, screenWidth=644, screenHeight=644):
        self.pixelsPerBlock = 28
        # each block is self.pixelsPerBlock x self.pixelsPerBlock
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screenSize = (screenWidth, screenHeight)
        self.blocksWide = screenWidth // self.pixelsPerBlock
        self.blocksHigh = screenHeight // self.pixelsPerBlock

        # Board is the play area, it is a 2d list, screenWidth//pixelsPerBlock x screenHeight//pixelsPerBlock
        self.board = [[Tile() for x in range(self.blocksWide)] for y in range(self.blocksHigh)]

        # Jeroos should be stored in a list for easy iteration in loops
        self.jeroos = []

        # Pygame will initialize in the init for Jerooga, the screen will be updated each time something on the board is changed, for instance moving a jeroo
        pygame.init()
        self.window = pygame.display.set_mode(self.screenSize)

    def board_to_string(self):
        return [str(self.board[x][y]) for x in range(self.blocksWide) for y in range(self.blocksHigh)]
        
    def updateWindow(self):
        # Draws tiles
        for y in self.board:
            for tile in y:
                tile.draw(self.window)
        
        # Draws Jeroos
        for jerooIter in self.jeroos:
            jerooIter.draw(self.window)
        pass







   
    









# Tile class to be stored in the board 2d list, it should represent each type of block
class Tile:
    def __init__(self, blockX, blockY, state = "water"):
        self.state = state
        self.blockX = blockX
        self.blockY = blockY
        self.img = type2Texture[self.state]

    # Returns pygame texture
    def getTexture(self):
        return type2Texture[self.state]

    def __str__(self):
        return self.state

    getState = __str__
    
    def draw(self, window):
        window.blit(self.getTexture(), (self.blockX*, self.yPos))
    
    def getRect(self):
        rect = self.img.get_rect()
        return (self.x, self.y, rect[2], rect[3])
    
class Jeroo(Tile):
    def __init__(self, number, spawnPosition="Placeholder, correct later", flowers = 0):
        self.number = number
        self.flowers = flowers
        self.spawnPosition = spawnPosition
        self.direction = "E"

    def getTexture(self):
        if self.board[self.blockY][self.blockX].getState() == "flower":
            return type2Texture[f"{self.number}{self.direction}_F"]
        return type2Texture[f"{self.number}{self.direction}"]
            
    
    # Action methods
    def hop(numberOfSpaces=1):
        pass
        # Picks up the flower on the current position and places it in inventory
    def pick():
        pass

        # Places flower at current position
    def plant(self, window):
        #= Tile("Flower")
        pass
    
        # Places a flower one block in the direction that the jeroo is facing
    def toss():
        pass
    
    def give():
        pass

    def turn(direction):
        pass  

    # Boolean Methods (not by zack "BooleanMaster" McKenzie)
    
    def hasFlower(self):
        return True if self.flowers > 0 else False
    
    def isFacing(self, direction):
        return True if self.direction == direction else False








# Texture dictionary
type2Texture = {
    "collision": pygame.image.load("Textures/Collision.gif"),
    "flower": pygame.image.load("Textures/Flower.gif"),
    "trapped": pygame.image.load("Textures/Trapped.gif"),
    "wet": pygame.image.load("Textures/Wet.gif"),
    "collision": pygame.image.load("Textures/Collision.gif"),
    "water": pygame.image.load("Textures/Water.gif"),
    "land": pygame.image.load("Textures/Land.gif"),
    "net": pygame.image.load("Textures/Net.gif")
    }
# Makes the textures for the jeroos with various flowers and directions
type2Texture.update({f"{n}{d}{f}": pygame.image.load(f"Textures/{n}{d}{f}.gif") for n in range(4) for d in "NESW" for f in ("","_F")})