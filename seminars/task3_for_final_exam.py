import random

# creating the list with negative numbers
nums_list = []
for i in range(20):
    nums_list.append(random.randint(-1000, -1))
print("The list with random numbers: ", nums_list)

# getting the biggest number in the list
biggest_num = max(nums_list)
print("Biggest number: ", biggest_num)

# summing the numbers in the list
sum = 0
for num in nums_list:
    sum += num
print("The sum of all the numbers in the list is: ", sum)

# second list for numbers that can be devided by 3
nums_list2 = [] # the list

for num in nums_list:
    if num % 3 == 0:
        nums_list2.append(num)

print("The second list with numbers that can be devided by 3: ", nums_list2)

# sorting the second list and 
nums_list2.sort()
print("The second list, but sorted: ", nums_list2)

# deleting all the elements with odd index in the list
index = -1
for n in nums_list2:
    index += 1
    if index % 2 != 0:
        nums_list2.remove(n)

print("Filtered list: ", nums_list2)