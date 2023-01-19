import networkx as nx
import itertools

def main():
    # Crear el grafo
    G = nx.Graph()

    # Agregar los planetas como nodos
    planets = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine', 'Kamino', 'Naboo', 'Mustafar', 'Scarif', 'Bespin', 'planeta1', 'planeta2', 'planeta3', 'planeta4', 'planeta5', 'planeta6', 'planeta7']
    G.add_nodes_from(planets)

    # Crear una lista de tuplas con las relaciones entre los planetas y con un peso asociado
    planet_pairs = list(itertools.combinations(planets, 2))
    for i, pair in enumerate(planet_pairs):
        G.add_edge(pair[0], pair[1], weight=i)


    # Encontrar el árbol de expansión mínima utilizando el algoritmo de Prim
    T = nx.minimum_spanning_tree(G, algorithm='prim', weight='weight')
    print(T.edges())
