""" EX03 """

cod = input("Informe o código identificador: ")

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


if TAM_INVALIDO or INI_INVALIDO or NUM_INVALIDO or FIM_INVALIDO:
    print("Código inválido")
else:
    print("Código válido.")
