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

def leg(which,position="none"):
    if which == '1':
        which = [0,1,2]
    elif which == '2':
        which = [3,4,5]
    elif which == '3':
        which = [6,7,8]
    elif which == '4':
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



def menu_screen(leg):
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

def settings_menu():


    print("Entering test...")
    actual_leg=1
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    menu_screen()

    while(True):
        key = getkey()

        if key == 'u':
            leg(actual_leg,"u")
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_screen(actual_leg)

        elif key == 'd':
            leg(actual_leg,"d")
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_screen(actual_leg)

        elif key == 'o':
            leg(actual_leg,"o")
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_screen(actual_leg)

        elif key == 'c':
            leg(actual_leg,"c")
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_screen(actual_leg)

        elif key == 'f':
            leg(actual_leg,"f")
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_screen(actual_leg)

        elif key == 'n':
            leg(actual_leg,"n")
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_screen(actual_leg)


        elif key == 'A':
            if actual_leg>1:
                actual_leg -= 1

            os.system('cls' if os.name == 'nt' else 'clear')
            menu_screen(actual_leg)

        elif key == 'D':
            if actual_leg<4:
                actual_leg += 1

            os.system('cls' if os.name == 'nt' else 'clear')
            menu_screen(actual_leg)


        elif key == 'Q':
            exit()


if __name__ == "__main__":
    get_data()
    settings_menu()
    
