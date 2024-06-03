from prim import UndirectedGraph
from create_adj_list import create_adj_list
from dfs import dfs

def traveling_salesman(start: int, node_count: int) -> list[int]:
    """
    Python implementation of the 2-Approximation for the
    Traveling Salesman problem

    Arguments:
        - start (int): the starting node
        - node_count (int): number of nodes in the graph

    Returns:
        - path (list[int]): best path that approximately solves TSP
    """
    mst = graph.prim(start=start)
    adj_list = create_adj_list(node_count=node_count, edges=mst)
    path = dfs(mst=adj_list, start_node=start)
    return path

graph = UndirectedGraph(5)
graph.add_edge(0, 1, 6)
graph.add_edge(0, 2, 8)
graph.add_edge(0, 3, 5)
graph.add_edge(0, 4, 4)

graph.add_edge(1, 2, 6)
graph.add_edge(1, 3, 3)
graph.add_edge(1, 4, 5)

graph.add_edge(2, 3, 3)
graph.add_edge(2, 4, 5)

graph.add_edge(3, 4, 8)

path = traveling_salesman(start=0, node_count=5)
print(path)