#Variaveis livres + nonlocal

def fora(x):
    a = x
    def dentro():
        print(locals())
        return a
    return dentro

# por que A é uma variavel livre?: porque não está definida na variavel dentro. 
#ela é livre porque faz parte do escopo 'fora', quando executado o escopo dentro a var
#não está definida, mas a retorna. 

dentro = fora(10)

dentro_2 = fora(20)

print(dentro())
print(dentro_2())

def concatenar(string_initial):
    valor_final = string_initial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

texto = concatenar('a')
print(texto('b'))
print(texto('c'))
print(texto('d'))
final = texto()
print(final)