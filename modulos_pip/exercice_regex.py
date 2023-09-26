#Escreva um programa em Python para verificar se uma string contém apenas um 
#determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).
import re

def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

print(check_character("28321"))
print(check_character("ASDAEA"))
print(check_character("ASDAE2#A"))
