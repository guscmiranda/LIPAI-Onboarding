""" EX03 """


def soma_tupla(n1, n2, n3):
    return n1+n2+n3


nros = (1, 2, 3)

print(f"Soma = {soma_tupla(*nros)}")


def soma_tupla_melhorada(*nums):
    soma = 0
    for num in nums:
        soma += num
    return soma


nros = (1, 2, 3, 4, 5, 6)

print(f"Soma = {soma_tupla_melhorada(*nros)}")
