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

    def isVelWithinRange(self, gyroValCompare, gyroValMovement):
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

    def isAngleWithinRange(self, accelValA, accelValB):
        minRange = accelValA * 100 - 5
        maxRange = accelValA * 100 + 5
        return (accelValB * 100 - minRange) * (accelValB * 100 - maxRange) <= 0


    def compare_motions(self, motion1, motion2):
        if (isAngleWithinRange(motion1[0], motion2[0]) and isAngleWithinRange(motion1[1], motion2[1])
                and isAngleWithinRange(motion1[2], motion2[2]) and isVelWithinRange(motion1[3], motion2[3])):
            return true
        else:
            return false





        
