# def perfect(num):
#     sum1 = 0
#     for x in range(1,num):
#         if num % x == 0:
#             sum1 = sum1 + x
#     if sum1 == num:
#         print("its a perfect num")
# perfect(6)
            
# def perfect(num):
#     i = 1
#     while i <= 1000:
#         sum1 = 0
#         for x in range(1,i):
#             if i % x == 0:
#                 sum1 = sum1 + x
#         if sum1 == i:
#             print(i)
#         i+=1

def perfect():
    i = 1
    while i <= 1000:
        sum1 = 0
        for x in range(1,i):
            if i % x == 0:
                sum1 = sum1 + x
        if sum1 == i:
            print(i)
        i+=1
perfect()
