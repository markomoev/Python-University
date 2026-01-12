n = int(input("Enter the amount of numbers: "))

if n <= 15 or n >= 35:
    print("The number must be between 15 and 35")
else: 
    li = []
    while len(li) < n:
        num = int(input("Enter a number: "))

        if not 30 <= num <= 300:
            print("The number must be between 30 and 300")
        else: 
            li.append(num)
    print("The first list: ", li)

    count = 0
    for l in li:
        tens = (l // 10) % 10
        if tens % 3 == 0:
            count += 1
    print(count)

    h1_li = []
    found = False
    for l in li:
        if l % 6 == 4:
            h1_li.append(l)
            found = True
    if found:
        min1 = min(h1_li)
        i = li.index(min1)
        print(i)
    else: 
        print("Such a number not found!")

    li2 = []
    for l in li:
        if 9 < l < 100:
            if l % 2 == 0 or l % 3 == 0:
                li2.append(l)
    if len(li2) == 0:
        print("Second list is empty!")
    else: 
        print(li2)

        h1_li2 = li2[1::2]
        sum = 0
        for x in h1_li2:
            sum += x
        avg = sum / len(h1_li2)
        print(avg)

        h2_li2 = []
        for y in li2:
            if y % 2 == 0:
                h2_li2.append(y)
        if len(h2_li2) == 0:
            print("There were no even numbers")
        else: 
            min2 = min(h2_li2)
            li2.remove(min2)
            print(li2)