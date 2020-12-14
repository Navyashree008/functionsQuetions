def length_of_string(string1,string2):
    if len(string1)>len(string2):
        print(string1)
    elif len(string1) < len(string2):
        print(string2)
    else:
        print(string1)
        print(string2)
string1 = input("enter any string")
string2 = input("enter any string")
length_of_string(string1,string2)