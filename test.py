from getkey import getkey, keys
from calibrate import calibrate as clb
import sys
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

direction ="forward"
action = "forward_backward"


def forward_steps_frontlegs(leg,step):
    step = step % 12
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
        servo((leg*3)+0,86)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 6:
        servo((leg*3)+0,72)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 7:
        servo((leg*3)+0,58)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 8:
        servo((leg*3)+0,44)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 9:
        servo((leg*3)+0,30)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 10:
        servo((leg*3)+0,15)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 11:
        servo((leg*3)+0,0)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    else:
        print("12 steps, 0-11")

def forward_steps_rearlegs(leg,step):
    step = step % 12
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
        servo((leg*3)+0,14)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 6:
        servo((leg*3)+0,28)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 7:
        servo((leg*3)+0,42)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 8:
        servo((leg*3)+0,56)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 9:
        servo((leg*3)+0,70)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 10:
        servo((leg*3)+0,85)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 11:
        servo((leg*3)+0,100)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    else:
        print("12 steps, 0-11")



def backward_steps_frontlegs(leg,step):
    step = step % 12
    if step == 0:
        servo((leg*3)+0,0)
        servo((leg*3)+1,30)
        servo((leg*3)+2,20)
    elif step == 1:
        servo((leg*3)+0,20)
        servo((leg*3)+1,0)
        servo((leg*3)+2,30)
    elif step == 2:
        servo((leg*3)+0,40)
        servo((leg*3)+1,0)
        servo((leg*3)+2,30)
    elif step == 3:
        servo((leg*3)+0,55)
        servo((leg*3)+1,30)
        servo((leg*3)+2,20)
    elif step == 4:
        servo((leg*3)+0,60)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 5:
        servo((leg*3)+0,60)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 6:
        servo((leg*3)+0,50)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 7:
        servo((leg*3)+0,40)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 8:
        servo((leg*3)+0,30)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 9:
        servo((leg*3)+0,20)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 10:
        servo((leg*3)+0,10)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 11:
        servo((leg*3)+0,0)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    else:
        print("12 steps, 0-11")

def backward_steps_rearlegs(leg,step):
    step = step % 12
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
        servo((leg*3)+0,14)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 6:
        servo((leg*3)+0,28)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 7:
        servo((leg*3)+0,42)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 8:
        servo((leg*3)+0,56)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 9:
        servo((leg*3)+0,70)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 10:
        servo((leg*3)+0,85)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 11:
        servo((leg*3)+0,100)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    else:
        print("12 steps, 0-11")

def make_a_step(step):
    global action
    if action == "forward":
            forward_steps_frontlegs(0,step)
            forward_steps_rearlegs(1,step+3)
            forward_steps_frontlegs(2,step+6)
            forward_steps_rearlegs(3,step+9)

    elif action == "backward":
            backward_steps_rearlegs(0,step+9)
            backward_steps_frontlegs(1,step+6)
            backward_steps_rearlegs(2,step+3)
            backward_steps_frontlegs(3,step)

    elif action == "stay":
            forward_steps_frontlegs(0,7)
            forward_steps_rearlegs(1,7)
            forward_steps_frontlegs(2,7)
            forward_steps_rearlegs(3,7)


def change_direction(direction_forward):
    global direction
    if direction_forward:
        direction="forward"
    else:
        direction="backward"

def change_action(new_action):
    global action
    action = new_action

def action_control_screen():
    global direction
    global action
    print(f"\n  ############################ Spider Settings ############################\n")
    print(f"    Press: u - forward + change direction to forward \n")
    print(f"           d - forward + change direction to backwards \n")
    print(f"           a - turn left \n")
    print(f"           d - turn right \n")
    print(f"           q - forward left \n")
    print(f"           e - forward right \n\n")
    print(f"                Action Now:  {action} \n")
    print(f"                Dir.   Now:  {direction} \n")
    print(f"           space - Stop \n\n")
    print(f"           Q - Exit \n")

test_int = 0

def start_walking(stop):
    global test_int
    global action
    while(True):
        if action=="stay":
            test_int=0
        if direction=="forward":
            test_int+=1
        elif direction=="backward":
            test_int-=1
        make_a_step(test_int)
        time.sleep(0.03)
    
if __name__ == "__main__":

    get_data()
    '''while(True):
       for i in range(1,5):
           x = input()
           leg_step(i,x)'''
    
    change_direction(True)
    stop_moving = False
    moving = threading.Thread(target=start_walking, args= (lambda:stop_moving,))
    moving.start()
    while(True):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        action_control_screen()
        key = getkey()
        

        if key == 'w':
            change_direction(True)
            change_action("forward")
        elif key == 's':
            change_direction(True)
            change_action("backward")
        elif key == 'q':
            change_action("forward_left")
        elif key == 'e':
            change_action("forward_right")
        elif key == 'a':
            change_action("turn_left")
        elif key == 'd':
            change_action("turn_right")
        elif key == " ":
            change_action("stay")
        elif key == "Q":
            stop_moving=True
            moving.join()
            exit()

        time.sleep(0.2)

