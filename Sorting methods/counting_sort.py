def counting_sort(A):
    """  
    Implementazione dell'algoritmo di counting sort.

    Args: La funzione prende in input un array da ordinare con elementi compresi nell'intervallo 0 < x < n

    Return: Ritorna l'array ordinato.

    """
    #elemento massimo all'interno dell'array di input
    k = max(A)
    #crea un array dentro cui sono presenti i conteggi delle occorrenze
    B = [0] * (k + 1)
    res= [0]  * len(A)

    #conto le occorrenze
    for i in range(len(A)):
        B[A[i]]+=1
    
    #somma l'elemento i-esimo con l'elemento i-1 esimo
    for i in range(1,len(B)):
        B[i] += B[i-1]

    for i in range(len(A)-1,-1,-1):
        res[B[A[i]]-1] = A[i]
        B[A[i]] -= 1  
    
    return res

def main():
    unsorted_numbers = [2, 10, 11, 8, 6]

    print("Unsorted data --> ", unsorted_numbers)
    print("Sorted data --> ", counting_sort(unsorted_numbers))

if __name__ == '__main__':
    main()
