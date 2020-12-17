import numpy as np

# Geração de números aleatórios no numpy
# Geração de uma semente

np.random.seed(10)

# Float
arr = np.random.rand(6)*100
arr = np.random.randn(6)*100 # numeros negativos
print(arr)

# Int
arr = np.random.randint(1,20,12)

# Unique
print(np.unique(arr,return_counts=True)) # Retorna número de vezes que o número aparece

print(arr)

# Operações com arrays
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.astype(str))

mtz = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# Operações sobre todos os elementos da matriz
print(mtz.sum())

# Operações em cada coluna da matriz
print(mtz.sum(axis=0)[0])

# Operações em cada linha da matriz
print(mtz.sum(axis=1))
print(mtz.sum(axis=1)[2])