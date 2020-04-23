import item

class Movable(item.Item):
    
    def __init__(self, x, y, width, height, worldWidth, worldHeight, dX, dY):
        item.Item.__init__(self, x, y, width, height, worldWidth, worldHeight)
        self.mDX = dX
        self.mDY = dY

    def move(self, dt):
        self.mX = self.mX + (dt * self.mDX)
        self.mY = self.mY + (dt * self.mDY)

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY

    def setDX(self, value):
        self.mDX = value

    def setDY(self, value):
        self.mDY = value
