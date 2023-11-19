from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - Acessando o servidor web 
browser = webdriver.Edge()
browser.get('https://registro.br')

# 2 - Lista de dominios
domains = [
    'botscompython',
    'meta',
    'databot',
    'linkedin',
    'pythonbootcamp'
]

file = open('automacoes/Selenium/domains.txt', 'w', encoding='utf-8')
# 3 - Manipulando elementos

for domain in domains:
    elem = browser.find_element(By.ID, 'is-avail-field') # Para acessar a barra de busca
    elem.clear() # Para limpar a barra de busca
    elem.send_keys(domain) # Escreva na barra
    elem.send_keys(Keys.ENTER) # Enter
    time.sleep(5) # Esperando 5s para carregar.
    
    # 4 - Analisando os resultados
    results = browser.find_elements(By.TAG_NAME, 'strong')
    text = f'Dominio {results[1].text} está {results[2].text} para registro\n'
    print(text)
    file.write(text)

file.close()
browser.quit()

