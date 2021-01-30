# coding:utf-8
import Rhino
import scriptcontext

class Animation(Rhino.Display.DisplayConduit):
    def __init__(self,setup=None,update=None,draw=None,bake=None,saveImage=None):
        if(setup!=None):
            self.setup = setup
        if(update!=None):
            self.update = update
        if(draw!=None):
            self.draw = draw
        if(bake!=None):
            self.bake = bake
        if(saveImage!=None):
            self.saveImage = saveImage
            
        self.frameCnt = 0
        self.loopFlg = False

        self.setup()
        self.loop()

    def setup(self):
        pass

    def update(self):
        pass
    
    def draw(self,dp):
        pass

    def bake(self):
        pass

    def saveImage(self,frameCnt):
        pass

    def loop(self):
        self.Enabled = True
        self.loopFlg = True
        while(self.loopFlg):
            if scriptcontext.escape_test(False):
                self.loopFlg = False
                self.bake()  
            self.update()
            scriptcontext.doc.ActiveDoc.Views.ActiveView.Redraw()
            self.saveImage(self.frameCnt)
            self.frameCnt += 1
        self.Enabled = False

    def DrawOverlay(self, e):
        dp = e.Display
        self.draw(dp,self.frameCnt)