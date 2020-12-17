import numpy as np

space = np.loadtxt('space.csv', delimiter=';',dtype=str, encoding='utf-8')

print(np.char.find(space, '1984'))