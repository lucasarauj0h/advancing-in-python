a = 'A'
b = "B"
c = 1.1
formato = 'a={} agora é b={} agora tem de ser a C {}'.format(a,b,c) #quando eu coloco uma chave, e um .format, o parametro 
#o parametro é recebido de acordo com a ordem de parametros do .format
print(formato)
string = 'a={} agora é b={} agora tem de ser a C {}'
formatando = string.format(a,b,c)

string1 = 'a={0} agora é b={1} agora tem de ser a C {2} e repete o a {0}'
formatando2 = string1.format(a,b,c)
print(formatando2)

#parametro nomeado
#assim que eu nomeio um parametro, tenho que chamar ele pelo nome. exemplo a seguir

string2 = 'a={0} agora é b={1} agora tem de ser a C {nome3} e repete o A {0}'
formatando3 = string2.format(
    a,b, nome3=c
    )
