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
        self.accelRanges = []

    def set_ranges(self):
        i = 0
        for x in self.accelRanges:  # initialize the ranges for each angle
            lowerRange = int(self.movementVal[i]) * 100 - 5
            upperRange = int(self.movementVal[i]) * 100 + 5
            self.accelRanges[i] = range(lowerRange, upperRange)
            i += 1
        print(int(self.movementVal[i]) * 100 - 5)
        print(int(self.movementVal[i]) * 100 + 5)
        print(self.accelRanges)