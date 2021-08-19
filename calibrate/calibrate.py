from getkey import getkey, keys
import os
import time

def file_detect(found):
    if found:
        return "Data file found!"
    else:
        return "New calibration!"

def calibrate_screen(which_servo,if_max,file_found,servo_min,servo_max):
    print(f"\n {file_detect(file_found)}\n\n\n            ############################ Servo Calibration ############################\n")
    print(f"    Controls: w = +1    W = +15                                   Servo = {which_servo+1} \n")
    print(f"              s = -1    S = -15                                   Min = {servo_min[which_servo]}\n")
    if if_max:
        print(f"       q = set minimum    (( e = set maximum ))                   Max = {servo_max[which_servo]}\n")
    else:
        print(f"      (( q = set minimum ))    e = set maximum                    Max = {servo_max[which_servo]}\n")
    print(f"        a = previous servo    d = next servo\n\n\n")
    print(f"            Press ENTER to save and finish. ( or Control+C to quit without saving )\n")

def calibration():

    file_found = False
    data = ""

    servo_min = [0] * 12
    servo_max = [0] * 12

    try:
        f = open("calibrate/servo_data.v7", "r")
        data = f.read()
        file_found = True
        f.close()
        data = data.split(".")
        for i in range(12):
            servo_min[0+i] = int(data[1+i])
            servo_max[0+i] = int(data[13+i])
    except:
        file_found = False
        pass

    servo_now = 0
    servo_direction = True

    print("Starting calibration...")
    time.sleep(1)


    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        calibrate_screen(servo_now,servo_direction,file_found,servo_min,servo_max)
        key = getkey()
        if key == 'W':
            if servo_direction:
                servo_max[servo_now]+=15
            else:
                servo_min[servo_now]+=15
            os.system('cls' if os.name == 'nt' else 'clear')
            calibrate_screen(servo_now,servo_direction,file_found,servo_min,servo_max)

        elif key == 'S':
            if servo_direction:
                servo_max[servo_now]-=15
            else:
                servo_min[servo_now]-=15
            os.system('cls' if os.name == 'nt' else 'clear')
            calibrate_screen(servo_now,servo_direction,file_found,servo_min,servo_max)
        elif key == 'w':
            if servo_direction:
                servo_max[servo_now]+=1
            else:
                servo_min[servo_now]+=1
            os.system('cls' if os.name == 'nt' else 'clear')
            calibrate_screen(servo_now,servo_direction,file_found,servo_min,servo_max)
        elif key == 's':
            if servo_direction:
                servo_max[servo_now]-=1
            else:
                servo_min[servo_now]-=1
            os.system('cls' if os.name == 'nt' else 'clear')
            calibrate_screen(servo_now,servo_direction,file_found,servo_min,servo_max)
        elif key == 'e':
            servo_direction = True
            os.system('cls' if os.name == 'nt' else 'clear')
            calibrate_screen(servo_now,servo_direction,file_found,servo_min,servo_max)
        elif key == 'q':
            servo_direction = False
            os.system('cls' if os.name == 'nt' else 'clear')
            calibrate_screen(servo_now,servo_direction,file_found,servo_min,servo_max)
        elif key == 'a':
            if servo_now>0:
                servo_now -= 1
            os.system('cls' if os.name == 'nt' else 'clear')
            calibrate_screen(servo_now,servo_direction,file_found,servo_min,servo_max)
        elif key == 'd':
            if servo_now<11:
                servo_now += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            calibrate_screen(servo_now,servo_direction,file_found,servo_min,servo_max)
        elif key == keys.ENTER:
            data="sv&&servos."+str(servo_min[0])+"."+str(servo_min[1])+"."+str(servo_min[2])+"."+str(servo_min[3])+"."+str(servo_min[4])+"."+str(servo_min[5])+"."+str(servo_min[6])+"."+str(servo_min[7])+"."+str(servo_min[8])+"."+str(servo_min[9])+"."+str(servo_min[10])+"."+str(servo_min[11])+"."+str(servo_max[0])+"."+str(servo_max[1])+"."+str(servo_max[2])+"."+str(servo_max[3])+"."+str(servo_max[4])+"."+str(servo_max[5])+"."+str(servo_max[6])+"."+str(servo_max[7])+"."+str(servo_max[8])+"."+str(servo_max[9])+"."+str(servo_max[10])+"."+str(servo_max[11])+".enddata#"
            f = open("calibrate/servo_data.v7", "w")
            f.write(data)
            f.close()
            os.system('cls' if os.name == 'nt' else 'clear')
            break



if __name__ == "__main__":

    print("Use Calibration in settings.py to calibrate...")
    exit()