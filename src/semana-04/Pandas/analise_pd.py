import pandas as pd

data = pd.read_csv(
    'src/semana-04/Pandas/classification_results_trial_0001.csv')

print(data.info)
print("="*60)
print('1. Quantas imagens do conjunto são "benigno" e "maligno"?"')

print(data['real_class'].value_counts())
# benign = 0
# malign = 0
# for d in data['real_class']:
#     if d == 'benign':
#         benign += 1
#     else:
#         malign += 1
# print("Benign:", benign, "\nMalign:", malign)


print("="*60)
print("2. Identifique em quais imagens o modelo errou a predição")

erros = data[data['real_class'] != data['predicted_class']]
print("Erros:\n", erros)
print("Total de erros:", len(erros))

print("="*60)
print("3. Verifique se o modelo estava confiante mesmo quando errou a predição")

confianca = abs(erros['prob_malign'] - erros['prob_benign'])

print(f"{'Index':<6} | {'Confiança > 0.6':<10} | {'Confiança':<10}")
for id, conf in confianca.items():
    confiante = conf > 0.6
    print(f"{id:<8} {str(confiante):<18} {conf:.4f}")

print("="*60)
print("4. Calcule:\n"
      "Verdadeiros Positivos (TP) - real maligno, previsto maligno.\n"
      "Verdadeiros Negativos (TN) - real benigno, previso benigno.\n"
      "Falsos Positivos (FP) - real benigno, previsto maligno.\n"
      "Falsos Negativos (FN) - real maligno, previsto benigno.\n")
tp = data[(data['real_class'] == 'malign')
          & (data['predicted_class'] == 'malign')]

tn = data[(data['real_class'] == 'benign')
          & (data['predicted_class'] == 'benign')]

fp = data[(data['real_class'] == 'benign')
          & (data['predicted_class'] == 'malign')]

fn = data[(data['real_class'] == 'malign')
          & (data['predicted_class'] == 'benign')]
print('\nVerdadeiros Positivos (TP)\n', tp,)
print('\nVerdadeiros Negativos (TN)\n', tn)
print('\nFalsos Positivos (FP)\n', fp)
print('\nFalsos Negativos (FN)\n', fn)

print("="*60)
print("5. Calcule:\n"
      "Acurácia: (TP+TN)/(TP+TN+FP+FN)\n"
      "Precisão (Precision): TP/(TP+FP) (relevante para os casos preditos como positivos)\n"
      "Recall: TP/(TP+FN) (relevante para os casos reais positivos)\n"
      "Especificidade: TN/(TN+FP) (relevante para os casos reais negativos))\n")

TP = len(tp)
TN = len(tn)
FP = len(fp)
FN = len(fn)

acuracia = (TP + TN) / (TP + TN + FP + FN)
precisao = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0
especificidade = TN / (TN + FP) if (TN + FP) > 0 else 0

print(f"Acurácia: {acuracia:.4f}")
print(f"Precisão (Precision): {precisao:.4f}")
print(f"Recall (Sensibilidade): {recall:.4f}")
print(f"Especificidade: {especificidade:.4f}")

print("="*60)
print('6. Encontre as 5 imagens "benigno" com a menor probabilidade de serem "benigno" (prob_benign). O que isso pode indicar?')

df_benign = data[data['real_class'] == 'benign']
menores_prob_benign = df_benign.sort_values(by="prob_benign")
print(menores_prob_benign.head(5))

'''''
Indica que o modelo teve dificuldade em reconhecer corretamente essas amostras.
Isso pode ocorrer por motivos como: ruído, viés de dados de treinamento, características visuais atípicas.
Esses casos levam a falsos positivos, resultando em intervenções médicas desnecessárias
'''''

print("="*60)
print('7. Encontre as 5 imagens "maligno" com a maior probabilidade de serem "benigno" (prob_benign). O que isso pode indicar?')

df_malign = data[data['real_class'] == 'malign']
maiores_prob_malign = df_malign.sort_values(by="prob_malign")
print(maiores_prob_malign.head(5))

'''''
Indica que o modelo classificou, com alto nível de confiança, imagens de tumores malignos como benignos.
Isso caracteriza um falso negativo, podendo resultar no atraso do diagnóstico e, consequentemente, do tratamento
'''''
