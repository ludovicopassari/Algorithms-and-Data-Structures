"""  
ALGORITMO DI PRIM-JARNIK

"""

def min_pop_edge(crossing):
    """
    Effettua un pop su una lista di tuple così formate (w,u,v)

    Args: La funzione prende in input una lista di tuple (w,u,v)

    Return: Ritorna una tupla (w,u,v) con il peso minimo

    """
    # considera inizialmente come minimo la prima tupla di valori
    w_min, u_min, v_min = crossing[0]

    # per ogni tupla nella lista
    for item in crossing:
        # spacchetta la tupla
        w_curr, u_curr, v_curr = item

        # se il peso corrente è minode del peso fin ora trovato
        if w_curr < w_min:
            # aggiorna il valore globale  del peso minimi
            w_min = w_curr
            # e aggiorna i nodi dell'arco corrispondenti
            u_min = u_curr
            v_min = v_curr

    # rimuove dalla lista la tupla
    crossing.remove((w_min, u_min, v_min))

    return w_min, u_min, v_min


def prim_jarnik(graph, start):
    """
    Implementazione algoritmo Dijkstra

    Args: La funzione prende in input un grafo e un nodo da cui partire a considrare il MST.

    Return: Ritona l'albero di copertura minima.

    """
    # crea un albero di copertura minima vuoto
    minimum_spanning_tree = {}

    vertex_cloud = set()
    vertex_cloud.add(start)
    # numero progressivo che indica il nodo dell'albero
    n_node = 0

    while len(vertex_cloud) != len(graph):
        crossing = []

        for vertex in vertex_cloud:
            for k in graph[vertex]:
                if k not in vertex_cloud and k in graph[vertex]:
                    crossing.append((graph[vertex][k], vertex, k))

        # triade peso, u ,v
        w, u, v = min_pop_edge(crossing)

        vertex_cloud.add(v)
        # aggiungi un il nodo all'albero binario
        minimum_spanning_tree[n_node] = (w, u, v)
        # incrementa il conteggio del nodo del mst
        n_node += 1

    return minimum_spanning_tree


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

    print("Prim-Jarnik : ", prim_jarnik(graph, "ME"))
    print()
    print("Graph:", graph)


if __name__ == "__main__":
    main()
