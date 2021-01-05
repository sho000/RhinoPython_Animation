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

    def bake(self):
        print("bake")
        for circle in self.circles:
            rs.AddCircle(circle.centerPt,circle.radius)

    def draw(self):
        self.Enabled = True
        self.loopFlg = True
        while(self.loopFlg):
            if scriptcontext.escape_test(False):
                self.loopFlg = False
                # self.bake()   # なぜかbake関数は無視される。下記のように書いたら描かれる。謎
                for circle in self.circles:
                    rs.AddCircle(circle.centerPt,circle.radius)
            # print("frameCnt = {}".format(self.frameCnt))
            self.update()
            scriptcontext.doc.ActiveDoc.Views.ActiveView.Redraw()
            self.frameCnt += 1
        self.Enabled = False

    def DrawOverlay(self, e):
        for circle in self.circles:
            # circle
            pt = Rhino.Geometry.Point3d(circle.centerPt[0],circle.centerPt[1],circle.centerPt[2])
            c = Rhino.Geometry.Circle(pt, circle.radius)
            e.Display.DrawCircle(c, System.Drawing.Color.Black)
            # 2dtest
            msg = "{}".format(circle.centerPt)
            e.Display.Draw2dText(msg, System.Drawing.Color.Blue, pt, True, 5, "Arial")

    
    def bake(self):
        pass