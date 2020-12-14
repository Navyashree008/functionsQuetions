# first part of reverse of string 
def reverse_of_string(string):
    a = []
    i = 0
    while i < len(string):
        a.append(string[i])
        i+=1
    print(a)
    a.reverse()
    print(a)
    print(str(a))
string = input("enter any string")
reverse_of_string(string)

# reverse of string with slicing
def reverse_of_string(string):
    print(string[::-1])
string = input("enter any string")
reverse_of_string(string)

# reverse by while loop
a = "123abc"
b=len(a)-1
while b>=0:
    print(a[b],end="")
    b=b-1

# reverse of string by reverse function part 2
def reverse_of_string(string):
    a = []
    i = 0
    while i < len(string):
        a.append(string[i])
        i+=1
    print(a)
    a.reverse()
    print(a)
    j =1 
    b = a[0]
    while j <=1:
        k = 1
        while k < len(a):
            b = b + a[k]
            k+=1
        j+=1
        print(b)
string = input("enter any string")
reverse_of_string(string)

