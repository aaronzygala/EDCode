from MPU9250 import *
import time
import sys
import math

class motion:
    motionVals = ax, ay, az, wx, wy, wz;
    def __init__(self):
        self.motionVals = mpu6050_conv()
