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
        test = raw_input("Please map the value you would like to set to " + inputName )
        inputVal = self.get_motion()
        inputArray = inputVal
        return inputArray






    def compare_motions(self, motion1, motion2):
        mov1 = motion1.movementVal
        mov2 = motion2.movementVal
        if (isAngleWithinRange(mov1[0], mov2[0]) and isAngleWithinRange(mov1[1], mov2[1])
                and isAngleWithinRange(mov1[2], mov2[2]) and isVelWithinRange(mov1[3], mov2[3])):
            return true
        else:
            return false


def isAngleWithinRange(accelValA, accelValB):
    minRange = accelValA * 100 - 5
    maxRange = accelValA * 100 + 5
    return (accelValB * 100 - minRange) * (accelValB * 100 - maxRange) <= 0
def isVelWithinRange(gyroValCompare, gyroValMovement):
    minRange = 0;
    maxRange = 0;
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





        
