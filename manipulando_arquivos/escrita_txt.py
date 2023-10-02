#salvando seu nome em um arquivo de texto
name = input("Digite o seu nome: \n")

"""
- Arquivos: 
1 - opção w - write (escrita)
2 - opção r - read (leitura)
3 - opção a - append (adicionar ao fim da linha)
"""

# file = open("names.txt", 'a') #Metodo open é usado para trabalhar com arquivo
# file.write(f'{name}\n')
# file.close

#alternativa 2
with(open("names.txt",'a')) as file:
    file.write(f'{name}\n')