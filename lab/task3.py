# Write a Python function that takes a string as input and returns a dictionary 
# containing the number of uppercase and lowercase letters in the string. 
# Any characters that cannot be categorized as uppercase or lowercase (e.g. symbols) 
# should be counted as "other".

def func():
    text = str(input("Enter text: "))

    dic = {
        "uppercase": "",
        "lowercase": "",
        "other": ""
    }

    upper_number = 0
    lower_number = 0
    other_number = 0

    for i in text:
        if i.isupper() == True:
            upper_number += 1
            dic["uppercase"] = upper_number
        elif i.islower() == True:
            lower_number += 1
            dic["lowercase"] = lower_number
        else:
            other_number += 1
            dic["other"] = other_number

    print(dic)

func()