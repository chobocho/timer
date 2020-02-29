import wx
from ui.timerpanel import *
from ui.buttonpanel import *
from ui.timermenu import * 
from cbtimer.cbtimer import *
import time
import random

WINDOW_SIZE = 480

class TimerFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(TimerFrame, self).__init__(*args, **kw)
    
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.timerPanel = TimerPanel(self, parent_=self)    

        cbtimer = CBTimer(self.timerPanel)
        self.buttonPanel = ButtonPanel(self, parent_=self, cbtimer_=cbtimer, size=(WINDOW_SIZE, 50))    
        sizer.Add(self.buttonPanel, 0, wx.EXPAND, 1)

        sizer.Add(self.timerPanel, 1, wx.EXPAND)

        self.SetSizer(sizer)

        self._addMenubar()

    def _addMenubar(self):
        self.menu = TimerMenu(self)

    def OnWindowSizeUp(self):
        delta = random.randint(1,10)
        self.SetSize(WINDOW_SIZE*2+delta, WINDOW_SIZE*2+delta)
        self.ToggleWindowStyle(wx.STAY_ON_TOP)
        time.sleep(0.1)
        self.ToggleWindowStyle(wx.STAY_ON_TOP)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        msg = 'ChoboTimer V0.1\nhttp://chobocho.com'
        title = 'About'
        wx.MessageBox(msg, title, wx.OK | wx.ICON_INFORMATION)