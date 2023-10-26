import pygame
from time import sleep

class Jerooga:
    def __init__(self, secondsBetweenActions = 1, file:str="None", screenWidth:int=644, screenHeight:int=644):
        self.secondsBetweenActions = secondsBetweenActions
        self.pixelsPerBlock = 28
        # each block is self.pixelsPerBlock x self.pixelsPerBlock
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screenSize = (screenWidth, screenHeight)
        self.blocksWide = screenWidth // self.pixelsPerBlock
        self.blocksHigh = screenHeight // self.pixelsPerBlock

        if file != "None":
            lines = []
            f = open(file)
            toPush = []
            for x in f: 
                lines.append(f.readLine())
            for line in lines:
                for tile in line:
                    if tile == ".": state = "land"
                    elif tile == "F": state = "flower"
                    elif tile == "N": state = "net"
                    else: state = "water"
                    toPush.append(state)
          

            state = "temp" # Determine state from string
            self.board = [[Tile(x,y, state=state) for x in range(self.blocksWide)]]
            f.close()

            
            
        # Board is the play area, it is a 2d list, screenWidth//pixelsPerBlock x screenHeight//pixelsPerBlock
        #else:
        self.board = [[Tile(x,y) for x in range(self.blocksWide)] for y in range(self.blocksHigh)]

        # Jeroos should be stored in a list for easy iteration in loops
        self.jeroos = []

        # Pygame will initialize in the init for Jerooga, the screen will be updated each time something on the board is changed, for instance moving a jeroo
        pygame.init()
        self.window = pygame.display.set_mode(self.screenSize)

    def addJeroo(self, spawnPosition, flowers=0, direction = "E"):
        self.jeroos.append(Jeroo(self, len(self.jeroos), spawnPosition, flowers, direction))
        self.updateWindow()
        return self.jeroos[-1]
        
    def board_to_string(self):
        return [str(self.board[x][y]) for x in range(self.blocksWide) for y in range(self.blocksHigh)]
        
    def updateWindow(self):
        # Draws tiles
        for y in self.board:
            for tile in y:
                tile.draw(self.window, self.pixelsPerBlock)
        
        # Draws Jeroos
        for jerooIter in self.jeroos:
            jerooIter.draw(self.window, self.pixelsPerBlock)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        sleep(self.secondsBetweenActions)

    def allDone(self):
        # loop that checks for events and closes window, esc key should work too
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
        pygame.quit()
        exit()

    





# Tile class to be stored in the board 2d list, it should represent each type of block
class Tile:
    def __init__(self, blockX, blockY, state = "water"):
        self.state = state
        self.blockX = blockX
        self.blockY = blockY
        self.img = type2Texture[self.state]

    def setState(self, state):
        self.state = state

    # Returns pygame texture
    def getTexture(self):
        return type2Texture[self.state]

    def __str__(self):
        return self.state

    getState = __str__
    
    def draw(self, window, pixelsPerBlock):
        window.blit(self.getTexture(), (self.blockX*pixelsPerBlock, self.blockY*pixelsPerBlock))
    
    def getRect(self):
        rect = self.img.get_rect()
        return (self.x, self.y, rect[2], rect[3])
    




class Jeroo(Tile):
    def __init__(self, parentJerooga, number, spawnPosition, flowers = 0, direction = "E"):
        self.number = number
        self.flowers = flowers
        self.blockX, self.blockY = spawnPosition
        self.direction = direction
        self.parentJerooga = parentJerooga
    
    def draw(self, window, pixelsPerBlock):
        window.blit(self.getTexture(), (self.blockX*pixelsPerBlock, self.blockY*pixelsPerBlock))

    def getTexture(self):
        if self.isOnFlower():
            return type2Texture[f"{self.number}{self.direction}_F"]
        return type2Texture[f"{self.number}{self.direction}"]
            
    # Action methods
    def hop(self, numberOfSpaces=1):
        if self.direction == "N":
            self.blockY -= numberOfSpaces
        elif self.direction == "E":
            self.blockX += numberOfSpaces
        elif self.direction == "S":
            self.blockY += 1
        else:
            self.blockX -= 1

        self.parentJerooga.updateWindow()
        
    # Picks up the flower on the current position and places it in inventory
    def pick(self):
        self.parentJerooga.board[self.blockY][self.blockX] = "land"

        self.flowers += 1
        


    # Places flower at current position
    def plant(self):
        self.parentJerooga.board[self.blockY][self.blockX] = "flower"
        
        self.flowers -= 1
    

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
    
    def isOnFlower(self):
        return self.parentJerooga.board[self.blockY][self.blockX].getState() == "flower"








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