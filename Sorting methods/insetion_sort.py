def insertion_sort(data):
    """
    Ordinamento di un'array implementato con l'algoritmo Insertion-Sort.

    Costo computazionale : O(n) nel caso migliore, un 0(n^2) nel caso peggiore

    Description: Ad ogni iterazione l'array è ordinato da 0 a j-1 e disordinato da j a n.
    """
    # dimensione dell'array
    n = len(data)

    for j in range(1, n):
        # elemento corrente
        key = data[j]

        # indice dell'elemento a sinistra di key
        i = j - 1
        # finchè non arrivi all'indice 0 e finchè l'elemento in i è maggiore di elem
        while i >= 0 and data[i] > key:
            # trasla a destra l'elemento in i
            data[i + 1] = data[i]
            i -= 1
        # aggiungi l'ultimo elemento
        data[i + 1] = key

    return data


def main():
    data = [12, 5, 3, 4]
    print("Unsorted Data -->", data)
    print("Sorted Data -->", insertion_sort(data))


if __name__ == "__main__":
    main()
