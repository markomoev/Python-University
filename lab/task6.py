# De-posting and Sorting
# Write a Python function that takes a list of lows as input and returns another list
# containing unique elements from the input list, sorted alphabetically.

def check(li = ["hello", "cow", "apple", "long", "long", "cow"]):
    new_li = []

    for i in li:
        if(li.count(i) == 1):
            new_li.append(i)
    new_li.sort()
    print(new_li)
check()