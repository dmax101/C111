## Danilo Vidal Ribeiro
## Matrícula 1411

import numpy as np

paises = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

paises = np.char.chararray.strip(paises, " ").astype(np.str)

# Questão 1

arr = paises[:, [0, 1, 2, 3]]
print("Questão 01 -----------------------------------------")
print(arr)
print("----------------------------------------------------")

# Questão 2

unique, counts = np.unique(paises[:, 1], return_counts=True)

print("Questão 02 -----------------------------------------")
print("NUM\t| Regiões\t\t\t\t")
for i in range(len(unique)):
    print("{}\t| {}: {}".format(i + 1, unique[i], counts[i]))

print("----------------------------------------------------")

# Questão 3

#percentage = paises[:, 9].astype(dtype=np.float64).mean(axis=0)

arr = np.array(paises[:, 9], dtype=np.float)

percentage = arr.mean(axis=0)

print("Questão 03 -----------------------------------------")
print('Taxa média de alfabetização mundial: {:.2f}%.'.format(percentage))
print("----------------------------------------------------")

# Questão 4

print("Questão 04 -----------------------------------------")
arr = paises[:, 1]
northern_america = len(arr[arr == "NORTHERN AMERICA                   "])

print('Na América do Norte existem {} países.'.format(northern_america))
print("----------------------------------------------------")

# Questão 5

arr = paises[:, [0, 1, 8]]
arr_names = arr[arr[:, 1] == "LATIN AMER. & CARIB", 0]
arr_values = np.array(arr[arr[:, 1] == "LATIN AMER. & CARIB", 2], dtype=np.float64)

index = arr_values.argmax(axis=0)

print("Questão 05 -----------------------------------------")
print('O país da América do Sul e Caribe com maior renda per capita é o "{}" com renda de $ {:0.2f}.'.format(arr_names[index], arr_values[index]))
print("----------------------------------------------------")


