import movable
import bullet
import pygame

class Turret(movable.Movable):

    def __init__(self, worldwidth, worldheight):
        movable.Movable.__init__(self, worldwidth//2, worldheight - 50, 40, 30, worldwidth, worldheight, 0, 0)

    def fire(self):
        b = bullet.Bullet(self.mX+(self.mWidth//2) - 2, self.mY-15, self.mWorldWidth, self.mWorldHeight)
        return b

    def move(self, dt):
        self.mX = self.mX + (self.mDX * dt)
        if self.mX <= 0:
            self.mX = 0
        elif self.mX + self.mWidth >= self.mWorldWidth:
            self.mX = self.mWorldWidth - self.mWidth
    
    
    def draw(self, surface, color):
        r = pygame.Rect(self.mX,self.mY, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, color, r, 0)
        r = pygame.Rect(self.mX + (self.mWidth//2) - 5 ,self.mY - 5, 10, 5)
        pygame.draw.rect(surface, color, r, 0)

