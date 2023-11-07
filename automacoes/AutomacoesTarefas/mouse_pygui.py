import pyautogui

# 1 - Tamanho da tela
print(pyautogui.size())

# 2 - Pegar posição atual da tela
print(pyautogui.position())

# 3 - app para ver a posição em tempo real do mouse (no terminal)
# python
# from pyautogui import mouseInfo
# mouseInfo()

# 4 - Movendo o cursor do mouse
pyautogui.moveTo(1017, 95, 0.4)

# 5 - Realizando um scroll
pyautogui.moveTo(681,309)
pyautogui.scroll(-2000)