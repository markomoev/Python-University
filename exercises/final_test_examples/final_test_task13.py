n = int(input("Enter a number between 15 and 35: "))

if n < 15 or n > 35:
    print("The number should be between 15 and 35!")
else:
    li = []

    while len(li) < n:
        num = int(input("Enter a number: "))
        if 30 <= num <= 300:
            li.append(num)
        else: 
            print("Invalid number")
    print(li)

    count = 0
    
    for l in li:
        tens = (l // 10) % 10
        if tens % 3 == 0:
            count += 1
    print(count)

    min_nums = []
    for l in li:
        if l % 6 == 4:
            min_nums.append(l)
    min_val = min(min_nums)
    print(li.index(min_val))


    li2 = [num for num in li if 9 < num < 100 and (num % 2 == 0 or num % 3 == 0)]
    if len(li2) == 0:
        print("There are no such numbers!")
    else: 
        print(li2)

        sum = 0
        count = 0
        for i in range(len(li2)):
            if i % 2 != 0:
                sum += li2[i]
                count += 1
        avg = sum / count
        print(avg)

        even_nums = [num for num in li2 if num % 2 == 0]

        if even_nums:
            min_num = min(even_nums)
            li2.remove(min_num)
            print("After removing minimum even number:", li2)
        else:
            print("No even numbers to remove!")
