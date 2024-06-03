class UndirectedGraph:
    def __init__(self, node_count: int) -> None:
        self.node_count = node_count
        self.edges = []
        self.parents = [-1 for _ in range(self.node_count)]  # Initialize disjoint set (every node is a parent at first)

    def add_edge(self, node1: int, node2: int, weight: int) -> None:
        self.edges.append((node1, node2, weight))

    def union(self, node1: int, node2: int) -> None:
        """Unions two disjoint sets based on their ranks"""
        node1_root = self.find(node1)
        node2_root = self.find(node2)

        if node1_root != node2_root:
            # Determine which root has higher rank
            if self.parents[node1_root] < self.parents[node2_root]:  # node1_root has higher rank
                self.parents[node1_root] += self.parents[node2_root]  # Increase the rank of node1_root
                self.parents[node2_root] = node1_root  # Make node2_root a child of node1_root
            else:
                self.parents[node2_root] += self.parents[node1_root]  # Increase the rank of node2_root
                self.parents[node1_root] = node2_root  # Make node1_root a child of node2_root

    def find(self, node: int) -> int:
        """Finds the root of a disjoint set with path compression"""
        if self.parents[node] < 0:
            return node
        else:
            self.parents[node] = self.find(self.parents[node])  # Path compression
            return self.parents[node]

    def kruskal(self) -> list[tuple]:
        """
        Python implementation of Kruskal's algorithm
        Used to find the Minimum Spanning Tree of an undirected graph
        """
        # Sort the edges by weight
        sorted_edges = sorted(self.edges, key=lambda x: x[2])

        edge_set = []

        for node1, node2, weight in sorted_edges:
            # Get each node's root
            node1_root = self.find(node=node1)
            node2_root = self.find(node=node2)

            # As long as the roots are different (aka the nodes are in different sets),
            # we can add the edge to our edge set
            if node1_root != node2_root:
                edge_set.append((node1, node2, weight))
                self.union(node1=node1, node2=node2)

        return edge_set

# Example usage:
# g = UndirectedGraph(5)
# g.add_edge(0, 1, 3)
# g.add_edge(0, 3, 7)
# g.add_edge(0, 4, 8)
# g.add_edge(3, 4, 3)
# g.add_edge(3, 1, 4)
# g.add_edge(3, 2, 2)
# g.add_edge(1, 2, 1)

# mst_edges = g.kruskal()
# print("Edges in the MST:")
# for u, v, weight in mst_edges:
#     print(f"{u} -- {v} == {weight}")

# print("Parents array:", g.parents)
