import random

# creating n and checking if it is in the right range
try: 
    n = int(input("Enter a number: "))
    mylst_1 = []

    if n <= 10 or n >= 50:
        raise Exception("The n number should be between 10 and 50")
    
except Exception as e:
    print(e)

# filling up the list
a = random.randint(-2499, -1300)
b = random.randint(1110, 4444)
 # getting the users number in array
nums = input("Enter numbers for filling up the list: ")
nums = nums.split(" ")

for num in nums: 
    current  = int(num)
    if a <= current <= b:
        mylst_1.append(current)
    else:
        print(f"Number {current} is out of range [{a}, {b}]")

for num in mylst_1:
    negative_nums = []
    tens = abs(num) // 10 % 10
    if num < 0 and tens % 4 == 0 or tens % 5 == 0: 
        negative_nums.append(num)

    
sum = 0
count = 0
for num in mylst_1:
    if len(num) == 2 and num % 2 == 0:
        sum += num
        count += 1

avg_sum = sum // count


# second list operations
mylst_2 = []
for num in mylst_1:
    if len(num) == 3 and num % 3 == 0:
        mylst_2.append(num)


special_mylst2 = []
for n in mylst_2:
    count += 1
    if n % 2 != 0 and count % 2 == 0:
        special_mylst2.append(n)


for n in mylst_2:
    count += 1
    if count % 2 != 0:
        n = 13

len1 = len(mylst_1)
len2 = len(mylst_2)

if len1 > len2: 
    mylst_1.remove(mylst_1[0])
    mylst_1.remove(mylst_1[-1])

if len2 > len2: 
    mylst_2.remove(mylst_2[0])
    mylst_2.remove(mylst_2[-1])

if len1 == len2: 
    print("Both lists are equal as length")