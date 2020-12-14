def unique_eliment(list1):
    # list1 = [1,2,3,3,3,3,4,5]
    b = []
    i = 0
    for i in range(len(list1)):
        if list1[i] not in b:
            b.append(list1[i])
    print(b)
    return b
list1 = [1,2,3,3,3,3,4,5]
unique_eliment(list1)