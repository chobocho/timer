import unittest
import sys
sys.path.insert(0,'..')
sys.path.insert(1,'../ui')
sys.path.insert(2,'../cbtimer')
from cbtimer.cbtimer import *
from cbtimer.observer import *

class CBTimerTest(unittest.TestCase):
    def setUp(self):
        self.observer = Observer()
        self.cbTimer = CBTimer(self.observer)

    def tearDown(self):
        pass

    def test_start(self):
        self.cbTimer.Start(90)

    def test_stop(self):
        self.cbTimer.Stop()

    def test_update(self):
        self.cbTimer.Start(2)
        assert(self.cbTimer.Update() == True)
        assert(self.cbTimer.Update() == False)
        assert(self.cbTimer.Update() == False)

if __name__ == '__main__':
    unittest.main()