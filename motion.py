from MPU9250 import *
import time
import sys
import math

class motion:
    def __init__(self):
        self.motionVals = mpu6050_conv()
        print ("test")
