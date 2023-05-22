def merge(l_array, r_array, data):
    """
    Fa il merge di due array già ordinati in un nuovo array

    Args: La funzione prende in input due array ordinati e l'array in cui deve essere fatto il merge

    Ritorna: None. Modifica l'array passato nel campo data

    Complessità : 0(nlgn)

    Descrizione: La funzione utilizza tre indici i,j,k che scorrono ognuno uno dei tre array. Ad ogni iterazione viene controllato chi è l'elemento più piccolo tra l'i-esimo e il j-esimo ed inserisce il piuù piccolo tra i due nella posizione k di data.

    """
    # indici di scorrimento
    i, j, k = 0, 0, 0
    # dimensione dell' sottoarray di sinstra
    left_array_size = len(l_array)
    # dimensione del sottoarray di destra
    right_array_size = len(r_array)

    while i < left_array_size and j < right_array_size:
        if l_array[i] > r_array[j]:
            data[k] = r_array[j]
            j += 1

        else:
            data[k] = l_array[i]
            i += 1
        k += 1

    # sposta gli ultimi elementi dall'array di sinistra o da quello di destra
    if i < left_array_size:
        while i < left_array_size:
            data[k] = l_array[i]
            i += 1
            k += 1

    if j < right_array_size:
        while j < right_array_size:
            data[k] = r_array[j]
            j += 1
            k += 1


def merge_sort(data):
    n = len(data)

    if n > 1:
        mid = n // 2
        # effettua uno slice dall'indice 0 fino alla metà
        left_array = data[:mid]
        # effettua uno slice dall'indice mediano fino alla fine
        right_array = data[mid:]

        merge_sort(left_array)
        merge_sort(right_array)
        # fa un merge dei due array già ordinati
        merge(left_array, right_array, data)
        return data


def main():
    u_data = [6, 5, 10, 2, 7, 1, 8, 4]
    print("Unsorted Data --> ", u_data)
    print("Sorted Data -->", merge_sort(u_data))


if __name__ == "__main__":
    main()
