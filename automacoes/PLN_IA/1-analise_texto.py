import os
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


# nltk.download('punkt')

# 1 - Importando o texto
with open(os.path.join('automacoes/PLN_IA/data', 'texto.txt', ), 'r', encoding='utf-8') as file:
    texto = file.read()
    # print(texto)

# 2 - Tokenizando o texto (separando por palavras, ou setença (ponto final))
sent_tokens = sent_tokenize(texto)
print(sent_tokens)
print(len(sent_tokens))

word_tokens = word_tokenize(texto)
print(word_tokens)
print(len(word_tokens))

# 3 - Frequencia de distribuição
fdist = FreqDist(word_tokens)
print(fdist)
print(fdist.most_common(10))
fdist.plot(10)

# 4 - WordCloud / WordCloud Customizado
def plot_cloud(wordcloud):
    plt.figure(figsize=(40,30))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    random_state = 1,
    background_color= 'salmon',
    colormap='Pastel1',
    collocations=False,
    stopwords = STOPWORDS
).generate(texto)

# plot_cloud(wordcloud)

mask = np.array(
    Image.open('automacoes/PLN_IA/data/upvote.png')
)

print(mask)
wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    random_state = 1,
    background_color= 'salmon',
    colormap='Pastel1',
    collocations=False,
    stopwords = STOPWORDS,
    mask = mask
).generate(texto)

plot_cloud(wordcloud)
print(' ')