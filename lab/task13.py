with open("data.txt", 'r', encoding="utf-8") as f:
    for line in f:
        if "Python" in line:
            python_line = line
            print(python_line)