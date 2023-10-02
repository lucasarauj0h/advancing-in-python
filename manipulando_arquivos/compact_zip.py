import glob, os, zipfile

# 1 pegando o diretório de trabalho atual
os.getcwd()

# 2 - pegando todos os arquivos txt

for file in glob.glob('*.txt'):
    print(file)
    
# 3 - pegando todos os arquivos csv
for file in glob.glob('*.csv'):
    print(file)
    
# 4 - compactando (arquivos txt)
with zipfile.ZipFile('names.zip', 'w') as zip:
    for file in glob.glob('*.txt'):
        zip.write(file)
        
# 5 - compactando (arquivos csv)
with zipfile.ZipFile('dados.zip', 'w') as zip:
    for file in glob.glob('*.csv'):
        zip.write(file)
        
# 6 - compactando todos os arquivos 
with zipfile.ZipFile('code.zip', 'w') as zip:  
    for file in glob.glob('*'):
        zip.write(file)
        
