# Enviando e-mail com o corpo em uma estrutura HTML
from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

password = open('automacoes\AutomacoesTarefas\password.txt', 'r').read()
print(password)
from_email = 'saculrp06@gmail.com'
to_email = 'saculrp06@gmail.com'

# Assunto
subject = 'Proposta de parceria'

# Corpo
body =  open('automacoes\AutomacoesTarefas\HTML.txt', 'r', encoding='utf-8').read()

# Montando a estrutura do e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
# Definindo o conteudo do corpo
message.set_content(body, subtype='html')
safe = ssl.create_default_context()

# Adicionando anexo
anexo = 'automacoes\AutomacoesTarefas\password.txt'
print(mimetypes.guess_type(anexo)[0])
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )
# Envio de e-mail


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )