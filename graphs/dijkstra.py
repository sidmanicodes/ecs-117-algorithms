import heapq

class Graph:
    def __init__(self, nodes: int) -> None:
        self.nodes = nodes
        self.adj_list = {i: [] for i in range(self.nodes)}

    def add_node(self, node: int) -> None:
        self.nodes.append(node)
        self.adj_list[node] = []

    def add_edge(self, node1: int, node2: int, weight: int) -> None:
        if node1 not in range(self.nodes) or node2 not in range(self.nodes):
            raise IndexError("One or more nodes not found in graph")
        
        self.adj_list[node1].append((node2, weight))
        self.adj_list[node2].append((node1, weight))

    def dijkstra_array(self, start: int) -> list[int]:
        # Initialize all distances except start to inf
        dist = [float('inf') for _ in range(self.nodes)]
        visited = [False for _ in range(self.nodes)]
        dist[start] = 0

        for _ in range(self.nodes):
            # ------------------------------------------------------------------------
            # Since we are choosing not to use a priority queue, we will have to
            # find the minimum node each time by iterating through all the nodes; O(V)
            # ------------------------------------------------------------------------
            # This is a greedy process
            # ------------------------------------------------------------------------
            min_dist = float('inf')
            min_node = None
            for node in range(self.nodes):
                if not visited[node] and dist[node] < min_dist:
                    min_dist = dist[node]
                    min_node = node

            visited[min_node] = True

            # Explore minimum node's adjacency list
            for neighbor, weight in self.adj_list[min_node]:
                # If we have not visited the neighbor and it is faster to go through the 
                # min node than straight to the neighbor, update the distance to the neighbor
                if not visited[neighbor] and dist[min_node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[min_node] + weight

        return dist

    def dijkstra_heap(self, start: int) -> tuple[list[int], list[int]]:
        # Initialize distances
        dist = [float('inf') for _ in range(self.nodes)]
        pi = [None for _ in range(self.nodes)]
        dist[start] = 0
        
        pq = [(0, start)] # priority queue; (distance from start, node)

        # As long has we have unvisited nodes in the priority queue
        while pq:
            # Get the unvisited node with the smallest distance and its source 
            min_dist, min_node = heapq.heappop(pq)

            # If the node is outdated (meaning that we've found a better path),
            # disregard the node
            if min_dist > dist[min_node]:
                continue

            # Explore the neighbors of the min_node
            for neighbor, weight in self.adj_list[min_node]:
                distance = min_dist + weight

                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    pi[neighbor] = min_node
                    heapq.heappush(pq, (distance, neighbor))

        return (dist, pi)
    
g = Graph(5)
g.add_edge(0, 1, 3)
g.add_edge(0, 3, 7)
g.add_edge(0, 4, 8)
g.add_edge(3, 4, 3)
g.add_edge(3, 1, 4)
g.add_edge(3, 2, 2)
g.add_edge(1, 2, 1)
distances, parents = g.dijkstra_heap(start=0)

for i in range(g.nodes):
    print(f"Node {i} with parent {parents[i]}: {distances[i]}")