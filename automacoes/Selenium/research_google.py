from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - Termo de Pesquisa
term = input("Digite o que deseja pesquisar:\n")
list_results = []

# 2 - Iniciando o driver
browser = webdriver.Edge()
browser.get('https://www.google.com.br/')

# 3 - Encontrando o elemento
elem = browser.find_element(
    By.XPATH,
    "//textarea[@aria-label='Pesquisar']"
)

# 4 - Enviando termo para pesquisa
elem.send_keys(term)
elem.send_keys(Keys.ENTER)
time.sleep(3)

# 5 - Retornando a quantidade de registros:
results = browser.find_element(By.ID, 'result-stats').text
print(f'Foram encontrados {results}resultados')

# 6 - Retornando o número de paginas
frase = results
frase = int(frase.split(' ')[1].replace('.',''))
pages = int(frase/10)
print(f'Total de paginas: {pages}')

while True:
    # Armazena a posição vertical antes de rolar
    antes_rolar = browser.execute_script("return window.pageYOffset;")
    
    # Executa um script JavaScript para rolar a página
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Aguarda um curto período para a página carregar ou adicione lógica para verificar o carregamento de elementos específicos
    time.sleep(1)  # Aguarda 1 segundo (pode ser ajustado de acordo com a velocidade de carregamento da página)
    
    # Armazena a posição vertical após rolar
    depois_rolar = browser.execute_script("return window.pageYOffset;")
    
    # Se não houver mais rolagem possível (posição vertical não mudou após rolar), saia do loop
    if antes_rolar == depois_rolar:
        break

# 8 - Recuperando informações

divs = browser.find_elements(
    By.XPATH,
    '//div[@class="yuRUbf"]'
)
for div in divs:
    name = div.find_element(By.TAG_NAME, 'h3')
    link = div.find_element(By.TAG_NAME, 'a')
    result = "%s,%s" %(name.text, link.get_attribute('href'))
    print(result)
    list_results.append(result)
    
# 9 - Salvando em um arquivo txt
with open('automacoes/Selenium/results_terms.txt', 'w', encoding='utf-8') as file:
    for result in list_results:
        file.write("%s\n" % result)
        
        
print(f'Foram encontradas {len(list_results)} resultados na pesquisa.')
browser.quit()