def is_root(tree, node):
    """
    Verifica se un nodo è il nodo radice dell'albero

    Args : La funzione prende in input un albero binario e un nodo

    Return : Ritorna True se il nodo è radice, False se il nodo non lo è.

    """
    return tree[node]["parent"] is None


def is_leaf(tree, node):
    """
    Verfica se un nodo è una foglia o meno.

    Args: La funzione prende in input un albero binario e un nodo.

    Return: Ritorna True se il nodo è un nodo foglia altrimenti ritorna False.

    Description: Un nodo è considerato foglia se entrambi i figli sono 'None'
    """
    return tree[node]["left"] is None and tree[node]["right"] is None


def preorder(tree, curr_node, visited=[]):
    """
    Effettua un attraversamento preorder ricorsivamente

    Args : La funzione prende in input un albero binario, un nodo  e una lista dei nodi visitati

    Return : ritorna la lista dei nodi visitati

    Description :  Un attraversamento preorder prevede che sia visitata prima la radice e poi in ordine il sottoalbero con radice nel figlio sinistro e successivameente il sottoalbero con radice nel figlio destro.
    """

    if curr_node is not None:
        visited.append(curr_node)

        preorder(tree, tree[curr_node]["left"], visited)
        preorder(tree, tree[curr_node]["right"], visited)
    return visited


def postorder(tree, curr_node, visited=[]):
    """
    Effettua un attraversamento postorder di un albero binario

    Arga: La funzione prende in input un albero binario , un nodo da cui partire per attraversare e una lista che conterrà tutti i nodi visitati.

    Return : Ritorna una lista con tutti i nodi visitati.

    Description : L'attraversamento postoorder prevede che venga visitata per primo il sottoalbero sinistro, poi quello destro e successivamente la radice.

    """
    if curr_node is not None:
        postorder(tree, tree[curr_node]["left"])
        postorder(tree, tree[curr_node]["right"])
        visited.append(curr_node)

    return visited


def inorder(tree, curr_node, visited=[]):
    """
    Effettua un attraversamento inorder di un albero binario ricorsivamente.

    Args : La funzione prende in input un albero binario, un nodo da cui partire ad attraversare e una lista dei nodi visitati.

    Return: Ritorna una lista dei nodi visitati.

    Description: L'attraversamento inorder prevede che sia visitato prima il ottoalbeo di sinistra poi la radice e per ultimo il sottolabero di destra.

    """
    if curr_node is not None:
        inorder(tree, tree[curr_node]["left"])
        visited.append(curr_node)
        inorder(tree, tree[curr_node]["right"])

    return visited


def breadth_first(tree, start_node):
    """
    Effettua una visita in ampiezza di un albero binario.

    Args: La funzione in input un albero binario e un nodo da cui partire per attraversare l'albero.

    Return: Ritorna una lista dei nodi visitati

    Description: La visita in ampiezza prevede che l'albero sia visitato per livelli.
    """
    visited = list()

    queue = [start_node]

    while queue:
        curr = queue.pop(0)
        visited.append(curr)
        for child in get_children(tree, curr):
            queue.append(child)

    return visited


def get_sibling(tree, node):
    """
    Restituisce il fratello di un nodo se esiste.
    """
    if not is_root(tree, node):
        parent = tree[node]["parent"]

        if node == tree[parent]["left"]:
            return tree[parent]["right"]
        if node == tree[parent]["right"]:
            return tree[parent]["left"]


def get_cousins(tree, node):
    """
    Restituisce il cugino di un nodo se esiste.
    """
    zio = get_sibling(tree, tree[node]["parent"])

    return get_children(tree, zio)


def get_children(tree, node):
    """
    Restituisce i figli  di un nodo se esistono
    """
    children_list = list()

    if tree[node]["left"] is not None:
        children_list.append(tree[node]["left"])

    if tree[node]["right"] is not None:
        children_list.append(tree[node]["right"])

    return children_list


def depth(tree, node):
    """
    Misura la profondità di un nodo all'interno di un albero binario.

    Agrs: La funzione prende in input un albero e il nodo di cui si vuole misurare l'altezza.

    Return: Ritorna il valore di profondità del nodo

    Description: La profpndità di un nodo è quanti livelli lo separano dalla radice.

    """
    if is_root(tree, node):
        return 1
    else:
        return 1 + depth(tree, tree[node]["parent"])


def height(tree, node):
    """
    Misura l'altezza di un nodo all'interno di un albero binario.

    Args: La funzione prende in input un albero binario e il nodo di cui si vuole conoscere l'altezza.

    Return: Ritorna l'altezza del nodo.

    Descrition: L'altezza del nodo è quanti livelli separano un nodo da un nodo foglia.
    """
    if is_leaf(tree, node):
        return 0
    else:
        return 1 + max(height(tree, child) for child in get_children(tree, node))


def main():
    # albero binario
    tree = {
        16: {"parent": None, "left": 7, "right": 19},
        7: {"parent": 16, "left": 2, "right": 8},
        19: {"parent": 16, "left": 17, "right": 21},
        2: {"parent": 7, "left": None, "right": None},
        8: {"parent": 7, "left": None, "right": None},
        21: {"parent": 19, "left": None, "right": None},
        17: {"parent": 19, "left": None, "right": None},
    }

    print("Depth -->", depth(tree, 21))
    print("Height -->", height(tree, 16))
    print("\nTraversal:\n")
    print("preorder --> ", preorder(tree, 16))
    print("postorder --> ", postorder(tree, 16))
    print("inorder --> ", inorder(tree, 16))
    print("breadth_first --> ", breadth_first(tree, 16))


if __name__ == "__main__":
    main()
