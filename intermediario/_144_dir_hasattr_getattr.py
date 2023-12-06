# dir, hasattr e getattr em Python
#"has atribute" verifica se a variavel tem esse atributo
#"get atribute" nos dá esse atributo

string = 'Lucas'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('existe upper', string.upper())

if hasattr(string, metodo):
    print('existe upper', getattr(string, metodo)())
else: print("não existe metodo", metodo)

print('upper')