""" EX04 """


def soma(*args):
    s = 0
    for num in args:
        s += num
    return s


resultado = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Soma =", resultado)
