from moeda import *

valor = float(input("Digite o valor: R$"))
print(f"Aumento de 10%: {moeda(aumentar(valor, 10))}")
print(f"Diminuindo 20%: {moeda(diminuir(valor, 20))}")
print(f"Dobro: {moeda(dobro(valor))}")
print(f"Metade: {moeda(metade(valor))}")
