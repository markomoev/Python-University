n = int(input("Enter amount of numbers: "))

if n <= 4 or n >= 35:
    print("The number should be between 15 and 35!")
else:
    li = []
    while len(li) < n:
        num = int(input("Enter number for the list: "))

        if num < 30 or num > 300:
            print("The numbers in the list should be between 30 and 300 included!")
        else: 
            li.append(num)
    print("The list is: ", li)

    count = 0
    found1 = False
    for l in li:
        current = str(l)
        tens = int(current[-2])
        if tens % 3 == 0:
            count += 1
            found1 = True
    if found1:
        print("The count of number that can be devided by 3 is: ",count)
    else: 
        print("Sorry there were no numbers that can be devided by 3 in the list!")


    h_list = []
    for l in li:
        if l % 6 == 4:
            h_list.append(l)
    min_str_num = min(h_list)
    index = li.index(min_str_num)
    print("The index of the smallest strange number is: ", index)


    li2 = [l for l in li if 9 < l < 100 and (l % 2 == 0 or l % 3 == 0)]
    if len(li2) == 0:
        print("There were no such numbers to fill up the second list!")
    else: 
        print("The second list is: ", li2)

        h_li2 = li2[1::2]
        sum_ = 0
        for x in h_li2:
            sum_ += x
        avg = sum_ / len(h_li2)
        print("The average of the numbers with odd indexes: ", avg)

        h2_li2 = []
        for y in li2:
            if y % 2 == 0:
                h2_li2.append(y)
        min_num_even = min(h2_li2)
        li2.remove(min_num_even)
        print("Second list after deleting the smallest even number: ", li2)