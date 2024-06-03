from collections import deque

class Graph:
    class Node:
        def __init__(self, label: str) -> None:
            self.label = label
            self.color = 'white'  # Default color, indicating unvisited
            self.discovery_time = -1
            self.finish_time = -1

        def __eq__(self, other) -> bool:
            return self.label == other.label if isinstance(other, Graph.Node) else False

        def __hash__(self) -> int:
            return hash(self.label)

        def __repr__(self) -> str:
            return f'{self.label}: [{self.discovery_time}, {self.finish_time}]'

    def __init__(self, nodes: list[str]) -> None:
        if len(nodes) < 1:
            raise ValueError("Enter at least one node")
        self.nodes = {node: self.Node(node) for node in nodes}  # Store node instances by label
        self.adj_list = {self.nodes[node]: [] for node in nodes}  # Use references to these instances
        self.time = 0 # Global time

    def __repr__(self) -> str:
        return '\n'.join(f'{node}: {[n.label for n in neighbors]}' for node, neighbors in self.adj_list.items())

    def add_node(self, node: str) -> None:
        if node not in self.nodes:
            new_node = self.Node(node)
            self.nodes[node] = new_node
            self.adj_list[new_node] = []

    def remove_node(self, node: str) -> None:
        target_node = self.nodes.get(node)
        if target_node:
            self.adj_list.pop(target_node, None)
            for neighbors in self.adj_list.values():
                if target_node in neighbors:
                    neighbors.remove(target_node)
            del self.nodes[node]  # Also remove from node dictionary

    def add_edge(self, node1: str, node2: str) -> None:
        if node1 in self.nodes and node2 in self.nodes:
            node1 = self.nodes[node1]
            node2 = self.nodes[node2]
            if node2 not in self.adj_list[node1]:
                self.adj_list[node1].append(node2)
            else:
                raise ValueError("Node 2 is already an edge of Node 1")
        else:
            raise ValueError("Either one or both nodes are not in the Graph.")

    def set_node_color(self, node_label: str, color: str) -> None:
        if node_label in self.nodes:
            self.nodes[node_label].color = color
        else:
            raise ValueError("Node does not exist in the graph")
        
    def dfs_recursive(self) -> None:
        # Make sure all Nodes are unvisited yet
        for node in self.nodes.values():
            node.color = "white"
            node.discovery_time = -1
            node.finish_time = -1
        
        # Set the time to 0
        self.time = 0

        # Explore all unvisited Nodes
        for node in self.nodes.values():
            if node.color == "white":
                self._visit_node(node=node)
        
    def _visit_node(self, node: Node) -> None:
        # Node gets discovered and is being visited
        self.time += 1
        node.discovery_time = self.time
        node.color = "grey"

        # Visit all adjacent nodes
        for neigbor in self.adj_list[node]:
            if neigbor.color == "white":
                self._visit_node(neigbor)

        # Once we have dived as deep as we can into the graph,
        # we backtrack and set the nodes to visited
        node.color = "black"
        self.time += 1
        node.finish_time = self.time

    def bfs(self, start: str) -> dict:
        if start not in self.nodes:
            raise KeyError(f"{start} is not a node in the graph")

        # BFS is typically used to find the distance from the starting point
        # to all the other nodes in the graph. So, we will keep track of the 
        # distances here
        dist = {}
        for node in self.nodes:
            dist[node] = float('inf')

        # Initialize starting distance to 0
        dist[start] = 0        

        # Initialize set of visited nodes, and queue
        visited = set()
        queue = deque()

        # Add the start node to the visited set and queue
        visited.add(start)
        queue.append(start)

        # As long as the queue isn't empty
        while queue:
            # Dequeue the first node and explore all of its neighbors
            node_label = queue.popleft()
            node = self.nodes[node_label]
            visited.add(node) # If node is already in visited, this has no effect
            for neighbor in self.adj_list[node]:
                # If the neighbor is unvisited, set the distance to the node's distance from the start + 1
                if neighbor not in visited:
                    dist[neighbor.label] = dist[node_label] + 1
                    queue.append(neighbor.label)
        
        return dist



# Example usage
graph = Graph(["a", "b", "c", "d"])
graph.add_edge("a", "b")
graph.add_edge("a", "c")
graph.add_edge("b", "d")
graph.add_edge("c", "d")
graph.add_edge("d", "a")

graph.dfs_recursive()
print(graph.nodes)  # Output nodes to see their discovery and finish times
print(graph.bfs(start="a"))