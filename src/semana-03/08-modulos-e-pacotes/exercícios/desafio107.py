from moeda import *

valor = float(input("Digite o valor: R$"))
print(f"Aumento de 10%: {aumentar(valor, 10)}")
print(f"Diminuindo 20%: {diminuir(valor, 20)}")
print(f"Dobro: {dobro(valor)}")
print(f"Metade: {metade(valor)}")
