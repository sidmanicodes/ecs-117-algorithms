class Graph:
    def __init__(self, vertices: int) -> None:
        self.vertices = range(vertices)
        self.edges = [] # Don't worry about validating edges
    def add_edge(self, u: int, v: int, w: int) -> None:
        self.edges.append((u, v, w))
    def bellman_ford(self, s: int) -> list[int]:
        # Initialize distances array
        d = [float('inf') for _ in range(len(self.vertices))]

        # Set starting node distance to 0
        d[s] = 0

        # Relax all edges |V| - 1 times
        for _ in range(len(self.vertices)-1):
            for u, v, w in self.edges:
                if d[u] != float('inf') and d[u] + w < d[v]:
                    d[v] = d[u] + w
        
        # Check for negative cycles
        for u, v, w in self.edges:
            if d[u] != float('inf') and d[u] + w < d[v]:
                print("Graph contains a negative cycle")
                return None
            
        return d
    
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

source = 0
distances = g.bellman_ford(s=source)

if distances:
    print(f"Vertex distances from source {source}")
    for vertex, distance in enumerate(distances):
        print(f"Vertex {vertex}: {distance} units")