def largest_component(graph):
    visited = set()
    largest = 0
    for node in graph:
        size = explore(graph, node, visited, num_nodes=0)
        if size > largest:
            largest = size

    return largest


def explore(graph, current, visited, num_nodes):
    if current in visited:
        return num_nodes
    visited.add(current)
    num_nodes = num_nodes + 1

    for neighbor in graph[current]:
        num_nodes = explore(graph, neighbor, visited, num_nodes)

    return num_nodes


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
         [6, 7],
         [4, 5],
         [8, 9]]
graph = make_undirected_graph(edges)

num_nodes = largest_component(graph)
print("number of nodes in largest component: ", num_nodes)