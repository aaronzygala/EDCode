from MPU9250 import *
import time
import sys
import math

class Input:

    def __init__(self, name):
        self.inputName = name
        self.movementVal = []
        self.accelRangeX = range(0,0)
        self.accelRangeY = range(0,0)
        self.accelRangeZ = range(0,0)
        self.accelRanges = [self.accelRangeX, self.accelRangeY, self.accelRangeZ]