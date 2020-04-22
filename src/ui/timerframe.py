import wx
from ui.timerpanel import *
from ui.buttonpanel import *
from ui.timermenu import * 
from cbtimer.cbtimer import *
import time

WINDOW_SIZE = 480

class TimerFrame(wx.Frame):
    def __init__(self, *args, version, **kw):
        super(TimerFrame, self).__init__(*args, **kw)
    
        self.version = version

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.timerPanel = TimerPanel(self, parent_=self)    

        cbtimer = CBTimer(self.timerPanel)
        self.buttonPanel = ButtonPanel(self, parent_=self, cbtimer_=cbtimer, size=(WINDOW_SIZE, 70))    
        sizer.Add(self.buttonPanel, 0, wx.EXPAND, 1)

        sizer.Add(self.timerPanel, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self._addMenubar()

    def _addMenubar(self):
        self.menu = TimerMenu(self)

    def OnWindowSizeUp(self):
        self.ToggleWindowStyle(wx.STAY_ON_TOP)
        self.Maximize()
        self.OnShowMessasgeBox(self.version, 'Timer expired!')
        self.ToggleWindowStyle(wx.STAY_ON_TOP)
        self.Maximize(maximize=False)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        title = 'About'
        msg = self.version+'\nhttp://chobocho.com'
        self.OnShowMessasgeBox(title, msg)

    def OnShowMessasgeBox(self, title, msg):
        wx.MessageBox(msg, title, wx.OK | wx.ICON_INFORMATION)