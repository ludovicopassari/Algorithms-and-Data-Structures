"""  
ATTRAVERSAMENTI DI UN GRAFO

"""
def dfs(graph, vertex, visited=[]):
    """
    La funzione implementa un attraversamento in profondita di un grafo ricorsivamente.

    Args: La funzione prende in input un grafo, un vertice da cui partire, e una lista che tiene traccia dei nodi visitati.

    Return: Ritorna la lista dei nodi visitai

    """
    # se il nodo non è stato visitato
    if vertex not in visited:
        # visita il nodo corrente
        visited.append(vertex)
        # per ogni vicino del vertice
        for neighbours in graph[vertex]:
            # se il vicino non è stato visitato
            if neighbours not in visited:
                # richiama la funzione ricorsivamente con il vicino passaro come argomento
                dfs(graph, neighbours, visited)

    return visited


def dfs_iterative(graph, start_vertex):
    """
    Implementazione iterativa di un attraversamento in profindità di un grafo .

    Args: La funzione prende in input un grafo e un vertice da cui iniziare ad attaraversare.

    Return: Ritorna la lista dei nodi visitati

    """
    visited = []
    queue = [start_vertex]

    while queue:
        curr = queue.pop()

        # se il nodo corrente non è stato visitato
        if curr not in visited:
            # visita il nodo corrente
            visited.append(curr)
            # per ogni vicino
            for neighbour in graph[curr]:
                # se il vicino non è stato visitato
                if neighbour not in visited:
                    # mettilo in attesa per essere visitato
                    queue.append(neighbour)
    return visited


def bfs(graph, start_vertex):
    # explortion_map ={vertex:'white' for vertex in graph}
    exploration_map = {vertex: "white" for vertex in graph}

    queue = [start_vertex]
    exploration_map[start_vertex] = "gray"

    while queue:
        curr = queue.pop()

        for neighbour in graph[curr]:
            if exploration_map[neighbour] == "white":
                exploration_map[neighbour] = "gray"
                queue.append(neighbour)

        exploration_map[curr] = "black"
    return exploration_map


def dfs_color(graph, start_vertex):
    """
    Implmentazione di un attraversamento utilizzando un codice colori per identificare lo stato di visita di un vertice.

    'white' -> not visited
    'gray' -> in visit
    'black' -> visited

    Args: La funzione prende in input un grafo, e un vertice da cui inziare ad attraversare il grafo.

    Return: Ritorna il dizionario con lo stato delle visite.

    """
    exploration_map = {vertex: "white" for vertex in graph}

    for vertex in graph:
        # se il vertice non è ancora stato visitato
        if exploration_map[vertex] == "white":
            visit_vertex(graph, exploration_map, vertex)
    return exploration_map


def visit_vertex(graph, exploration_map, vertex):
    """
    Funzione di appoggio per la visita in profondità che visita in profondità un vertice e tutti i suoi vicini.

    Args: La funzione prende in input un grafo, un dizionario che contiele lo stato di esplorazione del grafo,e un vertice da visitare.

    Return: None
    """
    # mette in stato di visita il vertice
    exploration_map[vertex] = "gray"
    # per ogni vicino del vertice
    for neighbour in graph[vertex]:
        # se il vertice non è stato visitato
        if exploration_map[neighbour] == "white":
            # visita in profondità il vertice
            visit_vertex(graph, exploration_map, neighbour)

    exploration_map[vertex] = "black"


def main():
    # grafo non orientato, pesato
    graph = {
        "ME": {"CT": 93.6, "PA": 225.8},
        "PA": {"CT": 209.6, "ME": 225.8, "TP": 108.5},
        "CT": {"ME": 93.6, "PA": 209.6, "SR": 66.2},
        "TP": {"PA": 108.5},
        "SR": {"CT": 66.2, "CL": 159.6},
        "CL": {"SR": 159.6},
    }

    print("DFS visit:", dfs(graph, "ME"))
    print("DFS iterative visit:", dfs_iterative(graph, "ME"))
    print("DFS COLOR visit:", dfs_color(graph, "ME"))
    print("BFS visit :", bfs(graph, "ME"))

    print("Graph:", graph)


if __name__ == "__main__":
    main()
