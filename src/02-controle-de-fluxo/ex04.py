""" EX04 """

cod = input("Informe o código identificador: ")

erros = []
LEN = len(cod)

TAM_INVALIDO = LEN != 7
INI_INVALIDO = cod[0] != 'B' or cod[1] != 'R'

INDICE = 2
NUM_INVALIDO = 0
while INDICE < 6 and not TAM_INVALIDO:
    if cod[INDICE] < '0' or cod[INDICE] > '9':
        NUM_INVALIDO = 1
        break
    INDICE += 1

FIM_INVALIDO = cod[LEN-1] != 'X'

if TAM_INVALIDO:
    erros.append("O código deve ter 7 caracteres.")
if INI_INVALIDO:
    erros.append("O código deve iniciar com 'BR'.")
if NUM_INVALIDO:
    erros.append("Os caracteres 3 à 6 devem ser números de 0 a 9.")
if FIM_INVALIDO:
    erros.append("O código deve terminar com 'X'.")

if len(erros) != 0:
    print(erros)
else:
    print("Código válido.")
