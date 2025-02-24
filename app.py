graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H', 'I'],
    'E': ['B', 'J', 'K'],
    'F': ['C', 'L', 'M'],
    'G': ['C', 'N', 'O'],
    'H': ['D', 'P'],
    'I': ['D', 'Q'],
    'J': ['E', 'R'],
    'K': ['E', 'S'],
    'L': ['F', 'T'],
    'M': ['F', 'U'],
    'N': ['G', 'V'],
    'O': ['G', 'W'],
    'P': ['H'],
    'Q': ['I'],
    'R': ['J'],
    'S': ['K'],
    'T': ['L'],
    'U': ['M'],
    'V': ['N'],
    'W': ['O']
}

def bfs(graph_in, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph_in[node]:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    return None

start_node = 'A'
end_node = 'W'
print(bfs(graph, start_node, end_node))