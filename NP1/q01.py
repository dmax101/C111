# Nome: Danilo Vidal Ribeiro
# Matricula: 1411

# Questão 01

# input: nome e ano de várias músicas
# storage: musica -> dicionário -> lista
# output:
# a) quantas músicas
# b) informações das músicas do mais antigo

lista = []

def inserir():
    nome = input('Insira o nome da música: ')
    ano = int(input('Insira o ano da música: '))

    return {"nome": nome, "ano": ano}

def get_ano(lista):
    return lista.get('ano')

def mostrar_ordenado_antigo(l: list):
    print('Lista de músicas cadastradas')

    l.sort(key=get_ano)
    print(l, end='\n\n')

flag = True

while flag:
    info = inserir()
    lista.append(info)

    op = input('Deseja continuar? (s/n) ')
    if(op != 's'):
        flag = False

print("a) ", "foram cadastradas {} músicas".format(len(lista)))

print("b) ")
mostrar_ordenado_antigo(lista)