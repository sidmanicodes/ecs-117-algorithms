def create_adj_list(node_count: int, edges: tuple[int, int, int]) -> dict[int, list[int]]:
    adj_list = {}
    for i in range(node_count):
        adj_list[i] = []

    for u, v, _ in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list