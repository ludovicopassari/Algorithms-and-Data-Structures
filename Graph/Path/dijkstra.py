"""  
ALGORITMO DI DIJKSTRA
"""

def min_pop(pq):
    """
    Effettua un pop dell'elemento minimo.

    Args: La funzione prende in input una coda di priorità in cui ogni elemeneto è una tupla (w,vertex).

    Return: Ritorna una tupla con l'elemento minimo.

    """
    # considera inizialmente come minimo la prima tupla di valori
    min_w, min_v = pq[0]

    # per ogni tupla nella coda
    for item in pq:
        # spacchetta i valori della tupla
        curr_w, curr_v = item
        # se il valore di peso corrente è minore di quello fin ora trovato
        if curr_w < min_w:
            # aggiorna il valore del peso
            min_w = curr_w
            # aggiorna il nome del vertice corrispondente
            min_v = curr_v
    # rimuove dalla coda la tupla trovata
    pq.remove((min_w, min_v))

    return min_w, min_v


def dijkstra(graph, start):
    """
    Implementazione algoritmo Dijkstra.

    Args: La funzione prende in input un grafo e un vertice di start

    Return: Ritorna un dizionario con tutte le distanze dal nodo di start
    
    """

    # crea un dizionario con le distanze tutte ad infinito
    distances = {vertex: float("inf") for vertex in graph}
    # considera la distanza dal nodo di start al nodo di start 0.
    distances[start] = 0

    # coda di priorità
    pq = [(0, start)]

    while pq:
        # estrae dalla coda di priorità la tupla con il valore minimo di distanza
        curr_w, curr_v = min_pop(pq)
        
        # per ogni vicino e il suo relativo peso
        for neighbor, weight in graph[curr_v].items():
            # fa una stima della distanza tra il nodo di start e uil nodo vicino
            estimated_distance = weight + curr_w
            # se questa stima è minore della distanza finora trovata
            if estimated_distance < distances[neighbor]:
                # aggiorna il valore di distanza minima
                distances[neighbor] = estimated_distance
                pq.append((estimated_distance, neighbor))

    return distances


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

    print("Dijkstra : ", dijkstra(graph, "ME"))
    print()
    print("Graph:", graph)


if __name__ == "__main__":
    main()
