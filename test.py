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


def leg(which,position="none"):
    if int(which) == 1:
        which = [0,1,2]
    elif int(which) == 2:
        which = [3,4,5]
    elif int(which) == 3:
        which = [6,7,8]
    elif int(which) == 4:
        which = [9,10,11]
    else:
        print("Wrong value, expected number in range 1-4!")
        time.sleep(1.5)

    if position == "none":
        pass
    elif position == "default":
        servo(which[0],50)
        servo(which[1],20)
        servo(which[2],15)
    elif position == "u":
        servo(which[1],100)
    elif position == "d":
        servo(which[1],0)
    elif position == "o":
        servo(which[0],100)
    elif position == "c":
        servo(which[0],10)
    elif position == "f":
        servo(which[2],100)
    elif position == "n":
        servo(which[2],0)
    elif position == "h":
        servo(which[0],50)


def move_leg(which,where="none"):
    leg=which
    if int(which) == 1:
        which = [0,1,2]
    elif int(which) == 2:
        which = [3,4,5]
    elif int(which) == 3:
        which = [6,7,8]
    elif int(which) == 4:
        which = [9,10,11]
    else:
        print("Wrong value, expected number in range 1-4!")
        time.sleep(1.5)

    if where == "none":
        pass
    elif where == "default":
            servo(which[0],50)
            servo(which[1],30)
            servo(which[2],20)
    elif where == "forward":
        if leg == 2 or leg == 4:
            servo(which[0],100)
            time.sleep(0.2)
            servo(which[1],0)
            servo(which[2],100)
            time.sleep(0.1)
            servo(which[0],0)
            time.sleep(0.1)
            servo(which[1],50)
            servo(which[2],50)
            time.sleep(0.1)
            servo(which[0],50)
        else:
            servo(which[0],0)
            time.sleep(0.2)
            servo(which[1],0)
            servo(which[2],100)
            time.sleep(0.1)
            servo(which[0],100)
            time.sleep(0.1)
            servo(which[1],50)
            servo(which[2],50)
            time.sleep(0.1)
            servo(which[0],50)


def spider_pos(position="none"):
    all_legs = [1,2,3,4]
    
    if position == "none":
        pass

    elif position == "default":
        for i in all_legs:
            leg(i,"default")

    elif position == "up":
        for i in all_legs:
            leg(i,"u")

    elif position == "down":
        for i in all_legs:
            leg(i,"d")

    elif position == "floor":
        leg(1,"d")
        leg(2,"u")
        leg(3,"d")
        leg(4,"u")

    elif position == "ceiling":
        leg(1,"u")
        leg(2,"d")
        leg(3,"u")
        leg(4,"d")

    elif position =="show_leg":
        leg(2,"d")
        leg(2,"f")
        time.sleep(0.3)
        leg(2,"c")
        time.sleep(0.3)
        leg(2,"n")
        leg(2,"u")
        leg(3,"d")
        time.sleep(0.5)
        leg(3,"f")
        leg(3,"o")
        leg(4,"d")
        time.sleep(0.5)
        leg(4,"o")
        leg(4,"f")
        leg(1,"f")
        time.sleep(1.5)
        leg(1,"d")
        leg(1,"o")
        time.sleep(1)
        servo(0,30)
        time.sleep(0.4)
        servo(0,100)
        time.sleep(0.4)
        servo(0,30)
        time.sleep(0.4)
        servo(0,100)


def leg_menu_screen(leg):
    print(f"\n  ############################ Spider Settings ############################\n")
    print(f"    Press: u - Up \n")
    print(f"           d - Down \n")
    print(f"           o - Open \n")
    print(f"           c - Close \n")
    print(f"           f - Far \n")
    print(f"           n - Near \n\n")
    print(f"                Leg  {leg} \n")
    print(f"           A - Previous Leg \n")
    print(f"           D - Next Leg \n\n")
    print(f"           Q - Exit \n")


def leg_test_menu():
    print("Entering test...")
    actual_leg=1
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    leg_menu_screen(actual_leg)

    while(True):
        key = getkey()

        if key == 'u':
            leg(actual_leg,"u")
            os.system('cls' if os.name == 'nt' else 'clear')
            leg_menu_screen(actual_leg)

        elif key == 'd':
            leg(actual_leg,"d")
            os.system('cls' if os.name == 'nt' else 'clear')
            leg_menu_screen(actual_leg)

        elif key == 'o':
            leg(actual_leg,"o")
            os.system('cls' if os.name == 'nt' else 'clear')
            leg_menu_screen(actual_leg)

        elif key == 'c':
            leg(actual_leg,"c")
            os.system('cls' if os.name == 'nt' else 'clear')
            leg_menu_screen(actual_leg)

        elif key == 'f':
            leg(actual_leg,"f")
            os.system('cls' if os.name == 'nt' else 'clear')
            leg_menu_screen(actual_leg)

        elif key == 'n':
            leg(actual_leg,"n")
            os.system('cls' if os.name == 'nt' else 'clear')
            leg_menu_screen(actual_leg)


        elif key == 'A':
            if actual_leg>1:
                actual_leg -= 1

            os.system('cls' if os.name == 'nt' else 'clear')
            leg_menu_screen(actual_leg)

        elif key == 'D':
            if actual_leg<4:
                actual_leg += 1

            os.system('cls' if os.name == 'nt' else 'clear')
            leg_menu_screen(actual_leg)


        elif key == 'Q':
            exit()


