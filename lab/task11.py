txt = input("Kaji e kaput: ")

with open("log.txt", 'a', encoding='utf-8') as f:
    f.write(f'{txt}\n')