import hashlib
#hashlib é uma biblioteca de criptografia 

# 1 - Verificar os algoritmos disponíveis
print(hashlib.algorithms_available) #todos os algoritmos 
print(hashlib.algorithms_guaranteed) #de acordo com o sistema operacional

# 2 - Utilizando Sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é cria-lo".encode()
algorithm.update(message)
print(algorithm.hexdigest())