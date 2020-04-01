

from MPU9250 import *
import time
import sys
import math
from motion import Motion
from input import Input

#Naming all the inputs
left = Input("Left")
right = Input("Right")
up = Input("Up")
down = Input("Down")
up_left = Input("Up-Left")
up_right = Input ("Up-Right")
down_left = Input ("Down-Left")
down_right = Input ("Down-Right")
A = Input("A")
B = Input("B")
X = Input ("X")
Y = Input("Y")

possibleInputs = []
possibleInputs.extend([left, right, up, down])##, up_left, up_right, down_left, down_right, A, B, X, Y)
def map_all_inputs(inputArray):
    motion_instance = Motion()
    for x in inputArray:
        x.movementVal = motion_instance.map_input(x)
    return

def compare_motions(motion, currentInput):
        mov1 = motion
        mov2 = currentInput.accelRanges
        return isAngleWithinRange(mov1, mov2)

def check_input(motionVal, inputArray):
    rv = "No Input"
    for currentInput in inputArray:
        if compare_motions(motionVal, currentInput):
            rv = currentInput.inputName
    return rv

def isOverlapping(range1, range2):
    rSet = set(range1)
    rSet.intersect(range2)

def isAngleWithinRange(motion, inputRanges):
    print(str(motion[0]) + " AND " + str(inputRanges[0]))
    print(str(motion[1]) + " AND " + str(inputRanges[1]))
    print(str(motion[2]) + " AND " + str(inputRanges[2]))
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
try:
    motionVals = Motion()
    map_all_inputs(possibleInputs)#mapping all the inputs

    while True:
        movementVals = motionVals.get_motion()

        printInput = check_input(movementVals, possibleInputs) #every second, check for the current input among all the possible inputs
        print(printInput)
        movementVals = [] #reset current motion val
        time.sleep(1.0) #sleep for 1 second

except KeyboardInterrupt:
    sys.exit()
    


    
    
    
    
    
    
    

