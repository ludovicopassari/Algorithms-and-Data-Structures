def pop_min_edge(crossing):
    w_min, u_min, v_min = crossing[0]

    for item in crossing:
        w_curr, u_curr, v_curr = item

        if w_curr < w_min:
            w_min = w_curr
            u_min = u_curr
            v_min = v_curr
    crossing.remove((w_min, u_min, v_min))
    return w_min, u_min, v_min


def prim_jarnik(graph, start):
    # crea un albero vuoto
    mst = {}
    vertex_cloud = set()
    vertex_cloud.add(start)
    n = 0
    while len(vertex_cloud) != len(graph):
        crossing = []

        for vertex in vertex_cloud:
            for k in graph:
                if k not in vertex_cloud and k in graph[vertex]:
                    crossing.append((graph[vertex][k], vertex, k))

        w, u, v = pop_min_edge(crossing)
        vertex_cloud.add(v)
        mst[n] = (w, u, v)
        n += 1
    return mst


def main():
    graph = {
        "ME": {"CT": 93.6, "PA": 225.8},
        "PA": {"CT": 209.6, "ME": 225.8, "TP": 108.5},
        "CT": {"ME": 93.6, "PA": 209.6, "SR": 66.2},
        "TP": {"PA": 108.5},
        "SR": {"CT": 66.2, "CL": 159.6},
        "CL": {"SR": 159.6},
    }

    print(prim_jarnik(graph, "ME"))
    print(graph)


if __name__ == "__main__":
    main()
