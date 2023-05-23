def dfs(graph, current_vertex, visited=[]):
    """
    Implementazione ricorsiva dell'atteaversamento in profondità di un grafo:

    Args: LA funzione prende in input un grafo, il vertice da cui iniziare l'attraversamento e una list che conterrà tutti i nodi visitati.

    Return: Ritorna la lista dei nodi visitati.

    Description: La funzione considera un nodo di partenza e lo visita poi se il nodo ha dei vicini e questi vicini non sono stati visitati , richiama la funzine dfs() passando ogni volta come paramentro il nodo vicino.
    """
    # se il nodo corrente non è stato visitato
    if current_vertex not in visited:
        # visita il nodo
        visited.append(current_vertex)
        # per ogni vicino del nodo corrente
        for neighbours in graph[current_vertex]:
            # se il vicino non è stato visitato, visitalo
            if neighbours not in visited:
                dfs(graph, neighbours, visited)
    return visited


def dfs_iterative(graph, u):
    """
    La funzione implementa in maniera iterativa l'attraversamento in profondità di un grafo.

    """
    visited = []
    queue = []

    queue.append(u)

    while queue:
        current_vertex = queue.pop()

        if current_vertex not in visited:
            visited.append(current_vertex)
            for neighbours in graph[current_vertex]:
                queue.append(neighbours)

    return visited


def dfs_color(graph, u):
    exploration = {vertex: "white" for vertex in graph}

    for vertex in graph:
        if exploration[vertex] == "white":
            visit_vertex(graph, vertex, exploration)

    print(exploration)


def visit_vertex(graph, vertex, exploration):
    exploration[vertex] = "gray"

    for neighbours in graph[vertex]:
        if exploration[neighbours] == "white":
            visit_vertex(graph, neighbours, exploration)
    exploration[vertex] = "black"


def bfs(graph, start_vertex):
    """
    Questa funzione implementa una visita in ampiezza di un grafo.

    Args: Prende in input un grafo e un vertice da cui iniziare le visite.

    Color code : {'white':not visited} {'gray': visit in process} {'black': visited}
    """
    visit = []
    # crea una mappa delle visite in base ad un codice colore
    exploration_map = {vertex: "white" for vertex in graph}
    exploration_map[start_vertex] = "gray"

    stack = []
    stack.append(start_vertex)

    while stack:
        curr = stack.pop()

        # per ogni vicino del nodo corrente
        for neighbour in graph[curr]:
            # se il vicino è mappato come non visitato
            if exploration_map[neighbour] == "white":
                # mette in stato di visita il vicino
                exploration_map[curr] = "gray"
                stack.append(neighbour)

        # mappa il nodo corrente come visitato
        exploration_map[curr] = "black"

        # da valutare.......
        if curr not in visit:
            visit.append(curr)

    return exploration_map, visit


def main():
    graph = {
        "ME": {"CT": 93.6, "PA": 225.8},
        "PA": {"CT": 209.6, "ME": 225.8, "TP": 108.5},
        "CT": {"ME": 93.6, "PA": 209.6, "SR": 66.2},
        "TP": {"PA": 108.5},
        "SR": {"CT": 66.2, "CL": 159.6},
        "CL": {"SR": 159.6},
    }

    print("DFS:", dfs(graph, "ME"))
    print()
    print("DFS iterative :", dfs_iterative(graph, "ME"))
    print()
    # print(dfs_color(graph, "ME"))
    print("BFS:", bfs(graph, "ME"))
    print()
    print("Graph:", graph)


if __name__ == "__main__":
    main()
