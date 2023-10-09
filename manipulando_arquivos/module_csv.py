import csv

courses = []

with open("courses.csv", 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        courses.append({"language": row["language"], "category": row["category"]})
print(reader)
count = []
c = 0


for i in courses:
    key, name =  i.values()
    print(key,name)

for i in courses:
    print(i)
    for chave, valor in i.items():
        if chave == "language":
            if valor == 'Python':
                print("removido")
                count.append(c)
            c += 1
            
        
            
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
c=0
for i in count:
    del courses[i-c]
    c += 1
    
for i in courses:
    print(i)
