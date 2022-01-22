def forward_steps_frontlegs(leg,step,servo):
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

def forward_steps_rearlegs(leg,step,servo):
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



def backward_steps_frontlegs(leg,step,servo):
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

def backward_steps_rearlegs(leg,step,servo):
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


def turn_left_frontlegs(leg,step,servo):
    step = step % 12
    if step == 0:
        servo((leg*3)+0,20)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 1:
        servo((leg*3)+0,20)
        servo((leg*3)+1,0)
        servo((leg*3)+2,10)
    elif step == 2:
        servo((leg*3)+0,20)
        servo((leg*3)+1,0)
        servo((leg*3)+2,10)
    elif step == 3:
        servo((leg*3)+0,40)
        servo((leg*3)+1,0)
        servo((leg*3)+2,10)
    elif step == 4:
        servo((leg*3)+0,60)
        servo((leg*3)+1,0)
        servo((leg*3)+2,10)
    elif step == 5:
        servo((leg*3)+0,80)
        servo((leg*3)+1,0)
        servo((leg*3)+2,10)
    elif step == 6:
        servo((leg*3)+0,80)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 7:
        servo((leg*3)+0,60)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 8:
        servo((leg*3)+0,40)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 9:
        servo((leg*3)+0,20)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 10:
        servo((leg*3)+0,20)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 11:
        servo((leg*3)+0,20)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    else:
        print("12 steps, 0-11")

def turn_left_rearlegs(leg,step,servo):
    step = step % 12
    if step == 0:
        servo((leg*3)+0,80)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 1:
        servo((leg*3)+0,80)
        servo((leg*3)+1,0)
        servo((leg*3)+2,10)
    elif step == 2:
        servo((leg*3)+0,80)
        servo((leg*3)+1,0)
        servo((leg*3)+2,10)
    elif step == 3:
        servo((leg*3)+0,60)
        servo((leg*3)+1,0)
        servo((leg*3)+2,10)
    elif step == 4:
        servo((leg*3)+0,40)
        servo((leg*3)+1,0)
        servo((leg*3)+2,10)
    elif step == 5:
        servo((leg*3)+0,20)
        servo((leg*3)+1,0)
        servo((leg*3)+2,10)
    elif step == 6:
        servo((leg*3)+0,20)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 7:
        servo((leg*3)+0,40)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 8:
        servo((leg*3)+0,60)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 9:
        servo((leg*3)+0,80)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 10:
        servo((leg*3)+0,80)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    elif step == 11:
        servo((leg*3)+0,80)
        servo((leg*3)+1,100)
        servo((leg*3)+2,10)
    else:
        print("12 steps, 0-11")