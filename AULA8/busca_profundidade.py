grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def busca_profundidade(grafo, inicio, visitados = None):
    if visitados is None:
        visitados = set()

    visitados.add(inicio)
    print(inicio, end = ' ')

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            busca_profundidade(grafo, vizinho, visitados)

print('DFS a partir do nó A:')
busca_profundidade(grafo, 'B')
