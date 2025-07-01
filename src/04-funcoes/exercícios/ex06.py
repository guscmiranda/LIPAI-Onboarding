""" EX06 - Aquário"""


def calcula_volume(aquario):
    comp = aquario['comprimento']
    alt = aquario['altura']
    larg = aquario['largura']
    return (comp*alt*larg) / 1000


def potencia_termostato(volume, temp_desejada, temp_ambiente):
    return volume * 0.05 * (temp_desejada - temp_ambiente)


def litros_filtragem(volume):
    print(f"A filtragem por hora deve ser de {volume*2} a {volume*3} L")


print("Informe as seguintes dimensões do aquário, em cm")

aquario = {
    'comprimento': float(input("Comprimento: ")),
    'altura': float(input("Altura: ")),
    'largura': float(input("Largura: ")),
}

temp_desejada = float(input("Digite a temperatura desejada (°C): "))
temp_ambiente = float(input("Digite a temperatura ambiente (°C): "))

vol = calcula_volume(aquario)
print("Volume =", vol, "L")

potencia = potencia_termostato(vol, temp_desejada, temp_ambiente)
print("A potência do termostato deve ser de", potencia, "watts")

litros_filtragem(vol)
