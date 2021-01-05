import Rhino
import Rhino.Geometry
import scriptcontext
import rhinoscriptsyntax as rs
import System
import random
from Circle import Circle

class MyConduit(Rhino.Display.DisplayConduit):
    def __init__(self):
        self.frameCnt = 0
        self.loopFlg = False
        self.circles = []

    def setup(self):
        for i in range(1):
            circle = Circle()
            self.circles.append(circle)

    def update(self):
        for circle in self.circles:
            circle.setCenterPt()
            circle.setRadius()

    def draw(self):
        self.Enabled = True
        self.loopFlg = True
        while(self.loopFlg):
            if scriptcontext.escape_test(False):
                self.loopFlg = False
            # print("frameCnt = {}".format(self.frameCnt))
            self.update()
            scriptcontext.doc.ActiveDoc.Views.ActiveView.Redraw()
            self.frameCnt += 1
            # rs.Sleep(1)
        self.Enabled = False

    def DrawOverlay(self, e):
        # pt = Rhino.Geometry.Point3d(self.circles[0].centerPt[0],self.circles[0].centerPt[1],self.circles[0].centerPt[2])
        # c = Rhino.Geometry.Circle(pt, self.circles[0].radius)
        # # print(c)
        # e.Display.DrawCircle(c, System.Drawing.Color.Black)
        for circle in self.circles:
            pt = Rhino.Geometry.Point3d(circle.centerPt[0],circle.centerPt[1],circle.centerPt[2])
            c = Rhino.Geometry.Circle(pt, circle.radius)
            e.Display.DrawCircle(c, System.Drawing.Color.Black)

    
    def bake(self):
        pass