import numpy as np
def count_connected_components(grid: list)-> int:
    '''
    finds connected components in grid, counting all islands of 1s
    :param grid: binary list of 0s and 1s
    :return:
    '''
    visited = set()
    cnter = 0
    for c in range(np.shape(grid)[1]):
        for r in range(np.shape(grid)[0]):
            if grid[(r, c)]:
                if explore(grid, r, c, visited) == True:
                    cnter = cnter + 1
    return cnter

def explore(grid, r, c, visited):
    '''
    explores islands defined my connected domains of "TRUE" values
    :param grid:
    :param r:
    :param c:
    :param visited:
    :return:
    '''
    if (r, c) in visited:
        return False
    visited.add((r, c))

    neighbours = []
    if r > 0: neighbours.append((r-1, c))
    if r < np.shape(grid)[0]-1: neighbours.append((r+1, c))
    if c > 0: neighbours.append((r, c-1))
    if c < np.shape(grid)[1]-1: neighbours.append((r, c+1))

    for neighbor in neighbours:
        if grid[neighbor]:
            explore(grid, *neighbor, visited)

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


nrows = 10
p = 0.25
grid = np.random.random((nrows, nrows)) < p

n_components = count_connected_components(grid)
print("number of components: ", n_components)