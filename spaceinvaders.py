import pygame
import bullet
import bunker
import turret
import bomb
import ship
import random

class SpaceInvaders:

    def __init__(self, worldwidth, worldheight):
        self.mWorldWidth = worldwidth
        self.mWorldHeight = worldheight
        self.mTurret = turret.Turret(self.mWorldWidth, self.mWorldHeight)
        self.mBunkers = []
        self.mBullet = None
        self.mBombs = []
        self.mLives = 3
        self.mScore = 0
        self.mFont = pygame.font.SysFont('arial',30,True)
        self.mText =""
        self.mShipStartHeight = 40
        self.mShipStartSpeed = 8
        self.mDisplayGameOverText = False
        self.mFireRate = 1

        for i in range(4):
            bunk = bunker.Bunker((self.mWorldWidth//4) - 60 + i * 140, self.mWorldHeight - 150, self.mWorldWidth, self.mWorldHeight)
            self.mBunkers.append(bunk)

        self.mShips = []
        for i in range(11):
            shipColumn = []
            for j in range(5):
                s = ship.Ship(40 + i*50, self.mShipStartHeight + (j * 50), self.mWorldWidth, self.mWorldHeight, self.mShipStartSpeed, 0)
                shipColumn.append(s)
            self.mShips.append(shipColumn)

    def countShips(self):
        count = 0
        for ships in self.mShips:
            count += len(ships)
        return count

    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def getTurret(self):
        return self.mTurret

    def getShips(self):
        return self.mShips

    def getBunkers(self):
        return self.mBunkers

    def findBottomRowShips(self):
        for i in range(11):
            if len(self.mShips[i]) > 0:
                highest = 0
                lowestIndex = 0
                for j in range(len(self.mShips[i])):
                    if self.mShips[i][j].isAlive() and self.mShips[i][j].getY() >= highest:
                        highest = self.mShips[i][j].getY()
                        lowestIndex = j
                self.mShips[i][lowestIndex].setIsBottomRow(True)

    def moveTurretLeft(self):
        self.mTurret.setDX(-130)

    def moveTurretRight(self):
        self.mTurret.setDX(130)

    def stopTurret(self):
        self.mTurret.setDX(0)

    def fireTurret(self):
        if self.mBullet is None:
            b = self.mTurret.fire()
            self.mBullet = b

    def collideBombsAndBunkers(self):
        for bunker in self.mBunkers:
            bItems = bunker.getItems()
            for item in bItems:
                for bomb in self.mBombs:
                    if bomb.hits(item):
                        bomb.kill()
                        item.kill()

    def collideBulletAndBunkers(self):
        for bunker in self.mBunkers:
            bItems = bunker.getItems()
            for item in bItems:
                if self.mBullet is not None and self.mBullet.hits(item):
                    item.kill()
                    self.mBullet.kill()
                    self.mBullet = None

    def collideShipsAndBunkers(self):
        for bunker in self.mBunkers:
            bItems = bunker.getItems()
            for item in bItems:
                for ships in self.mShips:
                    for ship in ships:
                        if ship.hits(item):
                            item.kill()

    def collideBulletAndShips(self):
        for i in range(11):
            ships = self.mShips[i]
            if len(ships) > 0:
                for ship in ships:
                    if self.mBullet is not None and self.mBullet.hits(ship):
                        ship.kill()
                        for j in range(11):
                            for k in range(len(self.mShips[j])):
                                currentDX = self.mShips[j][k].getDX()
                                self.mShips[j][k].setDX(currentDX * 1.05)
                        self.mBullet.kill()
                        self.mBullet = None
                        self.mScore += 10
                        if self.mScore % 1000 == 0:
                            self.mLives += 1

    def collideBombsAndTurret(self):
        for bomb in self.mBombs:
            if bomb.hits(self.mTurret):
                if self.mLives >= 1:
                    self.mLives -=1
                    self.mTurret.setX(10)
                    self.mBombs = []
                    bomb.kill()
                if self.mLives == 0:
                    self.mTurret.kill()
                    bomb.kill()

    def collideBombsAndBullets(self):
        for bomb in self.mBombs:
            if self.mBullet is not None:
                if bomb.hits(self.mBullet):
                    self.mBullet.kill()
                    self.mBullet = None
                    bomb.kill()

    def collideAll(self):
        self.collideBombsAndBunkers()
        self.collideBulletAndShips()
        self.collideBulletAndBunkers()
        self.collideBombsAndBullets()
        self.collideBombsAndTurret()
        self.collideShipsAndBunkers()

    def moveShips(self, dt):
        for ships in self.mShips:
            for ship in ships:
                ship.move(dt)
                if ship.getY() + ship.getHeight() >= self.mTurret.getY():
                    self.gameOver()
        for i in range(11):
            if len(self.mShips[i]) > 0:
                ship = self.mShips[i][0]
                if (ship.getX() + ship.getWidth() >= self.mWorldWidth) or (ship.getX() <= 0):
                    for j in range(11):
                        for k in range(len(self.mShips[j])):
                            currentY = self.mShips[j][k].getY()
                            currentDX = self.mShips[j][k].getDX()
                            self.mShips[j][k].setY(currentY + 10)
                            self.mShips[j][k].setDX(currentDX * -1.02)
                            self.mShips[j][k].move(.0166)
                
    def moveAll(self, dt):
        for bomb in self.mBombs:
            bomb.move(dt)
        self.moveShips(dt)
        if self.mBullet is not None:
            self.mBullet.move(dt)
        self.mTurret.move(dt)
        self.stopTurret()

    def fireShips(self):
        for ships in self.mShips:
            for ship in ships:
                if ship.getIsBottomRow():
                    r = random.randrange(70 * (1 + (self.countShips()//self.mFireRate)))
                    if r == 1:
                        b = ship.fire()
                        self.mBombs.append(b)
                        
    def reset(self):
        self.mShipStartHeight += 20
        self.mFireRate *= 1.03
        if self.mShipStartHeight > 120:
            self.mShipStartHeight = 100
            self.mShipStartSpeed += 1
        self.mBombs = []
        self.mShips = []
        for i in range(11):
            shipColumn = []
            for j in range(5):
                s = ship.Ship(40 + i*50, self.mShipStartHeight + (j * 50), self.mWorldWidth, self.mWorldHeight, self.mShipStartSpeed, 0)
                shipColumn.append(s)
            self.mShips.append(shipColumn)

        

    def gameOver(self):
        self.mDisplayGameOverText = True

    def removeDead(self):
        newShips = []
        newBombs = []
        for i in range(11):
            newShips.append([])
        for i in range(11):
            for j in range(len(self.mShips[i])):
                if self.mShips[i][j].isAlive():
                    newShips[i].append(self.mShips[i][j])
        for bomb in self.mBombs:
            if bomb.isAlive():
                newBombs.append(bomb)
        for bunker in self.mBunkers:
            newItems = []
            bItems = bunker.getItems()
            for item in bItems:
                if item.isAlive():
                    newItems.append(item)
            bunker.setItems(newItems)
        if self.mBullet is not None and not self.mBullet.isAlive():
            self.mBullet = None
        elif not self.mTurret.isAlive() and self.mLives == 0:
            self.gameOver()
        self.mShips = newShips
        if self.countShips() == 0:
            self.reset()
        self.mBombs = newBombs

    def refresh(self, dt):
        if not self.mDisplayGameOverText:
            self.findBottomRowShips()
            self.fireShips()
        if not self.mDisplayGameOverText:
            self.moveAll(dt)
        if not self.mDisplayGameOverText:
            self.collideAll()
        if not self.mDisplayGameOverText:
            self.removeDead()

    def draw(self, surface):
        if self.mDisplayGameOverText:
            rect = (0, 0, self.mWorldWidth, self.mWorldHeight)
            pygame.draw.rect(surface, (0,0,0), rect, 0)
            gameOver ="Game Over"
            self.mFont = pygame.font.SysFont('arial',100,True)
            textsurface = self.mFont.render(gameOver,True, (255,255,255))
            surface.blit(textsurface,(self.mWorldWidth//5, self.mWorldHeight//3))
            yourScore = "Your Score: " + str(self.mScore)
            self.mFont = pygame.font.SysFont('arial',50,True)
            textsurface = self.mFont.render(yourScore, True, (255,255,255))
            surface.blit(textsurface, (self.mWorldWidth//3.5, self.mWorldHeight//3 + 75))
        else:
            rect = (0, 0, self.mWorldWidth, self.mWorldHeight)
            pygame.draw.rect(surface, (0,0,0), rect, 0)
            self.mText ="Player Lives: " + str(self.mLives)
            textsurface = self.mFont.render(self.mText,True, (255,255,255))
            surface.blit(textsurface,(10,10))
            playerScore ="Score: " + str(self.mScore)
            textsurface = self.mFont.render(playerScore,True, (255,255,255))
            surface.blit(textsurface,(530,10))
            for ships in self.mShips:
                for ship in ships:
                    ship.draw(surface, (255,255,255))
            for bomb in self.mBombs:
                bomb.draw(surface, (255,255,255))
            for bunker in self.mBunkers:
                bunker.draw(surface)
            if self.mBullet is not None:
                self.mBullet.draw(surface, (0,255,0))
            self.mTurret.draw(surface, (0,255,0))
