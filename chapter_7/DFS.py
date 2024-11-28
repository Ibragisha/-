def dfs(graph, start):
    visited = set()
    result = []
    
    def dfs_recursive(vertex):
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            for neighbor in graph[vertex]:
                dfs_recursive(neighbor)
    
    dfs_recursive(start)
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C', 'I'],
    'H': ['E'],
    'I': ['G']
}

start_vertex = 'A'
result = dfs(graph, start_vertex)
print("Обход в глубину:", result)
