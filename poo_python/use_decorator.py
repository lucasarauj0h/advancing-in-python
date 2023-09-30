from entities.decorator import my_decorator, uppercase_decorator, split_string

# exemplo 1
@my_decorator #Ele vai executar a função my_decorator, usando a função como parametro
def my_function(): 
    print("Dentro da função")
    
my_function()

# exemplo 2
#passando a função texto como parametro do decorator em tempo real
@uppercase_decorator
def text():
    return ("Hello World!")

print(text())

#exemplo 3
@split_string
def example():
    return "Aprendendo python e criando decorators"

print(example())

@split_string
@uppercase_decorator
def example():
    return "Aprendendo python e criando decorators"

print(example())
    