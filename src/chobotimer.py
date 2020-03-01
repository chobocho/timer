import wx
from ui.timerframe import *

SW_TITLE = "ChoboTimer V0.14"
WINDOW_SIZE = 480

def main(): 
    app = wx.App()
    frm = TimerFrame(None, version=SW_TITLE, title=SW_TITLE, size=(WINDOW_SIZE,WINDOW_SIZE))
    frm.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()