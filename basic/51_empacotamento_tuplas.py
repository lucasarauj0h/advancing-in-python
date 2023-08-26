nomes = ['Lucas', 'Diana', 'Maria'] #vamos tirar um dos valores e passar para outro

nome1, nome2, nome3 = nomes
print(nome1, nome2, nome3)
print(nomes)

nome4, *resto = ['Lucas', 'Diana', 'Maria']
print(nome4)
print(resto)