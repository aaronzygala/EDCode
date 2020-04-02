from MPU9250 import *
import time
import sys
import math

class Input:

    def __init__(self, name):
        self.inputName = name
        self.movementVal = []
        self.accelRanges = []

    def set_ranges(self):
        i = 0
        for x in range(0,3):  # initialize the ranges for each angle
            lowerRange = int(self.movementVal[i] * 100) - 5
            upperRange = int(self.movementVal[i] * 100) + 5
            x = range(lowerRange, upperRange)
            self.accelRanges.append(x)
            i += 1
