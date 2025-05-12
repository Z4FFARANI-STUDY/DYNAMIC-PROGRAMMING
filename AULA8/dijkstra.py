import networkx as nx

G1 = nx.Graph()
arestas1 = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2),
    ('D', 'F', 6),
    ('E', 'F', 2),
]

G1.add_weighted_edges_from(arestas1)

# Aplicando o algoritmo de Dijkstra de A até F
caminho1 = nx.dijkstra_path(G1, source='A', target='F')
distancia1 = nx.dijkstra_path_length(G1, source='A', target='F')

print("Caminho mais curto de A até F:" " → ".join(caminho1))
print('Distância total:', distancia1, 'km')
