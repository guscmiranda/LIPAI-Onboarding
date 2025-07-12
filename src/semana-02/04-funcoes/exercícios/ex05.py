""" EX05 - Calculadora de IMC"""


def calcular_imc(individuo):
    peso = individuo['peso']
    altura = individuo['altura']
    return peso / (altura * altura)


def obter_classificacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25.0 <= imc <= 29.9:
        return "Excesso de peso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade de Classe 2"
    elif imc >= 40.0:
        return "Obesidade de Classe 3"


def situacao_individuo(imc):
    if imc < 18.5:
        return "Ganhar peso"
    elif 18.5 <= imc <= 24.9:
        return "Normal"
    elif imc > 24.9:
        return "Perder peso"


individuo = {
    'altura': float(input("Informe a altura(m): ")),
    'peso': float(input("Informe o peso(Kg): "))
}

imc = calcular_imc(individuo)
print(f"IMC: {imc:.2f}")
print("Classificação:", obter_classificacao(imc))
print("Situação:", situacao_individuo(imc))
