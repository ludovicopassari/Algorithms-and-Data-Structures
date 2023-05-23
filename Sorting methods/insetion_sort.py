"""
ALGORITMO INSERTION-SORT
"""

def insertion_sort(array):
    """
    Ordinamento di un'array implementato con l'algoritmo Insertion-Sort.

    Costo computazionale : O(n) nel caso migliore, un 0(n^2) nel caso peggiore

    Description: Ad ogni iterazione l'array è ordinato da 0 a j-1 e disordinato da j a n.

    """

    # dimensione dell'array
    n = len(array)

    for j in range(1, n):
        # elemento corrente
        key = array[j]
        # indice dell'elemento a sinistra di key
        i = j - 1
        # finchè non arriva all'indice 0 e finchè l'elemento in i è maggiore di key
        while i >= 0 and array[i] > key:
            # trasla a destra l'elemento in i
            array[i + 1] = array[i]
            i -= 1
        # aggiungi l'ultimo elemento
        array[i + 1] = key

    return array


def main():
    unsorted_array = [12, 5, 3, 4]
    print("Unsorted Data -->", unsorted_array)
    print("Sorted Data -->", insertion_sort(unsorted_array))


if __name__ == "__main__":
    main()
