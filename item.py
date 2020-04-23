# Space Invaders item Class
# Aaron Bray 2018
import pygame

class Item:

    def __init__(self, x, y, width, height, worldWidth, worldHeight):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mWorldWidth = worldWidth
        self.mWorldHeight = worldHeight
        self.mAlive = True
    
    def getX(self):
        return self.mX

    def setX(self, value):
        self.mX = value
    
    def getY(self):
        return self.mY

    def setY(self, value):
        self.mY = value
    
    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def isAlive(self):
        return self.mAlive

    def kill(self):
        self.mAlive = False
    
    def revive(self):
        self.mAlive = True

    def hits(self, item):
        selfRect = pygame.Rect(self.mX,self.mY,self.mWidth,self.mHeight)
        itemRect = pygame.Rect(item.getX(),item.getY(),item.getWidth(),item.getHeight())
        if self.isAlive() and item.isAlive():
            return selfRect.colliderect(itemRect)

    def draw(self, surface, color):
        r = pygame.Rect(self.mX,self.mY, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, color, r, 0)

