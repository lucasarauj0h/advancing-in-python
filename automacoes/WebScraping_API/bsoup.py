from bs4 import BeautifulSoup

# 1 - Importando a pagina HTML
with open('automacoes/WebScraping_API/index.html', 'r', encoding='utf-8') as file_html:
    content = file_html.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    print(soup)
    
# 2 - Recuperar títulos das vagas:
# Encontrando a primeira 'vaga' que aparece
vagas = soup.find('h5')
print(vagas)
# Encontrando todas as vagas disponiveis
cursos = soup.find_all('h5')
print(cursos)
for curso in cursos:
    print(curso.text)