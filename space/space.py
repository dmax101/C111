## Danilo Vidal Ribeiro
## Matrícula 1411

import numpy as np

space = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

#Num;Company Name;Location;Datum;Detail;Status Rocket; Cost;Status Mission

# Questão 01
unique, counts = np.unique(space[:, -1], return_counts=True)

percentage = counts[3] / len(space) * 100

print('QUESTÃO 01: Porcentagem de missões bem sucedidas: {:.2f}%.'.format(percentage))


# Questão 02

arr = space[:, -2].astype(dtype=np.float64)
avr_cost = arr[arr != 0].mean(axis=0)

print('QUESTÃO 02: A média de gastos em missões com custo maior que 0 é: US$ {:.2f} M.'.format(avr_cost))


# Questão 03

i = 0
for missions in space:
    status = missions[2]

    if(status.find('USA') != -1):
        i = i + 1

print('QUESTÃO 03: Foram lançados em solo americano {} missões.'.format(i))


# Questão 04
arr = space[:, [1, -2, 4]]
arr_values = arr[arr[:, 0] == "SpaceX", 1]
arr_names = arr[arr[:, 0] == "SpaceX", 2]

index = arr_values.astype(dtype=np.float64).argmax(axis=0)

print('QUESTÃO 04: A missão da SpaceX mais cara foi a "{}" custando US$ {}M.'.format(arr_names[index], arr_values[index]))


# Questão 05

unique, counts = np.unique(space[:, 1], return_counts=True)

print('QUESTÃO 05: Empresas e quantidade de missões:')
print("NUM\t| Empresa\t\t\t\t")
for i in range(len(unique)):
    print("{}\t| {}: {}".format(i + 1, unique[i], counts[i]))