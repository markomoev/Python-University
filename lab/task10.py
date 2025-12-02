with open('hello.txt','r', encoding = 'utf-8') as f:
    count_lines = 0
    count_words = 0
        
    for line in f:
        count_lines +=1 
        count_words = len(line.split(' '))
            
    print(count_lines)
    print(count_words)