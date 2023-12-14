import urllib.request
import json



# Filmes mais populares
url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=cad33cb92ca0fa9baf86ee9240dc74d4'

# Filmes de animação
url = 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=cad33cb92ca0fa9baf86ee9240dc74d4'
# url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=cad33cb92ca0fa9baf86ee9240dc74d4'

resposta = urllib.request.urlopen(url)


print(resposta)

dados = resposta.read()
dados_json = json.loads(dados)

# print(dados_json['results'])