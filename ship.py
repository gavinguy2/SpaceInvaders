import movable
import bomb

class Ship(movable.Movable):

    def __init__(self, x, y, worldWidth, worldHeight, dx, dy):
        movable.Movable.__init__(self, x, y, 35, 35, worldWidth, worldHeight, dx, dy)
        self.mIsBottomRow = False

    def getIsBottomRow(self):
        return self.mIsBottomRow

    def setIsBottomRow(self, value):
        self.mIsBottomRow = value

    def fire(self):
        b = bomb.Bomb(self.mX + self.mWidth/2, self.mY + (self.mHeight + 1), self.mWorldWidth, self.mWorldHeight)
        return b
