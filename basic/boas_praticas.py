# constantes = 'variaveis' que não vão mudar. 
# LETRAS MAIUSCULAS PARA 'CONSTANTE'

velocidade = 60
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade >= RADAR_1:
    print('velocidade do carro passou do perimitido no radar 1')

if  local_carro >= ( LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) \
        and velocidade >= RADAR_1:
    print('carro multado em radar 1')

#metodo mais "clean"

vel_carro_permitido = velocidade >= RADAR_1
position_car = local_carro >= ( LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_permitido and position_car:
    print('carro multado em radar 2')
else:
    print('carro liberado')
