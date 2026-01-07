import random

try: 
    n = int(input("Enter a number: "))

    if n <= 15 or n >= 40: 
        raise Exception("The number should be between 15 and 40")
    
    a = random.randint(-3001, 1501)
    b = random.randint(1201, 5001)

    nums = str(input("Enter all the numbers with space in between: "))

    # list number 1
    lst_1 = nums.split()
    if len(lst_1) != n:
        raise Exception("The amount of numbers should be equal to the first number that you entered!")
    elif min(lst_1) < a or max(lst_1) >= b:
        raise Exception("Numbers in the list are not between a and b!")
    
    count = 0
    count2 = 0
    found = False
    avg_sum = 0

    for n in lst_1:
        current = int(n)
        if current < 0:
            current_string = str(current)
            if (current_string[-1]) % 3 == 0 or int(current_string[-1]) % 6 == 0:
                count += 1
        if len(current) == 3:
            count2 += 1
            sum += current
            avg_sum = sum / count2
            found = True

    print("Count of special numbers: ", count)

    if not found:
        print("There are no numbers between 100 and 1000")
    
    # list number 2
    lst_2 = []
    for n in lst_1:
        current = int(n)
        if len(str(current)) == 4 and current % 5 == 0:
            lst_2.append(current)

    index = -1
    count3 = 0
    for n in lst_2:
        current = int(n)
        index += 1

        if index % 2 != 0 and current % 2 == 0:
            count3 += 1
        if index % 2 == 0: 
            lst_2[index] = -99

    print("Count for special numbers: ", count3)
    print("The new list after swapping numbers: ", lst_2)

    if len(lst_1) > len(lst_2):
        lst_1.remove(lst_1[2])
        lst_1.remove(lst_1[-2])
        print("The shortened list: ", lst_1)

    if len(lst_1) < len(lst_2):
        lst_2.remove(lst_2[2])
        lst_2.remove(lst_2[-2])
        print("The shortened list: ", lst_2)

except Exception as e:
    print(e)