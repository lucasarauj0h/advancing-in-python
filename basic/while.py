#repetições:  while (enquanto) - executa uma ação quando a condição for verdadeira

contador = 0
while contador <= 10:
    contador += 1
    if contador == 4:
        print("nao vou mostrar o 4")
        continue
    print(contador)
    
    
