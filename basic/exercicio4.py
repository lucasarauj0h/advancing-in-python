"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra = 'zeppeto'
contagem = 0
corretas = ''

while True: 
    letra = input("Digite uma letra! ")
    
    if letra == 0:
        break

    if len(letra) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra in palavra:
        corretas += letra

    total_palavra = ''
    for l_secret in palavra:
        if l_secret in corretas:
            total_palavra += (l_secret)
        else: 
            total_palavra += '*'

    print(total_palavra)
    contagem += 1

    if total_palavra == palavra:
        break

print(f"Parabéns, você acertou na {contagem}x tentativa!")