

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


def leg_step(which,where):
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

    servo(which[1],0)
    servo(which[2],100)
    time.sleep(0.1)
    servo(which[0],where)
    time.sleep(0.1)
    servo(which[1],100)
    servo(which[2],0)
    time.sleep(0.02)

def walk(f="f"):
    
    spider_pos("default")
    time.sleep(0.4)
    while(f=="f"):
        leg1 = threading.Thread(target=leg_step, args=(1,90))
        leg4 = threading.Thread(target=leg_step, args=(4,0))
        leg1.start()
        leg4.start()
        time.sleep(0.2)
        servo(0,60)
        servo(9,40)
        servo(3,70)
        servo(6,20)
        time.sleep(0.2)
        leg2 = threading.Thread(target=leg_step, args=(2,0))
        leg3 =threading.Thread(target=leg_step, args=(3,90))
        leg2.start()
        leg3.start()
        time.sleep(0.2)
        servo(3,40)
        servo(6,50)
        servo(0,20)
        servo(9,70)
        time.sleep(0.2)
