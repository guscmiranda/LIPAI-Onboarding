""" EX01 """
# solicite ao usuário 3 notas e apresente o resultado da média aritmética das notas

MEDIA = 0
CONT = 0
while CONT < 3:
    nota = float(input(f"Digite a nota {CONT + 1}: "))
    MEDIA += nota
    CONT += 1
MEDIA /= 3
print(f"A média resultante é: {MEDIA:.2f}")