def position_menu_screen():
    print(f"\n  ############################ Spider Settings ############################\n")
    print(f"    Press: u - Up \n")
    print(f"           d - Down \n")
    print(f"           f - Floor \n")
    print(f"           c - Ceiling \n")
    print(f"           s - Show Leg \n\n")
    print(f"           Q - Exit \n")


def position_test_menu():

    print("Entering Position Test Menu...")
    spider_pos("default")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    position_menu_screen()

    while(True):
        key = getkey()

        if key == 'u':
            spider_pos("up")
            time.sleep(2)
            spider_pos("default")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            position_menu_screen()

        elif key == 'd':
            spider_pos("down")
            time.sleep(2)
            spider_pos("default")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            position_menu_screen()

        elif key == 'f':
            spider_pos("floor")
            time.sleep(2)
            spider_pos("default")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            position_menu_screen()

        elif key == 'c':
            spider_pos("ceiling")
            time.sleep(2)
            spider_pos("default")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            position_menu_screen()

        elif key == 's':
            spider_pos("show_leg")
            time.sleep(2)
            spider_pos("default")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            position_menu_screen()

        elif key == 'Q':
            exit()


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


        time.sleep(0.2)

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
    spider_pos("default")
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

def keep_alive():
    servo1 = 50
    servo2 = 50
    servo4 = 50
    servo5 = 50
    servo7 = 50
    servo8 = 50
    servo10 = 50
    servo11 = 50

    speed=1    
    while(True):
        servo1 = servo1+rnd.randint(-speed,speed)
        servo2 = servo2+rnd.randint(-speed,speed)
        servo4 = servo4+rnd.randint(-speed,speed)
        servo5 = servo5+rnd.randint(-speed,speed)
        servo7 = servo7+rnd.randint(-speed,speed)
        servo8 = servo8+rnd.randint(-speed,speed)
        servo10 = servo10+rnd.randint(-speed,speed)
        servo11 = servo11+rnd.randint(-speed,speed)


        servo(1,servo1)
        servo(2,servo2)
        servo(4,servo4)
        servo(5,servo5)
        servo(7,servo7)
        servo(8,servo8)
        servo(10,servo10)
        servo(11,servo11)
        time.sleep(0.01)


front_legs=[80,40]
back_legs=[40,80]
any_leg_up=False
leg_up=[False,False,False,False]

def front_step(which):
    if which == 0: 
        leg_up[0]=True
        leg(1,"d")
        leg(1,"f")
        time.sleep(0.1)
        servo(0,100)
        front_legs[0]=100
        leg(1,"u")
        leg(1,"n")
        time.sleep(0.3)
        leg_up[0]=False

    elif which == 1: 
        leg_up[2]=True
        leg(3,"d")
        leg(3,"f")
        time.sleep(0.1)
        servo(6,100)
        front_legs[1]=100
        leg(3,"u")
        leg(3,"n")
        time.sleep(0.3)
        leg_up[2]=False
    any_leg_up=False


def front_step_b(which):
    if which == 0: 
        leg_up[1]=True
        leg(2,"d")
        leg(2,"f")
        time.sleep(0.1)
        servo(3,0)
        back_legs[0]=0
        leg(2,"u")
        leg(2,"n")
        time.sleep(0.3)
        leg_up[1]=False

    elif which == 1: 
        leg_up[3]=True
        leg(4,"d")
        leg(4,"f")
        time.sleep(0.1)
        servo(9,0)
        back_legs[1]=0
        leg(4,"u")
        leg(4,"n")
        time.sleep(0.3)
        leg_up[3]=False
    any_leg_up=False

def stepgo(leg_up,front_legs,back_legs):
    
    if leg_up[0]:servo(0,front_legs[0])
    if leg_up[1]:servo(3,back_legs[0])
    if leg_up[2]:servo(6,front_legs[1])
    if leg_up[3]:servo(9,back_legs[1])
    time.sleep(0.5)

if __name__ == "__main__":

    get_data()
    
    move_forward=True
    spider_pos("up")
    time.sleep(1)
    servo(0,front_legs[0])
    servo(3,back_legs[0])
    servo(6,front_legs[1])
    servo(9,back_legs[1])

    while(move_forward):

        for i in range(len(front_legs)):
            if(front_legs[i]<=0):
                if any_leg_up:
                    pass
                else:
                    any_leg_up=True
                    threading.Thread(target=front_step, args=(i,)).start()
                    
            else:
                if i == 0 and not leg_up[0]:
                    front_legs[i]-=1
                if i == 1 and not leg_up[2]:
                    front_legs[i]-=1

        for i in range(len(back_legs)):
            if(back_legs[i]>=0):
                if any_leg_up:
                    pass
                else:
                    any_leg_up=True
                    threading.Thread(target=front_step_b, args=(i,)).start()
                    
            else:
                if i == 0 and not leg_up[1]:
                    back_legs[i]+=1
                if i == 1 and not leg_up[3]:
                    back_legs[i]+=1


        threading.Thread(target=stepgo,args=(leg_up,front_legs,back_legs,)).start()
