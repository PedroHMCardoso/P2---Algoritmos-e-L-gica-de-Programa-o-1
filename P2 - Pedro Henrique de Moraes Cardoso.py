# # 1 – Crie um programa que contenha uma lista inicializada com 8 valores.
# # Os valores devem estar em ordem aleatória, ou seja, não podem estar ordenados.

# # O programa deve ordenar os valores (Ver itens abaixo) e apresentá-los em:

# # •    Ordem crescente, sem utilizar qualquer função do Python, apenas laços de repetição;
# # •    Ordem decrescente, sem utilizar qualquer função do Python, apenas laços de repetição;
# # •    Ordem crescente, utilizando as funções do Python;
# # •    Ordem decrescente, utilizando as funções do Python.

# lista_A = [3, 6, 8, 2, 4, 9, 10, -1]
# n = len(lista_A)
# aux = 0


# for i in range(n): #crescente
#     for j in range(n - i - 1):
#         if lista_A[j] > lista_A[j + 1]:
#             aux = lista_A[j + 1]
#             lista_A[j + 1] = lista_A[j]
#             lista_A[j] = aux
# print(lista_A)



# for i in range(n): #decrescente
#     for j in range(n - i - 1):
#         if lista_A[j] < lista_A[j + 1]:
#             aux = lista_A[j + 1]
#             lista_A[j + 1] = lista_A[j]
#             lista_A[j] = aux

# print(lista_A)

# lista_A.sort(key=int) #crescente com função python
# print(lista_A)


# lista_A.sort(reverse=bool) #decrescente com função python
# print(lista_A)


# 2 – Crie uma lista vazia (não deve ser inicializada com nenhum valor ao ser criada).
# O programa deve receber valores informados pelo usuário até que ele digite "sair". Nesse momento, o programa deve ser encerrado.

# Em seguida, apresente:

# •    O maior valor, sem utilizar funções do Python;
# •    O menor valor, sem utilizar funções do Python;
# •    A soma de todos os valores, sem utilizar funções do Python;
# •    O tamanho da lista, sem utilizar funções do Python;
# •    O maior valor, utilizando funções do Python;
# •    O menor valor, utilizando funções do Python;
# •    A soma de todos os valores, utilizando funções do Python;
# •    O tamanho da lista, utilizando funções do Python.

# lista_B = []
# vmax = None
# vmin = None
# tamanho = 0
# soma = 0

# #Sem função do Python

# while True:
#     op = input("Digite 1 para inserir valores na lista e 'sair' para parar: ").lower()
#     if op == "sair":
#         break
#     else:
#         valor = float(input("Digite o valor a ser colocado na lista: "))
#         lista_B.append(valor)

# for valor in lista_B:
#     tamanho = tamanho + 1
#     soma = valor + soma

#     if vmax == None and vmin == None:
#         vmax = valor
#         vmin = valor

#     elif vmax < valor:
#         vmax = valor

#     elif vmin > valor:
#         vmin = valor


# print(vmax)
# print(vmin)
# print(tamanho)
# print(soma)

# print(max(lista_B))
# print(min(lista_B))
# print(sum(lista_B))
# print(len(lista_B))


# 3 – Crie um programa que inicialize uma lista com 3 nomes.

# Em seguida, crie uma função que receba dois parâmetros: a lista e um nome a ser removido.
# A função deve remover o nome informado da lista e exibir os itens restantes.

nomes = ["pedro", "ferraz", "felipe"] 


def remover(nm):
    nomes.remove(nm)
    print(nomes)

n = str(input("Digite o nome que você quer apagar da lista entre: Pedro, Ferraz e Felipe: ")).lower()
print(n)
remover(n)