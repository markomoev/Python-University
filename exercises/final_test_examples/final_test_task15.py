import random
mylst_15 = []

for x in range(15):
    current = random.randint(-5000, 0)
    mylst_15.append(current)
print("Current list: ", mylst_15)

max_num = max(mylst_15)
print("Maximum number: ", max_num)

sum = 0
for n in mylst_15:
    sum += n
print("The sum of the numbers in the first list: ",sum)

mylst_dev3 = []
for n in mylst_15:
    if n % 3 == 0:
        mylst_dev3.append(n)
print("Here is the second list: ", mylst_dev3)

mylst_dev3.sort()
print("Here is the sorted second list: ", mylst_dev3)

mylst_dev3 = mylst_dev3[::2]
print("Here is the second list without the odd index nums: ", mylst_dev3)