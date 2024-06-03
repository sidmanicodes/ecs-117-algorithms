from typing import List, Tuple
import heapq

class UndirectedGraph:
    def __init__(self, node_count: int) -> None:
        self.node_count = node_count
        self.adj_list = {i: [] for i in range(node_count)}

    def add_edge(self, u, v, w) -> None:
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))

    def prim(self, start: int) -> List[Tuple[int, int, int]]:
        """
        Python implementation of Prim's algorithm for finding the MST from an
        arbitrary starting node
        """
        # Initialization
        mst = []
        keys = [float('inf') for _ in range(self.node_count)]
        parent = [None for _ in range(self.node_count)]
        in_mst = [False for _ in range(self.node_count)]
        keys[start] = 0
        pq = []
        
        # Push every node onto the heap
        for i, key in enumerate(keys):
            heapq.heappush(pq, (key, i))

        # While there are still unvisited nodes in the heap
        while pq:
            _, min_node = heapq.heappop(pq)

            # Prevent repeated nodes in the mst
            if in_mst[min_node]:
                continue

            in_mst[min_node] = True

            # Edge case to get rid of the initialized node
            if parent[min_node] is not None:
                mst.append((parent[min_node], min_node, keys[min_node]))

            # Iterate over all neighbors and weights in the adjacency list
            for neighbor, weight in self.adj_list[min_node]:
                # As long as the neighbor is not already in the MST and the
                # weight connecting the min_node and neighbor is smaller than
                # the current smallest distance of the neighbor
                if not in_mst[neighbor] and weight < keys[neighbor]:
                    # Update the key and parent of the neighbor, and push it to the heap
                    # so that we have updated information
                    keys[neighbor] = weight
                    parent[neighbor] = min_node
                    heapq.heappush(pq, (keys[neighbor], neighbor))
        return mst

    
# g = UndirectedGraph(6)
# g.add_edge(1, 3, 1)
# g.add_edge(3, 4, 2)
# g.add_edge(1, 4, 3)
# g.add_edge(2, 4, 3)
# g.add_edge(0, 3, 4)
# g.add_edge(1, 2, 5)
# g.add_edge(4, 5, 7)
# g.add_edge(2, 5, 8)
# g.add_edge(0, 1, 9)
# print(g.prim(0))