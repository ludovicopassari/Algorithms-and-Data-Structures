def get_right_child(index):
    """
    Restituisce l'indice del figlio destro
    """
    return (index * 2) + 2


def get_left_child(index):
    """
    Restituisce l'indice del figlio sinitro
    """
    return (index * 2) + 1


def max_heapify(array: list[int], heapsize: int, i: int):
    """
    Fa scendere il valore di array[i] nel max_heap in modo che il sottoalbero con radice in i diventi un heap

    Args: La funzione prende in input un array qualunque, la dimensione(necessaria successivamente per l'heapsort), e l'indice di un elemento
    """
    # indice dell'elemento più grande tra radice-figlio sinistro- figlio destro
    largest = i

    # indice del figlio sinistro
    left = get_left_child(i)
    # indice del figlio destro
    right = get_right_child(i)

    # se il figlio sinistro esiste all'interno dello heap e se il figlio sinistro è più grande della radice
    if left < heapsize and array[left] > array[i]:
        # aggiorna il valore con l'elemento più grande
        largest = left
    # se il figlio destro esiste all'interno dello heap e se il figlio destro è pù grande dell'elemento più grande
    if right < heapsize and array[right] > array[largest]:
        # aggiorna il valore dell'elemento piu grande
        largest = right

    # se è stato aggiornato il valore di largest
    if i != largest:
        # scambia la radice che sta in indice i con l'elemento più grande
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, heapsize, largest)


def build_max_heap(data, heapsize):
    """
    Crea un max-heap a partire da un array qualunque.

    Args: La funzione prende in input una array e la sua dimensione

    Return: None. La modifica viene fatta sui dati di partenza

    """
    # per ogni elemento a partire dalla fine fino alla metà
    for i in range(heapsize // 2, -1, -1):
        max_heapify(data, heapsize, i)


def heapsort(data):
    """
    Ordina un array sfruttando l'algoritmo Heap-Sort

    Args: La funzione prende in input un array qualunque e la sua dimensione

    Return: None. La modifica viene effeettuata sui dati di partenza
    """
    heapsize = len(data)
    # crea un max heap
    build_max_heap(data, heapsize)

    for i in range(heapsize - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        # passa ogni volta la dimensione dell'array decrementata di 1.
        max_heapify(data, i, 0)


def main():
    # array disordinato
    unsorted_data = [2, 8, 5, 3, 9, 1]
    print("Unsorted Data --> ", unsorted_data)
    # lancia l'algoritmo di heap-sort
    heapsort(unsorted_data)
    print("Sortde Data --> ", unsorted_data)


if __name__ == "__main__":
    main()
