# pip install sumy

from goose3 import Goose
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.tokenizers import Tokenizer

# 1 - Coletando o artigo
g = Goose()
url = 'https://olhardigital.com.br/2023/08/09/ciencia-e-espaco/por-que-e-importante-criar-uma-rotina-de-sono/'
noticia = g.extract(url)
print(noticia.cleaned_text)

# 2 - Trabalhando com a sumarização
parser = PlaintextParser.from_string(
    noticia.cleaned_text,
    Tokenizer('portuguese')
) 
sumarizador = LuhnSummarizer()
resumo = sumarizador(
    parser.document,
    2 # Número de paragrafos do resumo
)
for setenca in resumo:
    print(setenca)