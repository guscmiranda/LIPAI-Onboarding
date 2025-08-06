import matplotlib.style as st
import matplotlib.pyplot as plt
import numpy as np

# INTRODUÇÃO
t = np.linspace(0, 2*np.pi, 500)
y = np.cos(4*t)
y1 = np.sin(4*t)

plt.figure("Cosseno", figsize=(5, 4))
plt.plot(t, y)
plt.title("Gráfico do Cosseno")
plt.xlabel("Tempo(s)")
plt.ylabel("Amplitude")


plt.figure("Seno")
plt.plot(t, y1)
plt.title("Gráfico do Seno")
plt.xlabel("Tempo(s)")
plt.ylabel("Amplitude")
# plt.show()

# Múltiplos Gráficos em uma mesma figura

t = np.linspace(0, 2*np.pi, 100)
y = np.cos(t)
y1 = np.sin(t)

plt.figure("Gráfico", figsize=(6, 4))
plt.plot(t, y)
plt.plot(t, y1)
plt.title("Gráficos Seno e Cosseno")
plt.grid()
plt.show()

# Vários Gráficos em uma mesma figura com subplot
x = np.linspace(0, 2*np.pi, 500)
c = np.cos(x)
s = np.sin(x)

plt.figure("Gráficos", figsize=(8, 4))
plt.subplots_adjust(
    left=0.12,
    right=0.95,
    top=0.9,
    bottom=0.14,
    wspace=0.438,
    hspace=0.4
)

ax1 = plt.subplot(1, 2, 1)
plt.plot(x, c)
ax1.set_title("Gráfico do Cosseno")
ax1.set_xlabel("Eixo de Tempo")
ax1.set_ylabel("Eixo de Amplitude")


ax2 = plt.subplot(1, 2, 2)
plt.plot(x, s)
ax2.set_title("Gráfico do Seno")
ax2.set_xlabel("Eixo de Tempo")
ax2.set_ylabel("Eixo de Amplitude")

plt.show()

# --------------------------------- #
x = np.arange(0, 5, 0.1)

y1 = x**2
y2 = x**5

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 4))
plt.suptitle("Gráficos com Subplots")
plt.subplots_adjust(
    left=0.093,
    right=0.948,
    top=0.8,
    bottom=0.148,
    wspace=0.348,
    hspace=0.824
)

axes[0, 0].plot(x, y1)
axes[0, 0].set_title("Função de Segundo Grau")
axes[0, 0].set_xlabel("Tempo")
axes[0, 0].set_ylabel("Amplitude")
axes[0, 0].grid(True)

axes[1, 1].plot(x, y2)
axes[1, 1].set_title("Função de Quinto Grau")
axes[1, 1].set_xlabel("Tempo")
axes[1, 1].set_ylabel("Amplitude")
axes[1, 1].grid(True)

# Customizando o Gráfico de Linha

x = np.linspace(0, 2*np.pi, 50)
y = np.cos(4*x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color='b', lw=0.8, marker='o', linestyle="solid")
plt.grid(True)
plt.title("Gráfico do Cosseno")
plt.xlabel("Tempo(s)")
plt.ylabel("Amplitude")
plt.show()

# Customizando as escalas dos eixos do gráfico

x = np.linspace(0, 2*np.pi, 300)
y = np.cos(3*x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y)

axe.set_title("Gráfico do Cosseno", fontsize=16)
axe.set_xlabel("Eixo X", fontsize=14)
axe.set_ylabel("Eixo Y", fontsize=14)

plt.xticks(np.arange(0, 2*np.pi+0.5, 0.5))
plt.yticks(np.arange(-1, 1.2, 0.2))

plt.grid(True)
plt.show()

# Aplicando diferentes estilos no gráfico

# plt.style.use("classic")
plt.style.use("ggplot")

x = np.linspace(0, 2*np.pi, 300)
y = np.cos(3*x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y)

axe.set_title("Gráfico do Cosseno", fontsize=16)
axe.set_xlabel("Eixo X", fontsize=14)
axe.set_ylabel("Eixo Y", fontsize=14)

plt.xticks(np.arange(0, 2*np.pi+0.5, 0.5))
plt.yticks(np.arange(-1, 1.2, 0.2))

plt.show()

# Identificando um ponto com linhas paraelas e marcador

plt.style.use("ggplot")

x = np.linspace(1, 5, 500)
y = np.log10(x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y, lw=1.2)
axe.set_xticks(np.arange(0, 5.5, 0.5))

axe.plot([0, 2.5], [0.4, 0.4], color='gray', linestyle="--", lw=0.8)
axe.plot([2.5, 2.5], [0, 0.4], color='gray', linestyle="--", lw=0.8)
axe.plot(2.5, 0.4, marker="o", color="gray")
plt.show()

# Inserindo texto no gráfico
plt.style.use("ggplot")

x = np.linspace(1, 5, 500)
y = np.log10(x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y, lw=1.2)
axe.set_xticks(np.arange(0, 5.5, 0.5))

axe.plot([0, 2.5], [0.4, 0.4], color='gray', linestyle="--", lw=0.8)
axe.plot([2.5, 2.5], [0, 0.4], color='gray', linestyle="--", lw=0.8)
axe.plot(2.5, 0.4, marker="o", color="gray")

axe.set_title("Gráfico Log")
axe.set_xlabel("Eixo X")
axe.set_ylabel("Eixo Y")

axe.text(2.6, 0.35, "P(2.5;0.4)")
axe.text(3, 0.42, "Logarítmo $y = log{10}x$", fontsize=10,
         bbox=dict(facecolor="red", alpha=0.5))
axe.annotate("P(2.5;0.4)", xy=(2.5, 0.4), fontsize=14, xytext=(0.5, 0.5),
             arrowprops=dict(facecolor="red"), color="r")
plt.show()
