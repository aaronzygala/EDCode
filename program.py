

from MPU9250 import *
import time
import sys
import math
import motion

left = []
right = []
up = []
down = []
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
    test = raw_input("Please input the value you would like to set to Right: ")
    motionVals = Motion()
    right.extend(motionVals)
    print(right)
    
    test = raw_input("Please input the value you would like to set to Left: ")
    motionVals = Motion()
    left.extend(motionVals)
    print(left)

    test = raw_input("Please input the value you would like to set to Up: ")
    motionVals = Motion()
    up.extend(motionVals)
    print(up)

    
    test = raw_input("Please input the value you would like to set to Down: ")
    motionVals = Motion()
    down.extend(motionVals)
    print(down)
    
    while True:
        ax,ay,az,wx,wy,wz = mpu6050_conv()
        
        movementVals.extend((ax,ay,az,wx,wy,wz))
        '''
        print('{}'.format('-'*30))
        print('accel [g]: x = {}, y = {}, z = {}'.format(ax,ay,az))
        print('gyro [dps]:  x = {}, y = {}, z = {}'.format(wx,wy,wz))
        print('{}'.format('-'*30))
        '''
        
        
        if(isAngleWithinRange(down[0], movementVals[0]) and isAngleWithinRange(down[1], movementVals[1])
           and isAngleWithinRange(down[2], movementVals[2]) and isVelWithinRange(down[3],movementVals[3])):
            print ("Down")
        elif(isAngleWithinRange(up[0], movementVals[0]) and isAngleWithinRange(up[1], movementVals[1])
           and isAngleWithinRange(up[2], movementVals[2]) and isVelWithinRange(up[3],movementVals[3])):
            print("Up") 
        elif(isAngleWithinRange(right[0], movementVals[0]) and isAngleWithinRange(right[1], movementVals[1])
           and isAngleWithinRange(right[2], movementVals[2]) and isVelWithinRange(right[4],movementVals[4])):
            print("Right")  
        elif(isAngleWithinRange(left[0], movementVals[0]) and isAngleWithinRange(left[1], movementVals[1])
           and isAngleWithinRange(left[2], movementVals[2]) and isVelWithinRange(left[4],movementVals[4])):
            print("Left")
        else:
            print("Input not found!")
           
        movementVals = []
        time.sleep(1.0) #sleep for 1 second

except KeyboardInterrupt:
    sys.exit()
    

    
    
    
    
    
    
    

