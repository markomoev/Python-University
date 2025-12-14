try: 
    number = input("Entere a whole number: ")
    mult = 1

    if number[0] == '-': 
        number = number[1:]

    for n in number:
        mult *= int(n)

    print(mult)

except ValueError:
    print("Invalid input")