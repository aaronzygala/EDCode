from MPU9250 import *
import time
import sys
import math

class Motion:

    def __init__(self):
        self.motionVal = [];
    def get_motion(self):
        self.motionVal = mpu6050_conv();
