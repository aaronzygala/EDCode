

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
        mov1 = motion.movementVal
        mov2 = currentInput.accelRanges
        return isAngleWithinRange(mov1, mov2)

def check_input(motionVal, inputArray):
    for currentInput in inputArray:
        compare_motions(motionVal, currentInput)

try:
    motionVals = Motion()
    map_all_inputs(possibleInputs)#mapping all the inputs

    while True:
        movementVals = motionVals.get_motion()

        check_input(movementVals, possibleInputs) #every second, check for the current input among all the possible inputs

        movementVals = [] #reset current motion val
        time.sleep(1.0) #sleep for 1 second

except KeyboardInterrupt:
    sys.exit()
    


    
    
    
    
    
    
    

