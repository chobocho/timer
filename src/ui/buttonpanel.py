import wx

WINDOW_SIZE = 480

class ButtonPanel(wx.Panel):
    def __init__(self, *args, parent_, cbtimer_, **kw):
        super(ButtonPanel, self).__init__(*args, **kw)
        self.parent = parent_
        self.cbtimer = cbtimer_
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self._initButton()

    def _initButton(self):
        self.buttonList = []
        sizer = wx.BoxSizer(wx.VERTICAL)

        #
        nameBox = wx.BoxSizer(wx.HORIZONTAL)

        self.lblTimerName = wx.StaticText(self, style = wx.ALIGN_BOTTOM,label="Timer name", size=(80,28))
        nameBox.Add(self.lblTimerName, 0, wx.ALIGN_CENTRE|wx.ALL, 1)

        self.timerName = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, size=(310,25))
        self.timerName.SetValue("")
        nameBox.Add(self.timerName, 1, wx.EXPAND, 1)

        nameBoxClearBtnId = wx.NewId()
        self.nameBoxClearBtn = wx.Button(self, nameBoxClearBtnId, "Clear", size=(50,30))
        self.nameBoxClearBtn.Bind(wx.EVT_BUTTON, self.OnClearTimerName)
        nameBox.Add(self.nameBoxClearBtn, 0, wx.ALIGN_CENTRE|wx.ALL, 1)

        sizer.Add(nameBox, 1, wx.BOTTOM, 1)
        #

        btnBox = wx.BoxSizer(wx.HORIZONTAL)
        self.timeCount = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, size=(30,25))
        self.timeCount.SetValue("15")
        btnBox.Add(self.timeCount, 1, wx.EXPAND, 1)
        self.timeCount.Bind(wx.EVT_TEXT_ENTER, self.OnStartBtn)
        self.buttonList.append(self.timeCount)

        self.lblMin = wx.StaticText(self, style = wx.ALIGN_BOTTOM,label=" Min ", size=(30,28))
        btnBox.Add(self.lblMin, 0, wx.EXPAND, 1)

        startBtnId = wx.NewId()
        self.startBtn = wx.Button(self, startBtnId, "Start", size=(50,30))
        self.startBtn.Bind(wx.EVT_BUTTON, self.OnStartBtn)
        btnBox.Add(self.startBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 1)
        self.buttonList.append(self.startBtn)

        _1MinBtnId = wx.NewId()
        self._1MinBtn = wx.Button(self, _1MinBtnId, "1 min", size=(50,30))
        self._1MinBtn.Bind(wx.EVT_BUTTON, self.OnStart1MinBtn)
        btnBox.Add(self._1MinBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 1)
        self.buttonList.append(self._1MinBtn)

        _5MinBtnId = wx.NewId()
        self._5MinBtn = wx.Button(self, _5MinBtnId, "5 min", size=(50,30))
        self._5MinBtn.Bind(wx.EVT_BUTTON, self.OnStart5MinBtn)
        btnBox.Add(self._5MinBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 1)
        self.buttonList.append(self._5MinBtn)

        _10MinBtnId = wx.NewId()
        self._10MinBtn = wx.Button(self, _10MinBtnId, "10 min", size=(50,30))
        self._10MinBtn.Bind(wx.EVT_BUTTON, self.OnStart10MinBtn)
        btnBox.Add(self._10MinBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 1)
        self.buttonList.append(self._10MinBtn)

        _30MinBtnId = wx.NewId()
        self._30MinBtn = wx.Button(self, _30MinBtnId, "30 min", size=(50,30))
        self._30MinBtn.Bind(wx.EVT_BUTTON, self.OnStart30MinBtn)
        btnBox.Add(self._30MinBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 1)
        self.buttonList.append(self._30MinBtn)

        _45MinBtnId = wx.NewId()
        self._45MinBtn = wx.Button(self, _45MinBtnId, "45 min", size=(50,30))
        self._45MinBtn.Bind(wx.EVT_BUTTON, self.OnStart45MinBtn)
        btnBox.Add(self._45MinBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 1)
        self.buttonList.append(self._45MinBtn)

        _60MinBtnId = wx.NewId()
        self._60MinBtn = wx.Button(self, _60MinBtnId, "60 min", size=(50,30))
        self._60MinBtn.Bind(wx.EVT_BUTTON, self.OnStart60MinBtn)
        btnBox.Add(self._60MinBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 1)
        self.buttonList.append(self._60MinBtn)

        sizer.Add(btnBox, 0, wx.BOTTOM, 1)
        self.SetSizer(sizer)

        self.bntLabel = ""
        self.clickedBtn = None


    def toggleButton(self, enable):
        for btn in self.buttonList:
            btn.Enable(enable)

    def OnStartBtn(self, event): 
        strCount = self.timeCount.GetValue()
        count = 900
        if len(strCount) > 0:
            try:
                count = int(strCount)
                if count > 0:
                    count *= 60
                else:
                   count *= -1
            except:
                print ("Invalid value!")
                return

        self._OnStartBtn(self.startBtn, count)

    def OnStart1MinBtn(self, event):
        self._OnStartBtn(self._1MinBtn, 60)

    def OnStart5MinBtn(self, event):
        self._OnStartBtn(self._5MinBtn, 300)

    def OnStart10MinBtn(self, event):
        self._OnStartBtn(self._10MinBtn, 600)

    def OnStart30MinBtn(self, event):
        self._OnStartBtn(self._30MinBtn, 1800)

    def OnStart45MinBtn(self, event):
        self._OnStartBtn(self._45MinBtn, 2700)
    
    def OnStart60MinBtn(self, event):
        self._OnStartBtn(self._60MinBtn, 3600)

    def OnClearTimerName(self, event):
        self.timerName.SetValue("")

    def _OnStartBtn(self, btn, count=900):    
        btnLabel = btn.GetLabel()
        if "Stop" in btnLabel:
            print("Stop timer!")
            self.timer.Stop()
            self.cbtimer.Stop()
            btn.SetLabel(self.bntLabel)
            self.timeCount.SetValue("15")
            self.clickedBtn = None
            self.toggleButton(True)
        else:
            print("Start timer! " + str(count))
            self.timer.Start(1000)
            self.cbtimer.Start(count)
            btn.SetLabel("Stop")
            self.bntLabel = btnLabel
            self.clickedBtn = btn
            self.timeCount.SetValue(str(int(count/60)))
            self.toggleButton(False)
            btn.Enable(True)

    def _OnStop(self):    
        print("_OnStop timer!")
        self.timer.Stop()
        self.cbtimer.Stop()
        self.clickedBtn.SetLabel(self.bntLabel)
        self.toggleButton(True) 

    def OnTimer(self, event):
        if self.cbtimer.Update() == False:
            self._OnStop()