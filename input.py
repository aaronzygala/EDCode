from MPU9250 import *
import time
import sys
import math

class Input:

    def __init__(self, name):
        self.inputName = name
        self.movementVal = []
        self.accelRangeX = 0
        self.accelRangeY = 0
        self.accelRangeZ = 0
        self.accelRanges = [self.accelRangeX, self.accelRangeY, self.accelRangeZ]