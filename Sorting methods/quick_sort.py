def partition(data, p, r):
    """
    Questa funzione riordina l'array in modo tale che tutti gli elementi minori del pivot stiano a sinistra e tutti quelli maggiori a destra.

    Args: La funzione prende in input un array e due indici che segnano l'inizio e la fine della partzione

    Return: Rintorna l'indice esatto in cui si trova il pivot
    """
    # prende l'ultimo elemento come pivot
    pivot = data[r]
    i = p - 1

    # attenzione si ferma a r-1 e quindi non fa l'ultimo swap quando viene controllato il pivot con se stesso
    for j in range(p, r):
        if data[j] <= pivot:
            i += 1

            swap(data, i, j)

    swap(data, i + 1, r)

    return i + 1


def swap(data, a, b):
    """
    Questa funzione fa lo swap di due elementi di un arrai che si trovano a indice a e b.

    Args: La funzione prende in input l'array e i due indici degli elementi da invertire

    """
    data[a], data[b] = data[b], data[a]


def quick_sort(data, left_mark, right_mark):
    """
    Args, La funzione prende in input un array e gli indici che puntano agli estremi dell'array

    Return: Ritorna l'array ordinato

    Costo computazionale: Nel caso migliore viene eseguito con la stessa velocità asintotica del merge soret ovvero 0(nlgn), nel caso peggiore è lento come l'insertion sort.
    """
    if left_mark < right_mark:
        pivot = partition(data, left_mark, right_mark)
        quick_sort(data, left_mark, pivot - 1)
        quick_sort(data, pivot + 1, right_mark)
    return data


def main():
    unsorted_numbers = [2, 10, 11, 8, 6]
    # inizializza due indici , uno all'inizio dell'array e uno alla fine
    leftmark, rightmark = 0, len(unsorted_numbers) - 1
    print("Unsorted data --> ", unsorted_numbers)
    print("Sorted data --> ", quick_sort(unsorted_numbers, leftmark, rightmark))


if __name__ == "__main__":
    main()
