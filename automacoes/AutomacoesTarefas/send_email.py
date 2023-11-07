from email.message import EmailMessage
import smtplib
import ssl

password = open('automacoes\AutomacoesTarefas\password.txt', 'r').read()
print(password)
from_email = 'saculrp06@gmail.com'
to_email = 'saculrp06@gmail.com'

# Assunto
subject = 'Curso Python'

# Corpo
body = '''
A melhor forma de prever o futuro é cria-lo
Aprendendo a linguagem python
'''

message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

# Setando o corpo da mensagem
message.set_content(body)
safe = ssl.create_default_context()

# Enviando o e-mail

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )