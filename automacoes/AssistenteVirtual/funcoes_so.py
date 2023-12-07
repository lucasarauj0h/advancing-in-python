import os
from datetime import datetime

def verifica_hora():
    hora = datetime.now().strftime('%H:%M') # Definindo a formatação do datetime, apenas em horas e minutos
    frase = f'Agora são: {hora}'
    return frase
    
def desligar_hora():
    os.system('shutdown /s /t 3600')
    frase = f'Agendado para desligar em uma hora'
    return frase
    
def desligar_meiahora():
    os.system('shutdown /s /t 1800')
    frase = f'Agendado para desligar em uma meia hora'
    return frase
    
def cancel_desligar():
    os.system('shutdown /a')
    frase = f'desligamento cancelado'
    return frase