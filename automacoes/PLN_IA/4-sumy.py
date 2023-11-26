# pip install sumy

from goose3 import Goose
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.luhn import LuhnSummarizer

# 1 - Coletando o artigo
g = Goose()
url = 'https://olhardigital.com.br/2023/08/09/ciencia-e-espaco/por-que-e-importante-criar-uma-rotina-de-sono/'
noticia = g.extract(url)
print(noticia.cleaned_text)

# 2 - Trabalhando com a sumarização