import pygame
from time import sleep

class Jerooga:
    def __init__(self, secondsBetweenActions = 1.0, file:str="defaultMap.jev", screenWidth:int=728, screenHeight:int=728):
        self.secondsBetweenActions = secondsBetweenActions
        self.pixelsPerBlock = 28
        # each block is self.pixelsPerBlock x self.pixelsPerBlock
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screenSize = (screenWidth, screenHeight)
        self.blocksWide = screenWidth // self.pixelsPerBlock
        self.blocksHigh = screenHeight // self.pixelsPerBlock
        # Board is the play area, it is a 2d list, screenWidth//pixelsPerBlock x screenHeight//pixelsPerBlock
        self.board = [[Tile(x,y) for x in range(self.blocksWide)] for y in range(self.blocksHigh)]
        self.drowned = False

        # Load board from file
        if file != "None":
            with open(file, 'r') as f:
                lines = f.readlines()
            lines = [line.rstrip('\n') for line in lines]
            for y, line in enumerate(lines):
                for x, tile in enumerate(line):
                    if tile == ".": state = "land"
                    elif tile == "F": state = "flower"
                    elif tile == "N": state = "net"
                    else: state = "water"
                    self.board[y+1][x+1].setState(state)
            f.close()

        # Jeroos should be stored in a list for easy iteration in loops
        self.jeroos = []

        # Pygame will initialize in the init for Jerooga, the screen will be updated each time something on the board is changed, for instance moving a jeroo
        pygame.init()
        self.window = pygame.display.set_mode(self.screenSize)

    def addJeroo(self, spawnPosition, flowers=0, direction = "E"):
        self.jeroos.append(Jeroo(self, len(self.jeroos), [i+1 for i in spawnPosition], flowers, direction))
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
        if self.drowned:
            pygame.quit()
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

    def getState(self, x, y):
        return self.board[y][x].getState()
    
    def setState(self, x, y, state):
        self.board[y][x].setState(state)

    def getJeroo(self, x, y):
        for jeroo in self.jeroos:
            if jeroo.getBlock() == (x,y):
                return jeroo
        return None
    
    def getJerooColl(self, x, y):
        jeroosAtCoord = []
        for jeroo in self.jeroos:
            if jeroo.getBlock() == (x, y):
                jeroosAtCoord.append(jeroo)
        if len(jeroosAtCoord) > 0:
            for jeroo in jeroosAtCoord:
                jeroo.setState("collided")
            return True
        return False

    










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
    
    def getBlock(self):
        return (self.blockX, self.blockY)










