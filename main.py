from calibrate import calibrate as clb
import time

file_found = False
servo_min = [0] * 12
servo_max = [0] * 12
data = ""

try:
    f = open("calibrate/servo_data.v7", "r")
    data = f.read()
    file_found = True
    f.close()
    data = data.split(".")
    for i in range(12):
        servo_min[0+i] = int(data[1+i])
        servo_max[0+i] = int(data[13+i])
    print("Coming soon")
except:
    print("Servo data file not found, starting new calibration...")
    time.sleep(1)
    clb.calibration()
    pass