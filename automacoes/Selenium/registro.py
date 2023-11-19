from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - Acessando o servidor web 
browser = webdriver.Edge()
browser.get('https://registro.br')

# 2 - Acessando a barra de busca e procurando um dominio 
elem = browser.find_element(By.ID, 'is-avail-field')
elem.clear()
elem.send_keys('botscompython.com.br')
elem.send_keys(Keys.ENTER)

time.sleep(5)

# 3 - Analisando os resultados
results = browser.find_elements(By.TAG_NAME, 'strong')
# import pdb
# pdb.set_trace()

print(f'O dominio: {results[1].text} está {results[2].text} para registro')
browser.save_screenshot('automacoes/Selenium/dominio.png')


browser.quit()

