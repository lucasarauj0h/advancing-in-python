
#lembrar das aulas de escopo do JAVA, declarar e criar variaveis fora do escopo do IF
"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = False
passou_no_if = None

if condicao:
    print("passou no if")
    passou_no_if = True
else:
    print("não passou no if")

print(passou_no_if, passou_no_if is None) #True = passou no if é none
print(passou_no_if, passou_no_if is not None) #False = é none, pois é falso que ele n é

if passou_no_if is None:
    print("passou_no_if é None")

elif passou_no_if is not None:
    print("passou_no_if não é None")