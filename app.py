# Initialize a 10x10 2D array
rows, cols = 10, 10
graph = [[0 for _ in range(cols)] for _ in range(rows)]

# Define the BFS function
def bfs(graph_in, start, end):
    queue = [[start]]
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        path = queue.pop(0)
        x, y = path[-1]

        if (x, y) == end:
            return path

        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if (nx, ny) not in visited and graph_in[nx][ny] == 0:
                        new_path = list(path) + [(nx, ny)]
                        queue.append(new_path)

    return None

start_node = (0, 0)
end_node = (9, 9)
print(bfs(graph, start_node, end_node))