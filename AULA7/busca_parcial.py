import heapq

lista = [8, 3, 5, 7, 9, 4, 10]

n = 3
m = 8

menores = heapq.nsmallest(n, lista)
maiores = heapq.nlargest(n, lista)

print(menores)
print(maiores)


#########################################

# grafo em uma estrutura com dicionario
dicionario = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

##########################################

grafo_amizades = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Diana'],
    'Charlie': ['Alice', 'Diana'],
    'Diana': ['Bob', 'Charlie', 'Eve'],
    'Eve': ['Diana'],
}

# 1. Quais os amigos em comum entre o bob e Charlie?
amigos_bob = set(grafo_amizades['Bob'])
amigos_charlie = set(grafo_amizades['Charlie'])

# Interseção
amigos_em_comum = amigos_bob & amigos_charlie
print(amigos_em_comum)



# 2. Quais os amigos diferentes entre Alice e Diana?
amigos_diana = set(grafo_amizades['Diana'])
amigos_alice = set(grafo_amizades['Alice'])

# Diferença (do maior para o menor)
amigos_diferentes = amigos_diana - amigos_alice
print(amigos_diferentes)



# 3. Quais os amigos de Charlie e Diana?
amigos_charlie = set(grafo_amizades['Charlie'])
amigos_diana = set(grafo_amizades['Diana'])

# União
amigos = amigos_charlie | amigos_diana
print(amigos)
