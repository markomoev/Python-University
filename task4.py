# Finding the shortest and longest words
# Write a Python function that takes a list of strings as input and 
# returns a tuple containing the shortest and longest words in the list in that order. 
# If there are multiple words with the same shortest or longest length, 
# return the first shortest/longest word found.

def short_long(): 

    inp = str(input("Enter the string, which we are making a list: "))
    li = inp.split()

    longest = max(li, key=len)
    shortest = min(li, key=len)
    
    new_li = []

    new_li.append(shortest)
    new_li.append(longest)

    print(tuple(new_li))

short_long()