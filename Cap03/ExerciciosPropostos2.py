# 1
# Conjuntos

loja1 = {
    'iPhone',
    'Samsung',
    'Xiaomi',
    'Motorola'
}
loja2 = {
    'Nokia',
    'iPhone',
    'Motorola'
}

print(loja1 | loja2) # União

print(loja1 & loja2) # Interseção

# 2
nome = input('Qual o nome do aluno? ')
media = float(input('Qual a media do aluno? '))

aluno = {
    'nome': nome,
    'media': media
}

if aluno['media'] >= 60:
    aluno['situacao'] = 'AP'
else:
    aluno['situacao'] = 'RP'

for k, v in aluno.items():
    print('{}: {}'.format(k, v))
