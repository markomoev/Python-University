import random

try:
    n = int(input("Enter n: "))
    li = []
    sum_nums = 0

    if n <= 10 or n >= 20: 
        raise Exception("The n number should have a value between 10 and 20")

    for num in range(0, n):
        num = random.randint(-500, 500)
        li.append(num)

    for number in li:
        nummie = int(number)
        if nummie % 7 == 0 and nummie >= 0:
            sum_nums += nummie
    
    print(sum_nums)

except Exception as e:
    print(e)