# Listas
# Orgarniza elementos entre []
# Muito parecido com as tuplas, mas...
# com as listas é possível modificar e adicionar novos dados

names = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

print(names[1:3])
print(names[2:])
print(names[-1])
print(len(names))

# Alterando uma lista
names[3] = 'Goten'

names.append('Jiren')
names.append('Jiren')

if 'Vegeta' in names:
    names.remove('Vegeta')
    print(names)