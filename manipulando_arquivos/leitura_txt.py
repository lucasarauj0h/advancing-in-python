"""
- Arquivos: 
1 - opção w - write (escrita)
2 - opção r - read (leitura)
3 - opção a - append (adicionar ao fim da linha)
"""

with(open("names.txt", "r", encoding="utf-8")) as file:
    for line in file: #criando um laço de repetição para ler linha a linha do arquivo
        print(f'{line.rstrip()}') #rstrip para que não haja uma linha vazia desenessária