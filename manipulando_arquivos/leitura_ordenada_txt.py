#vamos adicionar os dados a leitura do names.txt, adicionar em uma lista e usar o 
#metodo .sorted()
names = []
i = 0
with(open("names.txt", "r", encoding="utf-8")) as file:
    for line in file:

        if i < 1:
            i += 1 
            names.append(line.rstrip())
        
names.sort()
for name in names:
    print(name)

#2. alternativa
print("------------------------------------------------------")
for name in sorted(names):
    print(name)
    
