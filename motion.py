from MPU9250 import *
import time
import sys
import math

class Motion:

    def __init__(self):
        self.motionVal = []

    def get_motion(self):
        self.motionVal = mpu6050_conv()
        return self.motionVal

    def map_input(self, input):
        test = raw_input("Please map the value you would like to set to " + input.inputName )
        inputVal = self.get_motion()
        input.movementVal = inputVal
        i = 0
        for x in input.accelRanges:  # initialize the ranges for each angle
            x = range(int(input.movementVal[i]) * 100 - 5, int(input.movementVal[i]) * 100 + 5)
            i += 1
        print(str(input.accelRanges))
        return input.movementVal







        
