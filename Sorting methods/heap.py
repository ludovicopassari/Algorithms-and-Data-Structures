def get_right_child(i):
    return (i * 2) + 2


def get_left_child(i):
    return (i * 2) + 1


def swap(data, x, y):
    data[x], data[y] = data[y], data[x]


def max_heapify(data, i, heapsize):
    """
    Fa scendere il valore di data[i] nel max_heap in modo che il sottoalbero con radice in i diventi un heap
    """
    # indice dell'elemento più grande(presunto tale)
    largest = i

    left = get_left_child(i)
    right = get_right_child(i)

    if left < heapsize and data[left] > data[i]:
        largest = left

    if right < heapsize and data[right] > data[largest]:
        largest = right

    if i != largest:
        data[i], data[largest] = data[largest], data[i]
        max_heapify(data, largest, heapsize)


def build_max_heap(data, heapsize):
    for i in range(len(data), -1, -1):
        max_heapify(data, i, heapsize)


def heapsort(data):
    heapsize = len(data)

    build_max_heap(data, heapsize)

    for i in range(heapsize - 1, -1, -1):
        print(data)
        data[0], data[i] = data[i], data[0]
        max_heapify(data, 0, heapsize)


def main():
    unsorted_data = [7, 30, 20, 15, 52]
    heapsize = len(unsorted_data)
    # heapsort(unsorted_data)
    build_max_heap(unsorted_data, heapsize)
    print(unsorted_data)


if __name__ == "__main__":
    main()
