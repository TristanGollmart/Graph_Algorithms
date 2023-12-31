def DF_Search(graph: dict, src: int or str, trg: int or str, visited: set) -> bool:
    '''

    :param visited:
    :param adj_list: list of edges for each node
    :param src: source node
    :param trg: target node
    :return:
    '''

    print("src: ", src)
    if src == trg:
        return True
    if src in visited:
        return False

    visited.add(src)
    for node in graph[src]:
        # visited.append(node)
        if DF_Search(graph, node, trg, visited):
            return True
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

isconnected = DF_Search(graph, 1, 6, set())
print("path exists from 1 to 6: ", isconnected)