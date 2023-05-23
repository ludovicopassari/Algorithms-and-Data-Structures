def counting_sort(A):
    k = max(A)
    B = [0] * (k + 1)
    result = [0] * len(A)

    # conta le occorrentze
    for i in range(len(A)):
        B[A[i] - 1] += 1

    # sommo ogni elemento con il suo precedente
    for i in range(1, len(B):
        B[i] += B[i - 1]

    for i in range(len(A) - 1, -1, -1):
        result[B[A[i]] - 1] = A[i]
        B[A[i] - 1] -= 1
        
    return result


def main():
    data = [7, 2, 2, 7, 7, 1, 4, 5, 3, 2]
    counting_sort(data)


if __name__ == "__main__":
    main()
