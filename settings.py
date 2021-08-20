from getkey import getkey, keys
from calibrate import calibrate as clb
import os
import time

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
        print("Servo data file not found, starting new calibration...")
        time.sleep(1)
        file_found = False
        pass

def menu_screen():
    print(f"\n  ############################ Spider Settings ############################\n")
    print(f"    Press: r - Recalibrate \n")
    print(f"           R - Remove Servo Data File \n")
    print(f"           q - Quit \n")

def settings_menu():


    print("Entering settings menu...")
    time.sleep(1)


    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_screen()
        key = getkey()
        if key == 'r':
            clb.calibration()
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_screen()
        elif key == 'R':
            try:
                os.remove("calibrate/servo_data.v7")
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("\n\n\n   Data file removed!")
                time.sleep(2)
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n\n\n   File doesn't not exist anyway!")
                time.sleep(2)
            menu_screen()
        elif key == 'q':
            exit()

if __name__ == "__main__":

    settings_menu()
