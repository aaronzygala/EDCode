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
    def map_input(self, inputArray, inputName):
        test = raw_input("Please map the value you would like to set to: " + inputName )
        inputVal = self.get_motion()
        inputArray = inputVal
        return inputArray

    #def compare_motions(self, motion1, motion2):




        
