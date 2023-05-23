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
    
    #finchè non termina uno dei due sotto-array
    while i < left_array_size and j < right_array_size:
        #se l'elemento del sottoarray di sinistra è più grande di quello del sottoarray di destra.
        if l_array[i] > r_array[j]:
            #aggiungi all'interno dell'array di output l'elemnto j-esimo del sotto-array di destra.
            data[k] = r_array[j]
            j += 1

        else:
            data[k] = l_array[i]
            i += 1
        #incremente l'indice dell'array di output
        k += 1

    # se l'indice 'i' non ha ancora spazzolato tutto il sotto-array di sinstra 
    if i < left_array_size:
        #completa l'inserimento degli elementi nell'array di output
        while i < left_array_size:
            data[k] = l_array[i]
            i += 1
            k += 1
    # se l'indice 'j' non ha ancora spazzolato tutto il sotto-array di destra 
    if j < right_array_size:
        #completa l'inserimento degli elementi nell'array di output
        while j < right_array_size:
            data[k] = r_array[j]
            j += 1
            k += 1

def merge_sort(data):
    """
    Implementazione dell'algoritmo Merge-Sort.
    
    Args: La funzione prende in input un array disordinato.
    
    Rerurn: Ritorna un array ordinato.
    
    """
    n = len(data)
    #se l'array passato è composto almeno da due elementi
    if n > 1:
        
        #calcola il punto mediano dell'array
        mid = n // 2
        # effettua uno slice dall'indice 0 fino alla metà
        left_array = data[:mid]
        # effettua uno slice dall'indice mediano fino alla fine
        right_array = data[mid:]
        
        #richiama ricorsivamente la funzione
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
