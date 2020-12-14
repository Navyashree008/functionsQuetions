def multiple_of_list(list):
    mul = 1
    i = 0
    while i < len(list):
        mul = mul*list[i]
        i+=1
    print(mul)
list = [8,2,3,-1,7]
multiple_of_list(list)