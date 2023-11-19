from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Edge()

# 1- Acessando a página
browser.get('http://www.amazon.com.br')

# 2 - Acessando elementos de uma página
# Acessando a barra de pesquisa da pagina da amazon.
elem = browser.find_element(By.ID, 'twotabsearchtextbox')
elem.send_keys('ps5')
elem.send_keys(Keys.ENTER)

# browser.quit()