frase = 'O python é uma linguagem de programação multiparadigma' \
        'Python foi criado por Guido van Rossum.'

frase = frase.lower()

total_letra = 1
letra = ''

print(frase.count(''))
i = 0

while i < len(frase):
    letra_atual = frase[i]
    qntd_letra = frase.count(letra_atual)
    #print(qntd_letra)

    if qntd_letra > total_letra and letra_atual != ' ':
        total_letra = qntd_letra
        letra = frase[i]
        #print(letra)

    i += 1 

print(f'a letra que mais aparece é {letra}, aparecendo um total de {total_letra} vezes.')