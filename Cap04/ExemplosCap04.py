import numpy as np

#1 Array tamanho 21 linearmente espaçados

arr01 = np.linspace(0, 1, 21)

print(arr01)

#2 Array par 0 a 50 e outro 0 até 50
arr02 = np.arange(0, 51, 2) # 0 até 50 par
arr03 = np.arange(100, 50, -2) # 100 até 50 par

arr04 = np.sort(np.concatenate((arr02, arr03))) # Ordenar

print(arr04)

#3 Ordem decrescente
arr05 = np.flip(arr04)

print(arr05)

#4 de uns 3x4
arr06 = np.ones([3,4])

print(arr06)

arr07 = np.reshape(arr06,12)

print(arr07)