# Check before adding
# Write a Python function that takes a list and an element as input. 
# The function should add the element to the list only 
# if it is not already present in the list.

def func(li=[1,2,23,4], n=23):
    
    if n not in li:
        li.appent(n)
    print(li)

func()