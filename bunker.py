import item 
class Bunker:
    def __init__(self,x,y,worldwidth,worldheight):
        self.mX = x
        self.mY = y
        self.mWorldWidth = worldwidth
        self.mWorldHeight = worldheight
        self.mItems = []
        #add top row of items
        for i in range(2):
            for j in range(6):
                currentItem = item.Item(x+(15*j),y+(15*i),15,15,self.mWorldWidth, self.mWorldHeight)
                self.mItems.append(currentItem)
        #add left leg of items
        for i in range(3):
            for j in range(2):
                currentItem = item.Item(x+(15*j),y+30+(15*i),15,15,self.mWorldWidth,self.mWorldHeight)
                self.mItems.append(currentItem)
        #add right leg
        for i in range(3):
            for j in range(2):
                currentItem = item.Item(x+60+(15*j),y+30+(15*i),15,15,self.mWorldWidth,self.mWorldHeight)
                self.mItems.append(currentItem)

    def getItems(self):
        return self.mItems

    def setItems(self, newItems):
        self.mItems = newItems

    def draw(self,surface):
        for i in self.mItems:
            if i.isAlive():
                i.draw(surface, (0,255,0))
                
            
        
    
