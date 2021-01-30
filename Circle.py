import random
class Circle(object):
    def __init__(self):
        self.pt = [0,0,0]
        self.r = 1000

    def setCenterPt(self,min,max):
        x = random.uniform(min,max)
        y = random.uniform(min,max)
        z = random.uniform(min,max)
        self.pt = [x,y,z]
    
    def setRadius(self,min,max):
        self.r = random.uniform(min,max)