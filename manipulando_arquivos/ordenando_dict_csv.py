courses = []

with open("courses.csv", 'r', encoding='utf-8') as file:
    for line in file:
        language, category = line.rstrip().split(',')
        course = {}
        course["language"] = language
        course["category"] = category
        courses.append(course)       
        
print(courses)

def get_language(course):
    return course['language']

def get_category(course):
    return course['catergory']
#para ordenar dicionarios, precisamos retornar a chave para que ele ordene, em uma função
#é necessário uma função para que o metodo sorted saiba qual a key de cada dicionário
#ele deverá retornar.
for course in sorted(courses, key= lambda course: course['category']):
    print(f"{course['language']} - {course['category']}") #iterando pelos dicionarios da lista