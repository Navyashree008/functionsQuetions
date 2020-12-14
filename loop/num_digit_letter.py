a = "python 2.6"
alphabet = 0
digit = 0
i = 1
while i < len(a):
    ch = ord(a[i])
    if ch >= 65 and ch <= 90 or ch >= 97 and ch <=122:
        alphabet = alphabet+1
    else:
        digit =digit+1
    i+=1
print(alphabet)
print(digit)