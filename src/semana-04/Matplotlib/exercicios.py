import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import matplotlib.style as st
import numpy as np
import pandas as pd

data = pd.read_csv(
    'src/semana-04/Pandas/exercicios/classification_results_trial_0001.csv')

plt.style.use("seaborn-v0_8")

# 1. Você continuará usando o arquivo CSV que contém os resultados do modelo de classificação de imagens como "benigno" ou "maligno”

# 1.1. Crie um gráfico de barras mostrando a contagem de imagens para real_class (quantas "benigno" e "maligno" são na realidade).

plt.figure('Figura 1.1', figsize=(8, 5))
plt.title("Real: malign vs benign", fontsize=14)

x_labels = ["malign", "benign"]

malign_size = (data["real_class"] == "malign").sum()
benign_size = (data["real_class"] == "benign").sum()

plt.bar(x_labels, [malign_size, benign_size],
        color=["#8A2BE2", "#20B2AA"], edgecolor="black")
plt.ylabel("Quantidade de imagens")

plt.show()

# 1.2. Crie outro gráfico de barras mostrando a contagem de imagens para predicted_class (quantas "benigno" e "maligno" o modelo previu).

plt.figure('Figura 1.2', figsize=(8, 5))
plt.title("Predicted: malign vs benign")

x_labels = ["malign", "benign"]

malign_size = (data["predicted_class"] == "malign").sum()
benign_size = (data["predicted_class"] == "benign").sum()

plt.bar(x_labels, [malign_size, benign_size], color=[
        "#8A2BE2", "#20B2AA"], edgecolor="black")
plt.ylabel("Quantidade de imagens")
plt.show()

# 1.3. Crie um histograma para a coluna prob_benign (probabilidade de ser "benigno").

plt.figure('Figura 1.3', figsize=(8, 5))
plt.hist(data["prob_benign"], bins=10, color="#20B2AA", edgecolor="black")

plt.title("Histograma: Probabilidade de ser 'benigno'")
plt.xlabel("Probabilidade (prob_benign)")
plt.ylabel("Frequência")

plt.show()

# 1.4. Crie um histograma para a coluna prob_malign (probabilidade de ser "maligno").

plt.figure('Figura 1.4', figsize=(8, 5))
plt.hist(data["prob_malign"], bins=10, color="#8A2BE2", edgecolor="black")

plt.title("Histograma: Probabilidade de ser 'maligno'")
plt.xlabel("Probabilidade (prob_malign)")
plt.ylabel("Frequência")

plt.show()

# 1.5. Crie um gráfico de dispersão (scatter plot) onde o eixo X pode ser prob_benign e o eixo Y pode ser prob_malign.
# Pinte os pontos de forma diferente com base se o modelo acertou ou errou a predição da imagem.
# Isso pode ajudar a visualizar se os erros ocorrem em regiões de menor confiança (probabilidades próximas de 0.5).

prob_benign = data["prob_benign"]
prob_malign = data["prob_malign"]

colors = (data["real_class"] == data["predicted_class"]).map(
    {True: "#20B2AA", False: "#FF6347"})

plt.figure('Figura 1.5', figsize=(8, 5))
plt.scatter(prob_benign, prob_malign, c=colors)

plt.title("Dispersão: Probabilidades com base em acertos e erros")
plt.xlabel("Probabilidade de ser Benigno (prob_benign)")
plt.ylabel("Probabilidade de ser Maligno (prob_malign)")

plt.show()

# 1.6. Qual tipo de erro é mais comum (Falso Positivo ou Falso Negativo)? Crie um gráfico que ajude a visualizar isso. Dada a natureza dos dados médicos, qual tipo de erro seria mais preocupante e por quê?

fp = ((data['real_class'] == 'benign') & (
    data['predicted_class'] == 'malign')).sum()
fn = ((data['real_class'] == 'malign') & (
    data['predicted_class'] == 'benign')).sum()

plt.figure('Figura 1.6', figsize=(8, 5))
x_labels = ["Falso Positivo", "Falso Negativo"]
plt.bar(x_labels, [fn, fp],
        color=["#8A2BE2", "#20B2AA"], edgecolor="black")
plt.ylabel("Quantidade de imagens")

plt.show()

# 2. Dado o arquivo metrics.csv utilizando o Pandas e Matplotlib crie um gráfico semelhante ao de referência com as curvas de acurácia e perda do conjunto de treinamento e validação.

metrics = pd.read_csv('src/semana-04/Matplotlib/metrics.csv')

fig = plt.figure('Figura 2.0', figsize=(8, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.plot(metrics.index, metrics["train_acc"],
         label="train", color="#3CB371", linewidth=2)
ax1.plot(metrics.index, metrics["val_acc"],
         label="valid", color="#9370DB", linewidth=2)
ax1.set_title("model accuracy", fontsize=12)
ax1.set_xlabel("epoch")
ax1.set_ylabel("accuracy")
ax1.legend()

ax2.plot(metrics.index, metrics["train_loss"],
         label="train", color="#FF6347", linewidth=2)
ax2.plot(metrics.index, metrics["val_loss"],
         label="valid", color="#4682B4", linewidth=2)
ax2.set_title("model loss", fontsize=12)
ax2.set_xlabel("epoch")
ax2.set_ylabel("loss")
ax2.legend()

plt.show()
