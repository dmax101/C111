# Tuplas
# Organiza seus elementos dentro de ()
# Não permite alteração ou adção de novos elementos


names = ('Goku', 'Vegeta', 'Trunks', 'Gohan')

print(names[1:3])
print(names[2:])
print(names[-1])
print(len(names))


# Varredura de uma Tupla

# For Each
for name in names:
    print(name)

# For com Índice
for i in range(0, len(names)):
    print(i, names[i])

print(sorted(names))