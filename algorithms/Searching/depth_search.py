# Resource: https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
# Depth first traversal - nothing's being searched.
# It goes to the first node and dives into their node's nodes.
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)  # will jump to previous call if there is nothing. Like when going from D to E.


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = set()
dfs(visited, graph, 'A')
