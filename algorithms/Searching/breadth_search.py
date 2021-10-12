# Resource: https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
# Breadth first traversal - nothing's being searched.
# It goes to each key and visits their nodes.
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:  # while there's elements
        top = queue.pop(0)
        print(top, end=" ")

        for neighbour in graph[top]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = []
queue = []
bfs(visited, graph, 'A')
