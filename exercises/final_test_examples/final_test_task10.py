import random

N = int(input("Enter a number between 5 and 12: "))

if N < 5 or N > 12:
    print("Wrong interval")
else: 
    a = []
    b = []

    for n in range(N):
        a.append(random.randint(10, 99))
        b.append(random.randint(10, 99))
    print(a,b)

    c = []
    d = []
    for x in a:
        if x in b and x not in c:
            c.append(x)
        if x not in b:
            d.append(x)
    c.sort()

    print(c, d)

    sum = 0
    for y in d:
        sum += y
    if len(d) == 0:
        print("There are no numbers in d!")
    else:
        print(d, sum)

    if len(d) == 0:
        print("There are no numbers in d!")
    else:
        d = d[1::2]
        print(d)