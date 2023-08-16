
def DF_Search(adj_list: list, src: int or str, trg: int or str, queue=[]) -> bool:
    '''

    :param adj_list: list of edges for each node
    :param src: source node
    :param trg: target node
    :return:
    '''

    if queue == []:
        queue = [src]

    mynode = adj_list.

    for node in adj_list[src]:
        if node == trg:
            return True
        else:
            queue.insert(node, 0)

        return DF_Search(adj_list, queue[0], trg, queue)


graph = {1: [2, 3, 4],
         2: [3, 5],
         3: [4, 6],
         4: [5, 6],
         5: [6],
         6: [3, 4, 5],
         7: [7]}

isconnected = DF_Search(graph, 1, 6)