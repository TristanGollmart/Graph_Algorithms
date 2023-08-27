def shortest_path(graph, src, trg, visited = set()):
    queue = [[src, 0]]
    while queue:
        current, path_len = queue.pop()
        visited.add(current)
        if current == trg:
            return path_len
        for node in graph[current]:
            if node not in visited:
                queue.insert(0, [node, path_len+1])
    return -1


def make_undirected_graph(edge_list):
    graph = {}
    for edge in edge_list:
        node1, node2 = edge
        if node1 in graph:
            graph[node1].append(node2)
        else:
            graph[node1] = [node2]
        if node2 in graph:
            graph[node2].append(node1)
        else:
            graph[node2] = [node1]
    return graph


edges = [[1, 2],
         [1, 3],
         [2, 4],
         [3, 5],
         [5, 1],
         [3, 5],
         [4, 6],
         [6, 7],
         [4, 5],
         [8, 8]]
graph = make_undirected_graph(edges)

src = 1
trg = 6
path_len = shortest_path(graph, src, trg, set())
print(f"shortest path from {src} to {trg}: ", path_len)