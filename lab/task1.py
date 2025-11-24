inp = int(input("Enter a number: "))
l =[]
dict = {}

for i in range(1, inp + 1):
    l.append(i)
    reversed_l = l[::-1]

dict = {i: reversed_l[i-1] for i in l}
print(dict)
