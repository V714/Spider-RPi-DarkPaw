from getkey import getkey, keys
from calibrate import calibrate as clb
import os
import time

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

file_found = False
servo_min = [300] * 12
servo_max = [300] * 12
data = ""

def get_data():
    global file_found
    try:
        f = open("calibrate/servo_data.v7", "r")
        data = f.read()
        f.close()
        data = data.split(".")
        for i in range(12):
            servo_min[0+i] = int(data[1+i])
            servo_max[0+i] = int(data[13+i])
        file_found = True
    except:
        print("No calibration file!")
        exit()


def servo(x,value):
    
    try:
        value = int(value)
    except:
        print("You need to enter a number in range 0-100!")
        pass

    if value>100 or value<0:
        print("Wrong value! (expect 0-100)")
    else:
        pwm.set_pwm(x,0,int((servo_min[x])+((  (servo_max[x]-servo_min[x])/100) * value ) )  )


if __name__ == "__main__":
    get_data()
    while(True):
        servo(2,input('\nEnter value: '))