def divisible_of_3_5(limit):
    for x in range(1,limit+1):
        if x % 3 == 0 and x % 5 == 0:
            print(x)
divisible_of_3_5(40)