class Jeroo(Tile):
    def __init__(self, parentJerooga, number, spawnPosition, flowers = 0, direction = "E"):
        self.number = number
        self.flowers = flowers
        self.blockX, self.blockY = spawnPosition
        self.direction = direction
        self.parentJerooga = parentJerooga
        self.state = "normal"
    
    def draw(self, window, pixelsPerBlock):
        window.blit(self.getTexture(), (self.blockX*pixelsPerBlock, self.blockY*pixelsPerBlock))

    def getTexture(self):
        if self.state == "net":
            return type2Texture["trapped"]
        elif self.state == "water":
            return type2Texture["wet"]
        elif self.state == "collided":
            return type2Texture["collision"]
        elif self.isOnFlower():
            return type2Texture[f"{self.number}{self.direction}_F"]
        return type2Texture[f"{self.number}{self.direction}"]
            
    # Action methods
    def hop(self, numberOfSpaces=1):
        if self.direction == "N":
            self.blockY -= numberOfSpaces
        elif self.direction == "E":
            self.blockX += numberOfSpaces
        elif self.direction == "S":
            self.blockY += numberOfSpaces
        else:
            self.blockX -= numberOfSpaces

        # start of net collision    
        blockAtCurrent = self.parentJerooga.getState(self.blockX, self.blockY)
        if blockAtCurrent not in ("land", "flower"):
            self.setState(blockAtCurrent)
            self.parentJerooga.updateWindow()
            self.parentJerooga.allDone()

        if self.parentJerooga.getJerooColl(*self.getBlock()):
            self.parentJerooga.updateWindow()
            self.parentJerooga.allDone()


        self.parentJerooga.updateWindow()

    def getFlowers(self):
        return self.flowers
    
    def getInRDirection(self, relativeDirection):
        relativeDirection = relativeDirection.lower()
        if relativeDirection in ("h", "here"):
            return (self.blockX, self.blockY)
        elif relativeDirection in ("a", "ahead"):
            if self.direction == "N":
                potentialCoordinate = (self.blockX, self.blockY-1)
            elif self.direction == "E":
                potentialCoordinate = (self.blockX+1, self.blockY)
            elif self.direction == "S":
                potentialCoordinate = (self.blockX, self.blockY+1)
            else:
                potentialCoordinate = (self.blockX-1, self.blockY)
            return potentialCoordinate
        elif relativeDirection in ("l", "left"):
            if self.direction in ("N, S"):
                return (self.blockX+(-1 if self.direction == "N" else 1), self.blockY)
            else:
                return (self.blockX, self.blockY+(-1 if self.direction == "E" else 1))
        else:
            if self.direction in ("N, S"):
                return (self.blockX+(1 if self.direction == "N" else -1), self.blockY)
            else:
                return (self.blockX, self.blockY+(1 if self.direction == "E" else -1))
        
            
    def giveFlowers(self, number=1):
        self.flowers += number
        
    # Picks up the flower on the current position and places it in inventory
    def pick(self):
        if self.parentJerooga.getState(self.blockX, self.blockY) == "flower":
            self.parentJerooga.setState(self.blockX, self.blockY, "land")
            self.flowers += 1

        self.parentJerooga.updateWindow()
        


    # Places flower at current position
    def plant(self):
        if self.flowers > 0 and self.parentJerooga.getState(self.blockX, self.blockY) != "flower":
            self.parentJerooga.setState(self.blockX, self.blockY, "flower")
            self.flowers -= 1
        
        self.parentJerooga.updateWindow()
    

    # Places a flower one block in the direction that the jeroo is facing
    def toss(self):
        if self.flowers > 0:
            potentialCoordinate = self.getInRDirection("a")
            if self.parentJerooga.getState(*potentialCoordinate) in ("flower","water"):
                return
            else:
                self.parentJerooga.setState(*potentialCoordinate, "flower")
        self.parentJerooga.updateWindow()
        
        
    def give(self, relativeDirection = "ahead"):
        if self.flowers > 0:
            otherJeroo = self.parentJerooga.getJeroo(*self.getInRDirection(relativeDirection))
            if otherJeroo != None:
                otherJeroo.giveFlowers()
                self.flowers -= 1
            
        self.parentJerooga.updateWindow()

    def turn(self, relativeDirection):
        relativeDirection = relativeDirection.lower()
        if relativeDirection == "right" or relativeDirection == 'r':
            self.direction = cardinalDirections[(cardinalDirections.index(self.direction) + 1) % 4]
        elif relativeDirection == "left" or relativeDirection == 'l':
            self.direction = cardinalDirections[(cardinalDirections.index(self.direction) + 1) % 4]
        
        self.parentJerooga.updateWindow()

    # Boolean Methods (partially by Xæch "BooleanMaster" McKenzie)
    
    def hasFlower(self):
        return self.flowers > 0
    
    def isFacing(self, direction):
        return self.direction == direction
    
    def isOnFlower(self):
        return self.parentJerooga.getState(self.blockX, self.blockY) == "flower"
    
    def isFlower(self):
        if self.direction == "N":
            self.parentJerooga.getState(self.blockX, self.blockY-1) == "flower"
        elif self.direction == "E":
            self.parentJerooga.getState(self.blockX+1, self.blockY) == "flower"
        elif self.direction == "S":
            self.parentJerooga.getState(self.blockX, self.blockY+1) == "flower"
        else:
            self.parentJerooga.getState(self.blockX-1, self.blockY) == "flower"
    
    def isJerooDrowned(self):
        if self.parentJerooga.getState(self.blockX, self.blockY) == "water":
            print("Working")
    
    

    
    








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

cardinalDirections = ['N','E','S','W']