try:
    # declarations 
    txt = str(input("Please enter the numbers: "))
    li = txt.split()

    li_plus = []
    li_minus = []

    sum_plus = 0
    plus_avg = 0

    # operations
    for n in li:
        num = float(n)
        
        if num > 0:
            li_plus.append(num)
            for a in li_plus:
                sum_plus += a
                plus_avg = sum_plus / len(li_plus)

        if num < 0:
            li_minus.append(num)

    # exceptions
    if txt.strip() == "":
        raise Exception("There is nothing in your list")

    if li_minus == [] or li_plus == []: 
        raise Exception("You should enter both positive and negative numbers")
    else: 
        print(int(plus_avg))
        print(int(max(li_minus)))

except Exception as e: 
    print(e)