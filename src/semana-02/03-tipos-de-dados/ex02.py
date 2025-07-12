""" EX02 """

meses = ('Janeiro', 'Feveireiro', 'Março',
         'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro')

mes = int(input("Digite um mês do ano, em formato númerico 1,2,3...,12: "))

if 0 < mes < 13:
    print(f"O mês {mes} é {meses[mes-1]}")
else:
    print("O número informado não corresponde a um mês, tente números de 1 a 12")
