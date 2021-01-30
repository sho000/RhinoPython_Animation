# coding:utf-8
import Rhino
import rhinoscriptsyntax as rs
import scriptcontext
from Animation import Animation
from Circle import Circle


def setup():
    for i in range(1):
        circle = Circle()
        circles.append(circle)

def update():
    for circle in circles:
        circle.setCenterPt(-3000,3000)
        circle.setRadius(300,1200)

def draw(dp,frameCnt):
    print("frameCnt = {}".format(frameCnt))
    for circle in circles:
        # dynamic circle
        pt = Rhino.Geometry.Point3d(circle.pt[0],circle.pt[1],circle.pt[2])
        c = Rhino.Geometry.Circle(pt, circle.r)
        dp.DrawCircle(c, rs.CreateColor(255,0,0))
        # dynamic 2d text
        msg = "{}".format(circle.pt)
        dp.Draw2dText(msg, rs.CreateColor(0,0,255), pt, True, 5, "Arial")

def bake():
    pass
    # for circle in circles:
    #     rs.AddCircle(circle.pt, circle.r)

def saveImage(frameCnt):
    pass
    # bitmap = scriptcontext.doc.ActiveDoc.Views.ActiveView.CaptureToBitmap(True,True,True)
    # bitmap.Save("image/image{}.png".format(frameCnt))

if(__name__ == "__main__"):
    circles = []
    conduit = Animation(setup,update,draw,bake,saveImage)