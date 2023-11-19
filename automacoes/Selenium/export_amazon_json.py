from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

# 0 - Acessando o arquivo json para exportar a automação da pesquisa
with open('automacoes/Selenium/data_amazon.json', 'w') as f:
    json.dump([],f)

def write_json(new_data, filename='automacoes/Selenium/data_amazon.json'):
    # Abrindo o arquivo json em nosso diretório
    with open(filename, 'r+') as file:
        # Carregando o arquivo ja existente no json para salva-lo em linguagem python
        file_data = json.load(file)
        # Adiciona um novo dicionario em python, junto aos já presente no json
        file_data.append(new_data)
        # Retorna o cursor para a linha 1
        file.seek(0)
        # Adiciona novamente todos os dicionarios ao json [incluindo aquele que foi adicionado]
        json.dump(file_data, file, indent=4)

research = 'ps5'

browser = webdriver.Edge()

# 1- Acessando a página
browser.get('http://www.amazon.com.br')

# 2 - Acessando elementos de uma página
# Acessando a barra de pesquisa da pagina da amazon.
elem = browser.find_element(By.ID, 'twotabsearchtextbox')
elem.send_keys(research)
elem.send_keys(Keys.ENTER)
time.sleep(2)

isNextDisable = False

while not isNextDisable:
# 3 - Encontrando os elementos de todos os resultados
    element = browser.find_element(
        By.CSS_SELECTOR,
        'div.s-main-slot.s-result-list.s-search-results.sg-row'
    )
    time.sleep(2)


    # 4 - Encontrar informações dos produtos
    items = element.find_elements(
        By.XPATH,
        '//div[@data-component-type="s-search-result"]'
    )
    print(len(items))

    # 5 - Coletando o nome e o preço dos produtos
    for item in items:
        title = item.find_element(By.TAG_NAME, 'h2').text
        price = ''
        img = ''
        link = item.find_element(
            By.CLASS_NAME,
            'a-link-normal'
        ).get_attribute('href')
        
        try: 
            price = item.find_element(
                By.CLASS_NAME,
                'a-price'
            ).text.replace('\n','.')
        except:
            pass
        
        try:
            img = item.find_element(
                By.CLASS_NAME,
                's-image'
            ).get_attribute('src')
        except:
            pass
        
        print(f'Titulo: {title}')
        print(f'Preço {price}')
        print(f'Link: {link}')
        print(f'Imagem {img}\n')
        
        write_json(
            {
                "title": title,
                "price": price,
                "link": link,
                "img": img     
            }
        )
        
    try:
        # Encontre o botão para proxima página
        next_btn = browser.find_element(
            By.CLASS_NAME,
            's-pagination-next'
        )
        # Pegue a classe do botão proxima pagina e verifique se há proxima pagina
        next_class = next_btn.get_attribute('class')
        # Caso não tenha poxima pagina, finalize o loop
        if 's-pagination-disable' in next_class:
            isNextDisable = True
            break
        # Caso tenha, clique na proxima pagina
        next_btn.click()
    # Caso de erro, encerre o loop
    except Exception as e:
        print(e)
        isNextDisable = True
        

browser.quit()