def create_binary_search_tree():
    return dict()


def show_tree(tree):
    for node in tree:
        print(node, tree[node])


def get_root(tree):
    for node in tree:
        if tree[node]["parent"] is None:
            return node


def get_min(tree, curr):
    if tree[curr]["left"] is None:
        return curr
    else:
        return get_min(tree, tree[curr]["left"])


def get_max(tree, curr):
    if tree[curr]["right"] is None:
        return curr
    else:
        return get_max(tree, tree[curr]["right"])


def add_root(bst, root_value):
    # se la struttura ad albero non ha ancora una radice
    if len(bst) < 1:
        # inserisce il nodo radice nell'albero binario di ricerca
        bst[root_value] = {"parent": None, "left": None, "right": None}


def tree_search(tree, curr_node, target):
    if curr_node is None:
        return "not found"
    if target == curr_node:
        return curr_node
    if target < curr_node:
        return tree_search(tree, tree[curr_node]["left"], target)
    else:
        return tree_search(tree, tree[curr_node]["right"], target)


def tree_search_iterative(tree, curr, target):
    while curr is not None and curr != target:
        if target < curr:
            curr = tree[curr]["left"]
        else:
            curr = tree[curr]["right"]

    return curr


def insert(bst, node_value):
    x = get_root(bst)
    y = x

    while y is not None:
        x = y
        if node_value < y:
            y = bst[x]["left"]
        else:
            y = bst[x]["right"]

    bst[node_value] = {"parent": x, "left": None, "right": None}

    if node_value < x:
        bst[x]["left"] = node_value
    elif node_value >= x:
        bst[x]["right"] = node_value


def get_successor(tree, node):
    if tree[node]["right"] is not None:
        return get_min(tree, tree[node]["right"])
    else:
        parent = tree[node]["parent"]
        while parent < node and parent is not None:
            parent = tree[parent]["parent"]

        return parent


def get_predecessor(tree, node):
    if tree[node]["left"] is not None:
        return get_max(tree, tree[node]["left"])
    else:
        parent = tree[node]["parent"]
        while parent > node and parent is not None:
            parent = tree[parent]["parent"]
        return parent


def get_children(tree, node):
    children_list = []
    if node in tree:
        if tree[node]["right"] is not None:
            children_list.append(tree[node]["right"])
        if tree[node]["left"] is not None:
            children_list.append(tree[node]["left"])
        return children_list


def transplant(tree, z, new):
    z_parent = tree[z]['parent']

    if z_parent is None:
        pass
    #se z è il figlio sinistro
    elif tree[z_parent]['left'] == z:
        #modifico il genitore di z
        tree[z_parent]['left'] = new
        tree[new]['parent'] = z_parent

    elif tree[z_parent]['right'] == z:
        #modifico il genitore di z
        tree[z_parent]['right'] = new
        
    
def delete(tree, z):
   #se z non ha figli
    if tree[z]['left'] is None and tree[z]['right'] is None:
        z_parent =  tree[z]['parent']

        #se z è figlio sinistro
        if tree[z_parent]['left'] == z:
            tree[z_parent]['left'] = None
            
        else:
            tree[z_parent]['right'] = None
    #se ha un solo figlio a sinistra
    elif tree[z]['left'] is not None and tree[z]['right'] is None:
        #il sostituto di z è il suo figlio di sinistra
        new =  tree[z]['left']
        transplant(tree,z,new)
    #se ha un solo figlio a destra
    elif tree[z]['left'] is  None and tree[z]['right'] is not None:
        new =  tree[z]['right']
        transplant(tree,z,new)
    #se ha tutti e due i figli
    else:
        y = get_successor(tree,z)
        print(y)
        tree[y]['left'] = tree[z]['left']
        tree[ tree[z]['left']]['parent'] = y
        transplant(tree,z,y)


       

def main():
    bst = create_binary_search_tree()
    add_root(bst, 15)
    insert(bst, 6)
    insert(bst, 3)
    insert(bst, 7)
    insert(bst, 13)
    insert(bst, 9)
    insert(bst, 2)
    insert(bst, 4)
    insert(bst, 18)
    insert(bst, 17)
    insert(bst, 20)
    # print(tree_search(bst, 15, 3))
    # print(tree_search_iterative(bst, 15, 20))
    print("BST -->", bst)
    delete(bst,7)
    print()
    #print(get_max(bst, 2))
    print("BST -->", bst)


if __name__ == "__main__":
    main()
