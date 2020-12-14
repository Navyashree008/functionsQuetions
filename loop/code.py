i = 1
while i <= 5:
    # a = i
    j = i
    t = i+i-1
    while j <= t:
        b = j
        if b > t:
            print(b,end="")
            b = b-1
        else:
            print(b,end="")
            b = b+1
        j+=1
    print()
    i+=1


# i = 1
# while i <= 5:
#     j = i
#     t = i + i-1
#     b = j
#     while j < t:
#         print(b,end="")
#         b = b+1
#         j+=1
#     j = 1
#     while j < t:
#         print(b,end="")
#         b = b-1
#         j+=1
#     print()
#     if i == 1:
#         print(i)
#     i+=1