from time import process_time
from numpy.random import default_rng
import numpy as np

# Tipos de arrays: ndarrays -> array de N dimensoes
# 1-D array -> 1 dimensão: vetores
# 2-D array -> 2 dimensões: matrizes
# 3-D array -> 3 dimensões: tensores

arr = np.array([[1, 2, 3], [3, 2, 1]])
print('arr', arr, '\n-------------------------------------------')

vzeros = np.zeros(shape=(5, 3, 6))
print('vzeros', vzeros, '\n------------------------------------------------')

vones = np.ones((3, 3))
print('vones', vones, '\n------------------------------------------------')

vempty = np.empty((2, 2))
print('vempty', vempty, '\n------------------------------------------------')

varange = np.arange(start=10, stop=101, step=30)
print('varange', varange, '\n------------------------------------------------')

vlinspace = np.linspace(start=0, stop=100, num=20, endpoint=True, retstep=True)
print('vlinspace', vlinspace, '\n------------------------------------------------')


print('vzeros infos\n', vzeros.shape, '\n', vzeros.size, '\n', vzeros.ndim,
      '\n------------------------------------------------')

# Vetor (1-D) para Matriz (2-D)

v = np.array([1, 2, 3])
print(v.ndim)

m = v[np.newaxis, :]
print(m.shape, m.ndim, '\n', m)

m2 = v[:, np.newaxis]
print(m2)

# Concantenando arrays

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.concatenate((a, b))
d = np.concatenate((b, a))
print(c, '!=', d)

# Consulta em Arrays

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print('------------------------')
maior_8 = a[a > 8]
pares = a[a % 2 == 0]
print(maior_8)
print(pares)
print('------------------------')

# Operações com arrays
# a = np.array([1,2,3])
# a.sum()
# a.max()
# a.min()
# a.mean

# Gerando amostras aleatórias
rng = default_rng()
aleatorio = rng.integers(10, size=(2, 4))
print(aleatorio)

# Diferenças entre Arrays e Listas
a = np.array([1, 2, 3, 4, 5, 'oi', 7, 8])  # Apenas 1 tipo no arr
print(a)
print(type(a))
print('------------------------')
lista_a = [1, 2, 3, 4, 5, 'oi', 7, 8]      # Aceita tipos diferentes
print(lista_a)
print(type(lista_a))
print('------------------------')

# Comparando o processamento
lista_a = list(rng.integers(10, 100, 10000000))
lista_b = list(rng.integers(10, 100, 10000000))
c = []
t1 = process_time()
for i in range(len(lista_a)):
    c.append(lista_a[i]*lista_b[i])
t2 = process_time()
print('Tempo lista:', t2-t1)

arr_a = rng.integers(10, 100, 10000000)
arr_b = rng.integers(10, 100, 10000000)
t1 = process_time()
arr_c = arr_a*arr_b
t2 = process_time()
print('Tempo arr', t2-t1)
