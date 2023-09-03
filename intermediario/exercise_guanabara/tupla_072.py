cont = ('zero', 'um','dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinte', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte',)
# true = 2
# while True:
#     try:
#         print('Digite um numero de 0 a 20')
#         num = int(input())
#         if num >= 0 and num <= 20:
#             for i in range(len(cont)):
#                 if i == num:
#                     print(f'Número {num} em extenso: {cont[i]}')
#                     true = 489
#                     break
#         else:
#             print('número invalido.')
#     except: 
#         print('você não digitou um número')

cont = ('zero', 'um','dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinte', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte',)

while True:
    try:
        print('Digite um numero de 0 a 20')
        num = int(input())
        if num >= 0 and num <= 20:
            print(f'Número {num} em extenso: {cont[num]}')
            break
        else:
            print('número invalido.')
    except: 
        print('você não digitou um número')

