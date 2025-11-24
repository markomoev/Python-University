# Write a Python function that prompts the user for a number. 
# Then, if that number is present, it prints the sentence 
# "Hello, Python!" a specified number of times.

def greet_python():
    num = int(input("Enter a number: "))

    for i in range(num):
      print("Hello Python!")
greet_python()
