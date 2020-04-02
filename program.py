

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
possibleInputs.extend([left, right, up, down, up_left, up_right, down_left, down_right, A, B, X, Y])
defaultInputs = []
defaultInputs.extend([left, right, up, down, up_left, up_right, down_left, down_right]) #normal default controls for joystick don't include A,B,X,Y
def map_all_inputs(inputArray):
    motion_instance = Motion()
    for x in inputArray:
        x.movementVal = motion_instance.map_input(x)
    return
def map_defaults():
    left.set_movement_val([0.34,0.06,1.43])
    right.set_movement_val([-0.40,0.04,1.40])
    up.set_movement_val([-0.04,-0.28,1.45])
    down.set_movement_val([-0.03,0.47,1.38])
    up_left.set_movement_val([0.39,-0.50,1.24])
    up_right.set_movement_val([-0.45,-0.54,1.18])
    down_left.set_movement_val([0.25,0.52,1.32])
    down_right.set_movement_val([-0.32,0.61,1.23])
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
    motOne = motion[0] * 100
    motTwo = motion[1] * 100
    motThree = motion[2] * 100
    if int(motOne) in inputRanges[0] and int(motTwo) in inputRanges[1] and int(motThree) in inputRanges[2]:
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



def defaultMode():
    try:
        motionVals = Motion()
        map_defaults()  # mapping all the inputs

        while True:
            movementVals = motionVals.get_motion()
            printInput = check_input(movementVals, defaultInputs)  # every second, check for the current input among all the possible inputs
            print(printInput)
            movementVals = []  # reset current motion val
            time.sleep(1.0)  # sleep for 1 second
    except KeyboardInterrupt:
        sys.exit()

def mappingMode():
    try:
        motionVals = Motion()
        map_all_inputs(possibleInputs)  # mapping all the inputs

        while True:
            movementVals = motionVals.get_motion()
            printInput = check_input(movementVals, possibleInputs)  # every second, check for the current input among all the possible inputs
            print(printInput)
            movementVals = []  # reset current motion val
            time.sleep(1.0)  # sleep for 1 second
    except KeyboardInterrupt:
        sys.exit()


try:
    choice = input("Enter 1 for the default controls, and 2 for mapping mode: ")
    if choice == 1:
        defaultMode()
    else:
        mappingMode()

except KeyboardInterrupt:
    sys.exit()
    


    
    
    
    
    
    
    

