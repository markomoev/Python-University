num = int(input("napishi chislo e maina: "))

with open("hello.txt", 'r') as f:
    a = f.read(num)
    print(a)