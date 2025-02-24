graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B', 'I', 'J'],
    'F': ['C', 'K'],
    'G': ['C', 'L'],
    'H': ['D'],
    'I': ['E'],
    'J': ['E', 'M'],
    'K': ['F'],
    'L': ['G'],
    'M': ['J']
}

def bfs(graph_in, start, end):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node == end:
            visited.append(node)
            return visited
        if node not in visited:
            visited.append(node)
            queue.extend(graph_in[node])

    return visited

start_node = 'A'
end_node = 'H'
print(bfs(graph, start_node, end_node))