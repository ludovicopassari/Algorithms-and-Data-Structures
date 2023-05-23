"""  
Implementazione dell'algoritmo di Dijkstra per trovare il cammino minimo da un nodo A verso tutti gli atri nodi
"""


def dijkstra(graph, start):
    """
    Algoritmo che trova i cammini minimi da un vertice sorgente a tutti gli altri

    Args: La funzione prende in input un grafo pesato e il nome di un vertice da cui partire

    Return : Ritorna un dizionario con tutte le distanze dal nodo di start a tutti i inodi


    1) Viene creato un dizioanrio con tutte le distanze dal vertice di start verso tutti gli altri vertici(inizialmente tutte le distanze sono settate ad 'inf' tranne quella del nodo di start)

    2) Viene creata una coda in cui inizialmente viene incodato il primo vertice e la distanza 0

    3)viene utilizzata una funzione di supporto che fa un pop dell'elemento con la distanza minima

    4) Per ogni vicino del nodo corrente viene calcolata la distanza tra il nodo di partenza e quel nodo vicino e se è minore del valore memorizzato nel dizionario delle distanze, quel valore nel dizionario viene aggiornato e vien e viene incodata la tupla (w_calcolata,vertex)

    """
    # crea una mappa delle distanze, considerando inzialmente tutte le distanze a infinito
    distances_map = {vertex: float("inf") for vertex in graph}
    # imposta la distanza del vertice di start a 0
    distances_map[start] = 0
    # mette in coda il primo elemento
    queue = [(start, 0)]

    while queue:
        current_node, current_weight = min_pop(queue)
        # per ogni vicino del nodo corrente
        for neighbour in graph[current_node]:
            # fa un calcolo della distanza dal nodo di start al nodo vicino
            estimated_distance = current_weight + graph[neighbour][current_node]
            # se la distanza stimata è minore della distanza nella distances map
            if estimated_distance < distances_map[neighbour]:
                # ha trovato una distanza minore, allora aggiorna il valore nella mappa delle distanze
                distances_map[neighbour] = estimated_distance
                queue.append((neighbour, estimated_distance))
        # break

    return distances_map


def min_pop(queue):
    """
    Effettua un pop della tupla con il valore del peso minore

    Args: La funzione prende in input una coda

    Returns: Ritorna il nome e il peso minimo in coda

    """
    min_vertex, min_weight = queue[0]

    for edge in queue:
        curr_vertex, curr_w = edge
        if curr_w < min_weight:
            min_weight = curr_w
            min_vertex = curr_vertex

    queue.remove((min_vertex, min_weight))
    return min_vertex, min_weight


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

    print("Dijkstra result -->", dijkstra(graph, "ME"))
    print()
    print("Graph -->", graph)


if __name__ == "__main__":
    main()
