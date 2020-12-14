def upper_lower_case(string):
    upper = 0
    lower = 0
    i =0
    while i < len(string):
        a = string[i]
        c = ord(a)
        if c >= 65 and c <=90 :
            upper = upper+1
        elif c >= 97 and c <= 122:
            lower = lower +1
        i+=1
    print(upper,"upper case letters are their")
    print(lower,"upper case letters are their")
string = input("enter any string")
upper_lower_case(string)