

from MPU9250 import *
import time
import sys
import math
from motion import Motion
from input import Input

left = Input("Left")
right = Input("Right")
up = Input("Up")
up_left = Input("Up-Left")
up_right = Input ("Up-Right")
down = Input("Down")
down_left = Input ("Down-Left")
down_right = Input ("Down-Right")
A = Input("A")
B = Input("B")
X = Input ("X")
Y = Input("Y")
    
try:
    motionVals = Motion()

    right.movementVal = motionVals.map_input(right)
    left.movementVal = motionVals.map_input(left)
    up.movementVal = motionVals.map_input(up)
    down.movementVal = motionVals.map_input(down)

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
    

    
    
    
    
    
    
    

