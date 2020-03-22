from MPU9250 import *
import time
import sys
import math

class Input:

    def __init__(self, name):
        self.inputName = name
        self.movementVal = []