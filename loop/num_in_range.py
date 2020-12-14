def check_range(num):
    a =range(num)
    print(a)
    input1 = int(input("enter no"))
    if input1 in a:
        print("its their")
    else:
        print("not their")
check_range(20)