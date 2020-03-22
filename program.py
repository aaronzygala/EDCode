

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



    
try:
    motionVals = Motion()

    right.movementVal = motionVals.map_input(right.movementVal, right.inputName)
    left.movementVal = motionVals.map_input(left.movementVal, left.inputName)
    up.movementVal = motionVals.map_input(up.movementVal, up.inputName)
    down.movementVal = motionVals.map_input(down.movementVal, down.inputName)

    while True:
        movementVals = motionVals.get_motion()
        if motionVals.compare_motions(right, movementVals):
            print(right.inputName)
        elif motionVals.compare_motions(left, movementVals):
            print(left.inputName)
        elif motionVals.compare_motions(up, movementVals):
            print(up.inputName)
        elif motionVals.compare_motions(down, movementVals):
            print(down.inputName)
        else:
            print("No Input")

        movementVals = []
        time.sleep(1.0) #sleep for 1 second

except KeyboardInterrupt:
    sys.exit()
    

    
    
    
    
    
    
    

