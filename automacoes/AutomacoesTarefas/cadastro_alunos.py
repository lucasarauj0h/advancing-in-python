import pyautogui
from time import sleep
password = open('automacoes\AutomacoesTarefas\lunos.txt', 'r').read()
print(password)
with open('automacoes\AutomacoesTarefas\lunos.txt', "r", encoding="utf-8") as file:
    for line in file:
        print('a')
        aluno = line.split(',')[0]
        email = line.split(',')[1]
        
        pyautogui.click(140,19,duration=1)
        pyautogui.click(300,288,duration=1)
        pyautogui.write(aluno)
        pyautogui.click(300,328,duration=1)
        pyautogui.write(email)
        pyautogui.click(300,350,duration=1)
        
        
        