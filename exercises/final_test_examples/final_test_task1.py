import random

li = []
li2 = []

try: 
    n = int(input("Enter n:"))
    if n <= 20 or n >= 30: 
        raise Exception("The n number should be between 20 and 30")    
except Exception as e : 
    print(e)
    exit()

# operations with list 1

for num in range(0, n):
    num = random.randint(-1000, 1000)
    li.append(num)

i = -1
sum = 0
count = 0

# sum of the odd numbs
for i in range(len(li)):
    if i % 2 != 0:
        sum += li[i]

# checking if the decimal can be devided by 3
for x in li:
    tens = abs(x) // 10 % 10
    if tens % 3 == 0:
        count += 1

# multiply
product = 1
found = False

for x in li: 
    if x < 0 and x % 2 == 0:
        product *= x
        found = True

if found:
    print(product)
else: 
    print("No such elements")


# operations with list 2
diff = max(li2) - min(li2)

count2 = 0
for a in li2:
    if a % 2 != 0:
        count2 += 1
print(count2)

li2.remove(min(li2))
