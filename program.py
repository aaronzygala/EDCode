

from MPU9250 import *
import time
import sys
import math
from motion import Motion
from input import Input

left = Input("Left")
right = Input("Right")
up = Input("Up")
down = Input("Down")
movementVals = []

def isVelWithinRange(gyroValCompare, gyroValMovement):
    minRange = 0;
    maxRange = 0;
    if(gyroValCompare > 0):
        if(gyroValCompare > 1000):
            maxRange = gyroValCompare + 500
            minRange = gyroValCompare - 500
        elif(gyroValCompare <= 1000 and gyroValCompare > 500):
            maxRange = gyroValCompare + 100
            minRange = gyroValCompare - 100
        elif(gyroValCompare <= 500 and gyroValCompare > 100):
            maxRange = gyroValCompare + 50
            minRange = gyroValCompare - 50
        elif(gyroValCompare <= 100):
            maxRange = gyroValCompare + 10
            minRange = gyroValCompare - 10
    else:
        if(gyroValCompare < -1000):
            minRange = gyroValCompare + 500
            maxRange = gyroValCompare - 500
        elif(gyroValCompare >= -1000 and gyroValCompare < -500):
            minRange = gyroValCompare + 100
            maxRange = gyroValCompare - 100
        elif(gyroValCompare >= -500 and gyroValCompare < -100):
            minRange = gyroValCompare + 50
            maxRange = gyroValCompare - 50
        elif(gyroValCompare >= -100):
            minRange = gyroValCompare + 10
            maxRange = gyroValCompare - 10
            
    return (gyroValMovement - minRange) * (gyroValMovement - maxRange) <= 0

def isAngleWithinRange(accelValA, accelValB):
    minRange = accelValA*100 - 5
    maxRange = accelValA*100 + 5
    return (accelValB * 100 - minRange) * (accelValB * 100 - maxRange) <= 0

    
try:
    motionVals = Motion()

    right.movementVal = motionVals.map_input(right.movementVal, right.inputName)
    left.movementVal = motionVals.map_input(left.movementVal, left.inputName)
    up.movementVal = motionVals.map_input(up.movementVal, up.inputName)
    down.movementVal = motionVals.map_input(down.movementVal, down.inputName)

    while True:
        movementVals = motionVals.get_motion()
         
        movementVals = []
        time.sleep(1.0) #sleep for 1 second

except KeyboardInterrupt:
    sys.exit()
    

    
    
    
    
    
    
    

