def soma(x,y):
    return x+y
    
def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y


def impar(texto):
    letras = []
    for i in range(1,len(texto),2):
        letras += texto[i]
        
    print(letras)

def par(texto):
    letras = []
    for i in range(0,len(texto),2):
        letras += texto[i]
        
    print(letras)

def inverso(text):
    print(text[::-1])
