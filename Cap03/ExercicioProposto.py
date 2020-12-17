top5 = ('Real Madrid','Milan','Barcelona','Bayern','Liverpool')

print(top5[:3])
print(top5[3:])
print(sorted(top5))

for i in range(0, len(top5)):
    if top5[i] == 'Barcelona':
        print(i + 1)

print(top5.index('Barcelona') + 1)


valores = int(input('Digite quantos números você quer cadastrar: '))

lista = []

for i in range(valores):
    pos = i + 1
    v = int(input('Digite o {}º valor: '.format(pos)))
    if not v in lista:
        lista.append(v)

print(sorted(lista))
print(max(lista))
print(min(lista.sort()))
