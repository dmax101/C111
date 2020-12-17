# Nome: Danilo Vidal Ribeiro
# Matricula: 1411

# Para esta questão, faça o que se pede em ordem:
# a. Crie dois NumPy Arrays 1-D com 4 nomes de pessoas cada;
# b. Em seguida, concatene-os em um só Array;
# c. Transforme o Array final em um Array 2-D com mais colunas do que linhas;
# d. Por fim, ordene os nomes do Array 2-D em ordem decrescente;


import numpy as np

# a)
print('Questão 2. a) -------------')
arr01 = np.array(["Danilo", "Sofia", "Flavia", "Juliana"])
arr02 = np.array(["Viviane", "Joana", "Luana", "Júlia"])
print(arr01, arr02)

# b)
print('Questão 2. b) -------------')
arr03 = np.concatenate((arr01,arr02))
print(arr03)

# c)
print('Questão 2. c) -------------')
arr04 = arr03.reshape(2,4)
print(arr04)

# d)
print('Questão 2. d) -------------')
arr05 = np.flip(np.sort(arr04))
print(arr05)