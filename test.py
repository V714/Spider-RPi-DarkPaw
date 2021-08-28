from getkey import getkey, keys
from calibrate import calibrate as clb
import os
import time
import asyncio
import Adafruit_PCA9685
from mpu6050 import mpu6050
import RPi.GPIO as GPIO

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
        for i in which:
            servo(i,50)
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


async def move_leg(which,where="none"):
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
        for i in which:
            servo(i,50)
    elif where == "forward":
        servo(which[0],100)
        await asyncio.sleep(0.4)
        servo(which[1],0)
        servo(which[2],0)
        await asyncio.sleep(0.2)
        servo(which[0],100)
        await asyncio.sleep(0.2)
        servo(which[1],50)
        servo(which[2],50)
        await asyncio.sleep(0.2)
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
            leg(2,'o')
            leg(4,'o')
            time.sleep(0.5)
            leg(1,'c')
            leg(3,'c')
            time.sleep(0.5)
            leg(1,'h')
            leg(3,'h')
            time.sleep(1)
            leg(1,'d')
            leg(1,'f')
            time.sleep(0.2)
            leg(1,'o')
            time.sleep(0.2)
            leg(3,'d')
            leg(3,'f')
            time.sleep(0.2)
            leg(3,'o')
            time.sleep(1)
            leg(2,'d')
            leg(2,'f')
            time.sleep(0.2)
            leg(2,'default')
            time.sleep(0.2)
            leg(4,'d')
            leg(4,'f')
            time.sleep(0.3)
            leg(4,'default')
            front=0
            leg(1,"default")
            leg(3,"default")
            time.sleep(0.7)
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

async def moving():
    task = asyncio.create_task(move_leg(3,'forward'))
    task2 = asyncio.create_task(move_leg(2,'forward'))
    task3 = asyncio.create_task(move_leg(1,'forward'))
    task4 = asyncio.create_task(move_leg(4,'forward'))

    await task
    await asyncio.sleep(0.3)
    await task2
    await asyncio.sleep(0.3)
    await task3
    await asyncio.sleep(0.3)
    await task4
    await asyncio.sleep(0.3)


if __name__ == "__main__":
    get_data()
    
    while(True):
        key = getkey()

        if key == 'a':
            print("\nCLICKED")
            asyncio.run(moving())
