""" EX02 """

notas = input("Digite as notas no formato: n1, n2, n3, ..., nm: ")
notas = notas.split(",")

notas = [float(nota) for nota in notas]

media = sum(notas) / len(notas)
print(f"A média resultante é: {media:.2f}")

if media >= 6:
    print("Aprovado")
elif 4 < media < 6:
    print("Recuperação")
else:
    print("Reprovado")
