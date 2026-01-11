import random

try: 
    n = int(input("Enter a whole number: "))
    n_list = []

    # checking for the input
    if n <= 20 or n >= 30:
        raise Exception("The number should be between 20 and 30")
    
    # adding elements to the list
    for el in range(0, n):
        el = random.randint(-999, 1000)
        n_list.append(el)

    # operations for the first list 
    sum_odds = 0
    for i in range(len(n_list)):
        if i % 2 != 0: 
            sum_odds += n_list[i]

    count = 0
    for num in n_list:
        tens = abs(num) // 10 % 10
        if tens % 3 == 0:
            count += 1

    mult = 1
    for num in n_list:
        if num < 0 and num % 2 == 0:
            mult *= num

    # creating the second list
    another_n_list = []
        # filling the list
    for num in n_list:
        if num > n or num < (n * -1):
            another_n_list.append(num)

    # operations with the second list
    diff = max(another_n_list) - min(another_n_list)

    another_count = 0
    for nums in another_n_list:
        if nums % 2 != 0:
            another_count += 1

    another_negative_list = []
    for nums in another_n_list:
        if nums < 0: 
            another_negative_list.append(nums)

    another_n_list.remove(max(another_negative_list))
 
except Exception as e:
    print(e)