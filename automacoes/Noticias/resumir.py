# pip install sumy
# pip install goose3
# pip install numpy

from goose3 import Goose
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.tokenizers import Tokenizer

# 1 - Coletando o artigo
def resumo(link):
    g = Goose()
    url = 'https://noticias.r7.com/internacional/reino-unido-enviara-navio-de-guerra-para-guiana-em-meio-a-tensao-com-venezuela-24122023'
    noticia = g.extract(url)
    # print(noticia.cleaned_text)

    # 2 - Trabalhando com a sumarização
    parser = PlaintextParser.from_string(
        noticia.cleaned_text,
        Tokenizer('portuguese')
    ) 
    sumarizador = LuhnSummarizer()
    resumo = sumarizador(
        parser.document,
        5 # Número de paragrafos do resumo
    )
    # print(resumo)
    frase = ''
    for setenca in resumo:
        frase += '\n'+str(setenca)
        
        # with(open("names.txt",'a')) as file:
        #     file.write(f'{name}\n')
        
           
            