import matplotlib.pyplot as plt
import networkx as nx

# Función para agregar nodos al gráfico de un árbol
def add_edges(tree, graph, pos=None, x=0, y=0, layer=1, spread=1):
    if tree is None:
        return

    graph.add_node(tree['value'], pos=(x, y))

    if pos is None:
        pos = {}
    pos[tree['value']] = (x, y)

    if 'left' in tree and tree['left']:
        graph.add_edge(tree['value'], tree['left']['value'])
        add_edges(tree['left'], graph, pos, x - spread / layer, y - 1, layer + 1, spread)

    if 'right' in tree and tree['right']:
        graph.add_edge(tree['value'], tree['right']['value'])
        add_edges(tree['right'], graph, pos, x + spread / layer, y - 1, layer + 1, spread)

    return pos

def grafico_arbol_binario(dict_binary_tree):
    G = nx.Graph() # Crear un grafo
    pos = add_edges(dict_binary_tree, G) # Añadir los nodos y las conexiones
    # Dibujar el árbol
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")
    plt.show()
    
def grafico_grafo(matriz_adyacencia: list[list[int]], nodos: list) -> None:
    G = nx.Graph()  # Crear un grafo

    # Agregar nodos
    for nodo in nodos:
        G.add_node(nodo)

    # Agregar aristas basadas en la matriz de adyacencia
    for i in range(len(nodos)):
        for j in range(len(nodos)):
            if matriz_adyacencia[i][j] == 1:
                G.add_edge(nodos[i], nodos[j])

    # Dibujar el grafo
    pos = nx.spring_layout(G)  # Posicionar nodos de manera atractiva
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")
    plt.show()
    
def grafico_grafo_simple(nodos, aristas) -> None:
    G = nx.Graph()  # Crear un grafo

    # Agregar nodos
    for nodo in nodos:
        G.add_node(nodo.dato)

    # Agregar aristas
    for origen, destino in aristas:
        G.add_edge(origen.dato, destino.dato)

    # Dibujar el grafo
    pos = nx.spring_layout(G)  # Posicionar nodos de manera atractiva
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")
    plt.show()