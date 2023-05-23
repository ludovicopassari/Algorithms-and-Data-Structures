"""  
L'algoritmo Kruskal mantiene un insieme di cluster di veritici fondendo ripetutamente coppie di cluster fino a quando un singolo cluster si estende sul grafo.

1) Inizialmente ogni vertice è  di per se un singolo cluster

2) viene creata una lista con tutti gli archi

3)Successivamente per ogni arco nella lista di archi ordinata per pesi crescente viene estratto il clustr di appartenenza dei due nodi che formano l'arco e se i cluster di appartenenza sono diversi, viene aggiunto al minimum spanning tree il nodo e viene fatto il merge del cluster.

"""


def get_cluster_id(clusters, x):
    """
    La funzione serve per capire a quale cluster appartiene un certo vertice x.

    Args: La funzione prene in input un insieme di cluster e il nome di un vertice

    Retrun: Ritorna l'identificativo del cluster che contiene x
    """
    for cluster_id, cluster_list in clusters.items():
        # se x è nel cluster
        if x in cluster_list:
            # restituisci l'id
            return cluster_id


def merge_cluster(cluster, ku, kv):
    """
    La funzione serve a fare il merge di due cluster

    Args: La funzione prende in input un insieme di cluster e l'identificativo di due cluster diversi

    Return: La funzione ritorna l'insieme dei cluster con il merge effettuato

    Description : Il merge va effettuato spingendo sempre a sinistra i cluster

    """
    # fa il merge nel cluster più a sinistra
    if ku < kv:
        for vertex in cluster[kv]:
            cluster[ku].append(vertex)
        # svuota il cluster di provenienza
        cluster[kv] = []
    else:
        for vertex in cluster[ku]:
            cluster[kv].append(vertex)

        cluster[ku] = []
    return cluster


def kruskal(graph):
    # creo il mst
    mst = {}
    # dizionario con dentro i cluster
    cluster = {}
    # numero progressivo che identifica ogni cluster
    cluster_id = 0
    # strutturo i cluster
    for vertex in graph:
        cluster[cluster_id] = [vertex]
        cluster_id += 1

    # creo la lista degli archi
    edges = set()
    for u in graph:
        for v in graph[u]:
            w = graph[u][v]
            # si assicura che un arco la sua permutazione dei nodi non sia stata già inserita
            if (w, u, v) not in edges and (w, v, u) not in edges:
                edges.add((w, u, v))

    # numero progressivo che identifica un nodo
    mst_id_node = 0

    for edge in sorted(edges):
        w, u, v = edge

        ku = get_cluster_id(cluster, u)
        kv = get_cluster_id(cluster, v)

        if ku != kv:
            cluster = merge_cluster(cluster, ku, kv)
            mst[mst_id_node] = (w, u, v)
            mst_id_node += 1

    return mst


# {0: (66.2, 'CT', 'SR'), 1: (93.6, 'ME', 'CT'), 2: (108.5, 'PA', 'TP'), 3: (159.6, 'SR', 'CL'), 4: (209.6, 'PA', 'CT')}


def main():
    # grafo pesato non orientato
    graph = {
        "ME": {"CT": 93.6, "PA": 225.8},
        "PA": {"CT": 209.6, "ME": 225.8, "TP": 108.5},
        "CT": {"ME": 93.6, "PA": 209.6, "SR": 66.2},
        "TP": {"PA": 108.5},
        "SR": {"CT": 66.2, "CL": 159.6},
        "CL": {"SR": 159.6},
    }

    print("Kruskal resul:", kruskal(graph))
    # print(graph)


if __name__ == "__main__":
    main()
