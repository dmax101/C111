# Nome: Danilo Vidal Ribeiro
# Matricula: 1411

# a. Mostre apenas o nome das cores que são primárias;
# b. Mostre apenas os códigos hexadecimais das cores que possuem tom de azul máximo (255);
# c. A partir da coleção colors, extraia seus valores para criar um NumPy Array 1-D formado apenas pelo nome e código hexadecimal de cada cor;
# Ex: “black”, ”#000”, “green”, “#0F0”...
# d. Transforme o Array 1-D em um Array 2-D no seguinte padrão:
# ...
# green #0F0
# yellow #FF0
# ...
# e. Troque o nome de cada cor no Array 2-D para seu respectivo nome em Português;


colors = [
    {"color": "black", "type": "primary", "code": {"rgba": [255,255,255,1],"hex": "#000"}},
    {"color": "green", "type": "secondary", "code": {"rgba": [0,255,0,0.1],"hex": "#0F0"}},
    {"color": "yellow", "type": "primary","code": {"rgba": [255,255,0,0.7],"hex": "#FF0"}},
    {"color": "blue", "type": "primary","code": {"rgba": [0,0,255,1],"hex": "#00F"}}
    ]

# a)
print('Questão 3. a) -------------')
for color in colors:
    if(color.get('type') == 'primary'):
        print(color.get('color'))

# b)
print('Questão 3. b) -------------')
for color in colors:
    if(color['code']['rgba'][2] == 255):
        print(color['code'].get('hex'))

# c)
print('Questão 3. c) -------------')
import numpy as np

arr = np.array([])
for color in colors:
    arr_nome = color.get('color')
    arr_hex = color['code'].get('hex')
    arr_composta = np.array([arr_nome, arr_hex])
    arr = np.concatenate((arr, arr_composta))
print(arr)

# d)
print('Questão 3. d) -------------')
arr_col = arr.reshape(4,2)
print(arr_col)

# e)
print('Questão 3. e) -------------')
arr_col = np.where(arr_col=='black', 'preto', arr_col)
arr_col = np.where(arr_col=='green', 'verde', arr_col)
arr_col = np.where(arr_col=='yellow', 'amarelo', arr_col)
arr_col = np.where(arr_col=='blue', 'azul', arr_col)

print(arr_col)