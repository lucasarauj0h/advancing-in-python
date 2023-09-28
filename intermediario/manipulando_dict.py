pessoa = {

}
print(pessoa)
print()
key = 'nome'
key = 'nome_completo' #chave dinamica, eu preciso alterar apenas a atribuição a "key"
#ao inves de mudar todo lugar que tem "pessoa['nome']".
#pessoa['nome'] = 'Lucas'
pessoa[key] = 'Lucas'
print(pessoa)
print(pessoa['nome_completo'])
print(pessoa[key])
#apagando chaves;
print()
pessoa['sobrenome'] = 'Araujo Souza'
print(pessoa)
print(' ------------------------- removido ------------------------')
del pessoa['sobrenome']
#print(pessoa['sobrenome'])

try:
    print(pessoa['sobrenome'])
except:
    print("key sobrenome removido")
    print(pessoa)

if pessoa.get('sobrenome') is None:
    print('pessoa["sobrenome"] não existe!')
else: print("Existe!    ")