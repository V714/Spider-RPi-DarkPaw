from getkey import getkey, keys
from calibrate import calibrate as clb
import os
import time
import threading
import Adafruit_PCA9685
from mpu6050 import mpu6050
import RPi.GPIO as GPIO
import random as rnd

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

accel = mpu6050(0x68)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
buzzer = GPIO.PWM(12,440)

# RPi Connections: #
#   5 BCM - Light
#  12 BCM - Buzzer

"""

0  1  2    - 1st leg -> v

3  4  5    - 2nd leg -> ^

6  7  8    - 3rd leg <- v

9  10 11   - 4th leg <- ^

|   |  |
|   | 1 far/near 0
|   |
| 1 up/down 0
|
1 open/close 0

"""

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


def eyelight(bool):
    if bool:
        GPIO.output(5,GPIO.HIGH)
    else:
        GPIO.output(5,GPIO.LOW)


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

def accel_menu_screen(x,y,z):
    print(f"\n  ############################ Spider Settings ############################\n")
    print(f"    \n\n\n")
    print(f"           X: {x} \n")
    print(f"           Y: {y} \n")
    print(f"           Z: {z} \n\n\n")
    print(f"           Ctrl+C - Exit \n")


def accel_test_menu():
    print("Entering accelerometer test...")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    rh_legs=50
    lh_legs=50
    front=0

    while(True):
        accelerometer_data = accel.get_accel_data()

        os.system('cls' if os.name == 'nt' else 'clear')
        accel_menu_screen(accelerometer_data['x'],accelerometer_data['y'],accelerometer_data['z'])
        if accelerometer_data['z'] < -4:
            buzzer.start(50)
            buzzer.ChangeFrequency(7)
        else:
            buzzer.stop()


        if accelerometer_data['x'] < -6 and accelerometer_data['y'] > -2 and accelerometer_data['y'] < 2 and accelerometer_data['z'] > -2 and accelerometer_data['z'] < 5:
            front+=1
        else:
            front=0

        if accelerometer_data['y'] > 0.5:
            if lh_legs <=5 or rh_legs >= 95:
                pass
            else:
                lh_legs-=4
                rh_legs+=4
       
        if accelerometer_data['y'] < -0.5 :
            if lh_legs >=95 or rh_legs <= 5:
                pass
            else:
                lh_legs+=4
                rh_legs-=4

        if front > 10:
            buzzer.start(30)
            buzzer.ChangeFrequency(880)
            time.sleep(0.1)
            buzzer.stop()
            time.sleep(0.1)
            buzzer.start(30)
            buzzer.ChangeFrequency(880)
            time.sleep(0.1)
            buzzer.stop()
            leg(3,'c')
            time.sleep(0.2)
            leg(3,'d')
            leg(3,'f')
            time.sleep(0.2)
            leg(3,'default')
            front=0
            time.sleep(0.4)
            buzzer.start(30)
            eyelight(True)
            buzzer.ChangeFrequency(440)
            time.sleep(0.5)
            eyelight(False)
            buzzer.stop()
            time.sleep(0.1)
            eyelight(True)
            time.sleep(0.1)
            eyelight(False)

        
        servo(1,lh_legs)
        servo(4,lh_legs)
        servo(7,rh_legs)
        servo(10,rh_legs)
        time.sleep(0.03)

def init():
    print("Hello world...")
    buzzer.start(50)
    buzzer.ChangeFrequency(3)
    time.sleep(0.7)
    buzzer.stop()
    time.sleep(0.3)
    eyelight(True)
    time.sleep(0.1)
    eyelight(False)
    time.sleep(0.1)
    eyelight(True)
    time.sleep(0.05)
    eyelight(False)
    time.sleep(0.3)
    buzzer.start(30)
    buzzer.ChangeFrequency(440)
    time.sleep(0.1)
    buzzer.stop()
    time.sleep(0.1)
    buzzer.start(30)
    buzzer.ChangeFrequency(880)
    time.sleep(0.4)
    buzzer.stop()
    time.sleep(0.1)
    buzzer.start(30)
    buzzer.ChangeFrequency(698)
    time.sleep(0.1)
    buzzer.stop()

action = "forward"

def leg_stepf(leg,step):
    if step == 0:
        servo((leg*3)+0,0)
        servo((leg*3)+1,30)
        servo((leg*3)+2,20)
    elif step == 1:
        servo((leg*3)+0,33)
        servo((leg*3)+1,0)
        servo((leg*3)+2,30)
    elif step == 2:
        servo((leg*3)+0,67)
        servo((leg*3)+1,0)
        servo((leg*3)+2,30)
    elif step == 3:
        servo((leg*3)+0,90)
        servo((leg*3)+1,30)
        servo((leg*3)+2,20)
    elif step == 4:
        servo((leg*3)+0,100)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 5:
        servo((leg*3)+0,80)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 6:
        servo((leg*3)+0,60)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 7:
        servo((leg*3)+0,40)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 8:
        servo((leg*3)+0,20)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 9:
        servo((leg*3)+0,0)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    else:
        print("10 steps, 0-9")

def leg_stepb(leg,step):
    if step == 0:
        servo((leg*3)+0,100)
        servo((leg*3)+1,30)
        servo((leg*3)+2,20)
    elif step == 1:
        servo((leg*3)+0,67)
        servo((leg*3)+1,0)
        servo((leg*3)+2,30)
    elif step == 2:
        servo((leg*3)+0,33)
        servo((leg*3)+1,0)
        servo((leg*3)+2,30)
    elif step == 3:
        servo((leg*3)+0,10)
        servo((leg*3)+1,30)
        servo((leg*3)+2,20)
    elif step == 4:
        servo((leg*3)+0,0)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 5:
        servo((leg*3)+0,20)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 6:
        servo((leg*3)+0,40)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 7:
        servo((leg*3)+0,60)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 8:
        servo((leg*3)+0,80)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 9:
        servo((leg*3)+0,100)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    else:
        print("8 steps, 0-7")

def leg_step(leg,step):
    new_step = step % 10
    if leg == 0 or leg == 2:
        leg_stepf(leg,new_step)
    else:
        leg_stepb(leg,new_step)


def forward(step):
    global action

    if action == "forward":
        leg_stepf(0,step+0)
        leg_stepb(1,step+2)
        leg_stepf(2,step+4)
        leg_stepb(3,step+6)

    else:
        for i in range(12):
            if i % 3 == 1:
                servo(i,50)
            elif i % 3 == 2:
                servo(i,20)
            elif i % 3 == 0:
                servo(i,15)

if __name__ == "__main__":

    get_data()
    '''while(True):
       for i in range(1,5):
           x = input()
           leg_step(i,x)'''
    test_int = 0
    while(True):
        forward(test_int)
        test_int+=1
        time.sleep(0.2)

