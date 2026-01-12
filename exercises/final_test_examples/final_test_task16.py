first_list = []

while len(first_list) < 6:
    n = int(input("Enter number for the list: "))
    first_list.append(n)
print("The list is: ", first_list)

sum_min_max = min(first_list) + max(first_list)
print("The sum of the smallest and biggest number is: ", sum_min_max)

count = 0
found = False 
for x in first_list:
    if x % 2 != 0:
        count += 1
        found = True
if found == False:
    print("There are no odd numbers in the first list!")
else: 
    print("The count of odd numbers is: ", count)


second_list = []
for x in first_list:
    if x % 5 == 0:
        second_list.append(x)
if len(second_list) == 0:
    print("There are no numbers that can be devided by 5 in the first list!")
else: 
    print("The second list is: ",second_list)

    sum_nums = 0
    for y in second_list:
        sum_nums += y
    avg = sum_nums / len(second_list)

    diff = max(second_list) - avg
    print("The difference between the biggest number and the avg is: ", diff)

    sum_first_last = second_list[0] + second_list[-1]
    second_list.append(sum_first_last)
    print("The second list with newly added number: ", second_list)