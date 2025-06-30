""" EX03 """


def soma_tupla(n1, n2, n3):
    return n1+n2+n3


nros = (1, 2, 3)

print(f"Soma = {soma_tupla(*nros)}")


def soma_tupla_melhorada(*nums):
    return sum(nums)


nros = (1, 2, 3, 4, 5)

print(f"Soma = {soma_tupla_melhorada(*nros)}")
