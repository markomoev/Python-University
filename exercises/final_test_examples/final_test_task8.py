import random

list1 = []
list2 = []

X = int(input("Enter a whole number between 5 and 15: "))

if X < 5 or X > 15:
    print("The number should be between 5 and 15!")

else: 
    for i in range(0, X+1):
        num = random.randint(51,80)
        list1.append(num)

    for i in range(0, X+1):
        num = random.randint(51 ,80)
        list2.append(num)

    print(list1, list2)
    
    list3 = []
    list4 = []


    for x in list1:
        if x in list2 and x not in list3:
            list3.append(x)        
    list3.sort(reverse=True)

    for y in list2:
        if y not in list1 and y not in list4:
            list4.append(y)

    print(list3, list4)

    sum = 0
    length = len(list4)
    if length == 0: 
        print("There is nothing in list 4!")
    else: 
        for n in list4:
            sum += n
        
        avg = sum / length
        list4 = list4[::2]
        print(list4)