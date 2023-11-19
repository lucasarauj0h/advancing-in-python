from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Edge()

# 1- Acessando a página
browser.get('http://www.amazon.com.br')

# 2 - Acessando elementos de uma página
# Acessando a barra de pesquisa da pagina da amazon.
elem = browser.find_element(By.ID, 'twotabsearchtextbox')
elem.send_keys('ps5')
elem.send_keys(Keys.ENTER)
time.sleep(2)

# 3 - Encontrando os elementos de todos os resultados
element = browser.find_element(
    By.CSS_SELECTOR,
    'div.s-main-slot.s-result-list.s-search-results.sg-row'
)
print(element)
time.sleep(2)
browser.quit()