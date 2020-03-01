import wx
import math
import sys
sys.path.insert(0,'..')

from cbtimer.observer import Observer

WINDOW_SIZE = 480

class TimerPanel(wx.Panel, Observer):
    def __init__(self, *args, parent_, **kw):
        super(TimerPanel, self).__init__(*args, **kw)
        self.parent = parent_
        self._initValue()
        self._initUi()
    
    def _initValue(self):
        '''range 0-360'''
        self._value = 0
        self._endCount = 0
    
    def _initUi(self):
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
    def OnPaint(self, event):   
        dc = wx.AutoBufferedPaintDC(self)
        self.OnDrawTimer(dc)
       
    def OnTimer(self, value):
        self._value = value
        dc = wx.BufferedDC(wx.ClientDC(self))
        self.OnDrawTimer(dc)
       
    def OnDrawInitTimer(self, endCount):
        self._value = 0
        self._endCount = endCount
        dc = wx.BufferedDC(wx.ClientDC(self))
        self.OnDrawTimer(dc)
        
    def OnDrawTimer(self, dc):
        w, h = self.GetClientSize()
        if (w > h): 
          r = h / 6 
        else: 
          r = w / 6
        dc.Clear()
        dc.SetPen(wx.Pen(wx.RED, r))
        dc.DrawCircle(w/2, h/2, r*2)
        
        gc = wx.GraphicsContext.Create(dc)
        start = math.radians(270)
        self.max = 360
        self.min = 0

        arcStep = 0
        if (self._endCount > 0):
            current = 360 * self._value / self._endCount
            arcStep = 360 / (self.max - self.min) * current
        end = math.radians(270+arcStep)
        path = gc.CreatePath()
        path.AddArc(w/2, h/2, r*2, start, end, True)
        pen = wx.Pen('#F0F0F0', r*1.1)
        pen.SetCap(wx.CAP_BUTT)
        gc.SetPen(pen)
        gc.SetBrush(wx.Brush('#F0F0F0', wx.TRANSPARENT))
        gc.DrawPath(path)
        self._OnDrawLeftTime(dc, w/2, h/2, r*0.9)
        
    def _OnDrawLeftTime(self, dc, x, y, fontSize):
        font = wx.Font(fontSize, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        dc.SetFont(font) 
        leftTime = str(self._endCount-self._value)
        dc.DrawText(leftTime, x - (fontSize * len(leftTime)*0.4), (y - fontSize*0.6)) 

    def OnSize(self, event):
        event.Skip()
        self.Refresh()    

    def OnUpdate(self, count):
        self.OnTimer(count)

    def OnStart(self, endCount):
        self.OnDrawInitTimer(endCount)

    def OnStop(self, ):
        print("OnStop " + str(self._value) + " " + str(self._endCount))
        pressStopBtn = self._value < self._endCount
        self.OnDrawInitTimer(0)
        if pressStopBtn == False:
            self.parent.OnWindowSizeUp()
