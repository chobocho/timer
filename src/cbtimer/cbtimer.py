#!/usr/bin/python
#-*- coding: utf-8 -*-
from cbtimer.cbtimerinterface import CBTimerInterface

class CBTimer(CBTimerInterface):
    def __init__(self, observer):
        self.observer= observer

    def Start(self, endCount):
        print("Start")
        self.count = endCount
        self.currentCount = 0
        if (self.observer != None):
            self.observer.OnStart(self.count)

    def Stop(self, ):
        print("Stop")
        if (self.observer != None):
            self.observer.OnStop()

    def Pause(self, ):
        print("Pause")
        if (self.observer != None):
            self.observer.OnPause()

    def Resume(self, ):
        print("Resume")
        if (self.observer != None):
            self.observer.OnResume()

    def Update(self):
        self.currentCount += 1
        print("Update " + str(self.currentCount))
        if (self.observer != None):
            self.observer.OnUpdate(self.currentCount)
        if (self.count <= self.currentCount):
            return False
        return True