def busca_binaria(lista, alvo):
    l, h = 0, len(lista) - 1

    for iteracao in range(len(lista)):
        m = (l + h) // 2
        print(f"Iteração {iteracao} | l:{l} | h:{h} | m:{m}")

        if lista[m] == alvo:
            return m + 1
        elif lista[m] < alvo:
            l = m + 1
        else:
            h = m - 1
    return -1

lista_teste = [11, 17, 18, 45, 50, 71, 95]
alvo = 11

print(busca_binaria(lista_teste, alvo))