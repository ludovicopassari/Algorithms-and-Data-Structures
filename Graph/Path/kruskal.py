""" 
 
ALGORITMO DI KRUSKAL


L'algoritmo Kruskal mantiene un insieme di cluster di veritici fondendo ripetutamente coppie di cluster fino a quando un singolo cluster si estende sul grafo.

1) Inizialmente ogni vertice è  di per se un singolo cluster

2) viene creata una lista con tutti gli archi

3)Successivamente per ogni arco nella lista di archi ordinata per pesi crescente viene estratto il clustr di appartenenza dei due nodi che formano l'arco e se i cluster di appartenenza sono diversi, viene aggiunto al minimum spanning tree il nodo e viene fatto il merge del cluster.

"""


def find_cluster(clusters, target_vertex):
    """
    Ricerca un vertice all'interno dei cluster.

    Args: La funzione prende in input una nuvola di cluster e un vertice da cercare.

    Return : Ritorna il numero del cluster a cui appartiene il vertice di target.

    """
    # per ogni cluster
    for cluster in clusters:
        # se il vertice target è allinterno del cluster corrente
        if target_vertex in clusters[cluster]:
            # ritornano
            return cluster


def merge_cluster(clusters, ku, kv):
    """
    Unisce due cluster

    Args: La funzione prende in input una nuvola di cluster, e i due cluster di cui bisogna fare il merge

    Return: Ritorna il cluster modificato

    """
    # ATTENZIONE la funzione fa il merge nel cluster che si trova più a sinistra
    if ku < kv:
        for vertex in clusters[kv]:
            clusters[ku].append(vertex)
        # svuota il cluster più a destra
        clusters[kv] = []
    else:
        for vertex in clusters[ku]:
            clusters[kv].append(vertex)
        # svuota il cluster piu a destra
        clusters[ku] = []

    # ritorna il cluster modificato
    return clusters


def kruskal(graph):
    """
    Implementazione algoritmo di Kruskal

    Args: La funzione prende in input un grafo

    Retun: Ritorna un albero minimo di copertura

    """
    # crea l'albero di copertura minima vuoto
    mst = {}
    # crea la struttura che ospita i cluster
    cluster = {}
    # lista degli archi presenti nel grafo
    edges = []

    # numero progressivo che identifica ogni singolo cluster
    nk = 0

    # riempie la struttura dei cluster
    for vertex in graph:
        cluster[nk] = [vertex]
        nk += 1

    # riempie la lista degli archi
    for u in graph:
        for v in graph[u]:
            w = graph[u][v]

            if (w, u, v) not in edges and (w, v, u) not in edges:
                edges.append((w, u, v))

    # numero progressivo che identifica ogni singolo nodo dell'albero che creiamo
    nc = 0
    for edge in sorted(edges):
        w, u, v = edge

        # trova il cluster a cui appartengono i vertici
        ku = find_cluster(cluster, u)
        kv = find_cluster(cluster, v)

        # se i nodi appartengono a cluster diversi
        if ku != kv:
            merge_cluster(cluster, ku, kv)
            # aggiunge il nodo all'albero
            mst[nc] = (w, u, v)
            nc += 1

    print(mst)


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

    print("Prim-Jarnik : ", kruskal(graph))
    print()
    print("Graph:", graph)


if __name__ == "__main__":
    main()
