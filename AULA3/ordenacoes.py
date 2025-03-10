#Ex. 1
lista = [5,2,9,1,5,6]
lista.sort()
print(lista)

###############################################################

# Ex. 2
lista.sort(reverse = True)
print(lista)

###############################################################

# Ex. 3
lista = [5,2,9,1,5,6]
lista_ordenada = sorted(lista)
print(lista_ordenada)

###############################################################

# Ex. 4
lista = [5,2,9,1,5,6]
lista_ordenada1 = sorted(lista, reverse=True)
print(lista_ordenada1)

###############################################################

# Ex. 5
lista = [('maça', 3), ('banana', 1), ('laranja', 2), ('uva', 1)]
lista_ordenada = sorted(lista, key=lambda x: x[1])
print(lista_ordenada)

###############################################################

# Ex. 6
lista = [('maça', 3, 100), ('banana', 1, 152), ('laranja', 2, 234), ('uva', 1, 135)]
lista_ordenada = sorted(lista, key=lambda z:(z[1], z[0]))
print(lista_ordenada)