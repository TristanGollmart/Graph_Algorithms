
def count_connected_components(graph: dict)-> int:
    visited = set()
    cnter = 0
    for node in graph:
        if explore(graph, node, visited) == True:
            cnter = cnter + 1

    return cnter

def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True

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

n_components = count_connected_components(graph)
print("number of components: ", n_components)