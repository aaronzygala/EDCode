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
            x = range(input.movementVal[i] * 100 - 5, input.movementVal[i] * 100 + 5)
            i += 1
        return input.movementVal

    def compare_motions(self, motion, currentInput):
        mov1 = motion.movementVal
        mov2 = currentInput.accelRanges
        return isAngleWithinRange(mov1, mov2)

    def check_input(self, motionVal, inputArray):
        for currentInput in inputArray:
            compare_motions(motionVal, currentInput)

def isOverlapping(range1, range2):
    rSet = set(range1)
    rSet.intersect(range2)

def isAngleWithinRange(motion, inputRanges):
    if motion[0] in inputRanges[0] and motion[1] in inputRanges[1] and motion[2] in inputRanges[2]:
        return True
    return False

def isVelWithinRange(gyroValCompare, gyroValMovement):
    minRange = 0
    maxRange = 0
    if (gyroValCompare > 0):
        if (gyroValCompare > 1000):
            maxRange = gyroValCompare + 500
            minRange = gyroValCompare - 500
        elif (gyroValCompare <= 1000 and gyroValCompare > 500):
            maxRange = gyroValCompare + 100
            minRange = gyroValCompare - 100
        elif (gyroValCompare <= 500 and gyroValCompare > 100):
            maxRange = gyroValCompare + 50
            minRange = gyroValCompare - 50
        elif (gyroValCompare <= 100):
            maxRange = gyroValCompare + 10
            minRange = gyroValCompare - 10
    else:
        if (gyroValCompare < -1000):
            minRange = gyroValCompare + 500
            maxRange = gyroValCompare - 500
        elif (gyroValCompare >= -1000 and gyroValCompare < -500):
            minRange = gyroValCompare + 100
            maxRange = gyroValCompare - 100
        elif (gyroValCompare >= -500 and gyroValCompare < -100):
            minRange = gyroValCompare + 50
            maxRange = gyroValCompare - 50
        elif (gyroValCompare >= -100):
            minRange = gyroValCompare + 10
            maxRange = gyroValCompare - 10

    return (gyroValMovement - minRange) * (gyroValMovement - maxRange) <= 0





        
