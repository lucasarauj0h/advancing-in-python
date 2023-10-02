with open("courses.csv", 'r', encoding='utf-8') as file:
    for line in file:
        row = line.rstrip().split(",") #rstrip remove cada espaço em branco na string passada
        #o split recebe um parametro e fatia, a partir desse parametro em uma lista
        print(f'{row[0]} - {row[1]}')
        
        language, category = line.rstrip().split(",")
        print(f'{language} - {category}')