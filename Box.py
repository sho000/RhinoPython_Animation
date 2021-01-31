# coding:utf-8
class Box():

    def __init__(self,pt=[0,0,0],w=1000,d=1000,h=1000,color=[0,0,0]):
        self.pt = pt
        self.w = w
        self.d = d
        self.h = h
        self.color = color 
        self.corners = []

        self.setCorners()
    
    def setCorners(self):
        self.corners = [
            [-self.w/2 + self.pt[0], -self.d/2 + self.pt[1], -self.h/2 + self.pt[2]],
            [ self.w/2 + self.pt[0], -self.d/2 + self.pt[1], -self.h/2 + self.pt[2]],
            [ self.w/2 + self.pt[0],  self.d/2 + self.pt[1], -self.h/2 + self.pt[2]],
            [-self.w/2 + self.pt[0],  self.d/2 + self.pt[1], -self.h/2 + self.pt[2]],
            [-self.w/2 + self.pt[0], -self.d/2 + self.pt[1],  self.h/2 + self.pt[2]],
            [ self.w/2 + self.pt[0], -self.d/2 + self.pt[1],  self.h/2 + self.pt[2]],
            [ self.w/2 + self.pt[0],  self.d/2 + self.pt[1],  self.h/2 + self.pt[2]],
            [-self.w/2 + self.pt[0],  self.d/2 + self.pt[1],  self.h/2 + self.pt[2]]
        ]


