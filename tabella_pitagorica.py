i = 1 
a = 1

while i < 11:
    print(a * i, end = " ")
    a += 1
    if a >= 11:
        i += 1
        a = 1
    if a == 10:
        print("")
