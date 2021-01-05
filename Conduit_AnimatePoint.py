import Rhino
import scriptcontext
import rhinoscriptsyntax as rs
import System

class MyConduit(Rhino.Display.DisplayConduit):
    def __init__(self, index, points):
        self.index = index
        self.points = points
    
    def PostDrawObjects(self, e):
        e.Display.DrawPoint(self.points[self.index], System.Drawing.Color.Red)

def DoSomething():
    
    crv_id = rs.GetObject("Select a curve", 4, True, False)
    if not crv_id: return
    
    points = rs.DivideCurve(crv_id, 100, False, True)
    
    conduit = MyConduit(0, points)
    conduit.Enabled = True
    
    for i in xrange(len(points)):
        if scriptcontext.escape_test(False): break
        
        rs.Prompt("Frame {}".format(i))
        
        conduit.index = i
        scriptcontext.doc.Views.ActiveView.Redraw()
        
        rs.Sleep(25)
    
    conduit.Enabled = False

DoSomething()