from email.message import EmailMessage
import smtplib
import ssl
import sys

# Coletando a senha para acesso ao gmail via smt
caminho = r'C:\Users\Lucas\OneDrive\Documentos\password.txt'

try:
    with open(caminho, 'r') as arquivo:
        password = arquivo.read()
except FileNotFoundError:
    print(f'O arquivo em {caminho} não foi encontrado.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

from_email = 'saculrp06@gmail.com'
to_email = 'saculrp06@gmail.com'

# Assunto
subject = 'Proposta de parceria'

# Corpo
body =  open('automacoes\AutomacoesTarefas\corpo.txt', 'r', encoding='utf-8').read()


# Montando a estrutura do e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
# Definindo o conteudo do corpo
message.set_content(body)
safe = ssl.create_default_context()

# Envio de e-mail

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    ) 