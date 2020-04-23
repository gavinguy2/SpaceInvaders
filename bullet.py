import movable

class Bullet(movable.Movable):

    def __init__(self, x, y, worldwidth, worldheight):
        movable.Movable.__init__(self, x, y, 5, 10, worldwidth, worldheight, 0, -525)

    def move(self, dt):
        self.mX = self.mX + (dt * self.mDX)
        self.mY = self.mY + (dt * self.mDY)
        if self.mY <= 0:
            self.kill()

