# coding:utf-8
import Rhino
import rhinoscriptsyntax as rs
import scriptcontext
import random
from Animation import Animation
from Box import Box

def setup():
    for i in range(100):
        box = Box()
        boxes.append(box)

def update():
    for box in boxes:
        x = random.uniform(-1000,1000)
        y = random.uniform(-1000,1000)
        z = random.uniform(-1000,1000)
        box.pt = [x,y,z]
        box.w = random.uniform(10,300)
        box.d = random.uniform(10,300)
        box.h = random.uniform(10,300)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        box.color = [r,g,b]
        box.setCorners()

def draw(dp,frameCnt,bboxes):
    # print("frameCnt = {}".format(frameCnt))
    for box in boxes:
        corners = rs.coerce3dpointlist(box.corners, True)
        brep = Rhino.Geometry.Brep.CreateFromBox(corners)
        bbox = brep.GetBoundingBox(True)
        bboxes.append(bbox)
        mat = Rhino.Display.DisplayMaterial()
        mat.Diffuse = rs.CreateColor(box.color)
        mat.Transparency = 0.2
        dp.DrawBrepShaded(brep, mat)  
        # dp.DrawBrepWires(brep,rs.CreateColor(box.color))

def bake():
    print("bake")

def saveImage(frameCnt):
    pass
    # bitmap = scriptcontext.doc.ActiveDoc.Views.ActiveView.CaptureToBitmap(True,True,True)
    # bitmap.Save("image/image{}.png".format(frameCnt))

if(__name__ == "__main__"):
    boxes = []
    animation = Animation(setup,update,draw,bake,saveImage)