def BF_search(graph, src, trg, visited: set):
    queue = [src]
    visited.add(src)
    while queue:
        current = queue.pop()
        if current == trg:
            return True
        for node in graph[current]:
            if node not in visited:
                queue.insert(node, 0)
    return False

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
         [5, 6],
         [3, 6],
         [6, 7],
         [4, 5]]
graph = make_undirected_graph(edges)

isconnected = BF_search(graph, 1, 6, set())
print("path exists from 1 to 6: ", isconnected)