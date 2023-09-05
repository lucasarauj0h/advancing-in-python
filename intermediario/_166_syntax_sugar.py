def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        return func(*args, **kwargs)
    return interna

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser uma string')

@criar_funcao
def inverte_string(string):
    return string[::-1]


invertida = inverte_string('123')
print(invertida)