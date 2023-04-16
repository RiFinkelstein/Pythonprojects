def check_speed(speed):
    speed_limit = 70
    demerit_points = 0
    if speed < speed_limit:
        print("Ok")
    else:
        demerit_points = (speed - speed_limit) // 5
        if demerit_points > 12:
            print("License suspended")
        else:
            print("Points:", demerit_points)
speed = int(input("Enter the speed of the driver (in km/h): "))
check_speed(speed)
