from collections import deque

def bfs(start: str, adj_list: dict[int, list[int]], node_count: int) -> dict:
        # BFS is typically used to find the distance from the starting point
        # to all the other nodes in the graph. So, we will keep track of the 
        # distances here
        nodes = range(node_count)
        dist = {}
        for node in nodes:
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
            node = nodes[node_label]
            visited.add(node) # If node is already in visited, this has no effect
            for neighbor in adj_list[node]:
                # If the neighbor is unvisited, set the distance to the node's distance from the start + 1
                if neighbor not in visited:
                    dist[neighbor.label] = dist[node_label] + 1
                    queue.append(neighbor.label)
        
        return dist