""" EX03 """

meses = {
    1: 'Janeiro', 2: 'Feveireiro', 3: 'Março',
    4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}

mes = int(input("Digite um mês do ano, em formato númerico 1,2,3...,12: "))

if mes in meses:
    print(f"O mês {mes} é {meses[mes]}")
else:
    print("O número informado não corresponde a um mês, tente números de 1 a 12")
