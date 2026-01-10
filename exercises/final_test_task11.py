import random

M = int(input("Enter a number between 6 and 15: "))

if M < 6 or M > 15:
    print("Enter a number between 6 and 15 including!")
else: 
    nums = []
    for m in range(M):
        current = random.randint(1,50)
        nums.append(current)
    print(nums)

    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    
    if len(evens) == 0 :
        print("There are no even numbers in the list nums!")
    else: 
        print(evens)

    odds_unique = []
    for n in nums:
        if n % 2 != 0 and n not in odds_unique:
            odds_unique.append(n)

    if len(odds_unique) == 0:
        print("There are no odd numbers in the list nums!")
    else: 
        odds_unique.sort(reverse=True)
        print(odds_unique)

    sum = 0
    for n in evens:
        sum += n
    if len(evens) == 0:
        print("There are no numbers in the list evens!")
    else:   
        avg = sum / len(evens)
        print(avg)

    nums = nums[::2]
    print(nums)