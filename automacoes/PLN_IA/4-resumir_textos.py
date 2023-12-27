# pip install sumy

from goose3 import Goose
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.tokenizers import Tokenizer

# 1 - Coletando o artigo
g = Goose()
url = 'https://www.infomoney.com.br/guias/debentures/'
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