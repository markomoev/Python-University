try: 
    # inputing numbers and checking if they are 12
    nums = input("Enter 12 numbers: ")
    if len(nums.strip()) < 12:
        raise Exception("You should enter 12 numbers!")
    
    # creating the list
    nums_arr = nums.split()

    # operations
    for n in nums_arr:
        current = float(n)
        if current < 0 or not current.is_integer():
            raise Exception("The numbers should be whole and positive!")
        
    count_odd = 0
    for n in nums_arr:
        current = int(n)
        if current % 2 != 0:
            count_odd += 1
    print(f"{count_odd} odd numbers")

    count = 0
    sum = 0
    for n in nums_arr:
        current = int(n)
        sum += current
        count += 1
    avg_sum = sum / count
    print(avg_sum)


    nums_help_arr = []
    nums_spec_arr = []
    for n in nums_arr:
        current = int(n)
        if current % 2 == 0:
            nums_help_arr.append(current)
    print(nums_help_arr)

    nums_help_arr.sort(reverse=True)

    nums_spec_arr = nums_help_arr[0:5]
    nums_spec_arr.sort(reverse=True)
    print(nums_spec_arr)

    i = -1
    new_list = []
    for num in nums_spec_arr:
        i += 1
        if i % 2 != 0:
            new_list.append(num)
    nums_spec_arr = new_list 
    print(nums_spec_arr)

except Exception as e:
    print(e)