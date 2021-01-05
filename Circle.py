import random
class Circle(object):
    def __init__(self):
        self.centerPt = [0,0,0]
        self.radius = 1000

    def setCenterPt(self):
        x = random.uniform(0,10000)
        y = random.uniform(0,10000)
        z = random.uniform(0,10000)
        self.centerPt = [x,y,z]
    
    def setRadius(self):
        self.radius = random.uniform(300,1200)