def sum_of_list(list):
    sum = 0
    i = 0
    while i < len(list):
        sum = sum+list[i]
        i+=1
    print(sum)
list = [2,3,4,5,6,2,4]
sum_of_list(list)
