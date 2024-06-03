def dfs(mst, start_node):
    """
    Perform a DFS traversal on the MST starting from start_node.
    Returns the path as a list of nodes in the order they are visited.
    
    Args:
    mst (dict): Adjacency list representation of the MST.
    start_node: The starting node for DFS.
    
    Returns:
    list: The DFS traversal path.
    """
    visited = set()  # Set to keep track of visited nodes
    stack = [start_node]  # Stack for DFS
    path = []  # List to store the path
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            # Add neighbors to the stack in reverse order to maintain correct DFS order
            for neighbor in reversed(mst[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return path