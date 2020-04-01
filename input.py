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

    def set_ranges(self):
        i = 0
        for x in input.accelRanges:  # initialize the ranges for each angle
            lowerRange = int(input.movementVal[i]) * 100 - 5
            upperRange = int(input.movementVal[i]) * 100 + 5
            x = range(lowerRange, upperRange)
            i += 1
        print(int(input.movementVal[i]) * 100 - 5)
        print(int(input.movementVal[i]) * 100 + 5)
        print(input.accelRanges)