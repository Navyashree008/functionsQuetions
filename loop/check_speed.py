def check_speed(speed):
    if speed < 70:
        print("ok")
    elif speed > 70:
        point =speed // 5
        print(point)
        if  point >= 12:
            print("license is suspended" )
    return speed
check_speed(86)

def check(num):
    a = num
    print(a)
    print(check_speed(86))
check(4)