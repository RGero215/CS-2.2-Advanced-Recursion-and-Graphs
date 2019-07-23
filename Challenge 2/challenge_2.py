import sys
from graph import Graph, Vertex


def create_graph_obj_from_file(file_name):
    file = open(file_name, 'r') 
    file_list = file.readlines()
    g = Graph()
    
    for item in range(2, len(file_list)):
        vertex = file_list[item].rstrip().replace('(', '').replace(')', '').split(',')
        if len(vertex) == 3:
            g.addEdge(vertex[0],vertex[1],vertex[2])
        else:
            g.add_both_edges(vertex[0], vertex[1])
    return g

if __name__ == "__main__":
    g = create_graph_obj_from_file('graph_data.txt')
    print(g.bfs_shortest_path(sys.argv[1], sys.argv[2]))
    print(g.num_of_edges_in_bfs())
    print('\n================================================\n')
    print(create_graph_obj_from_file('graph_data.txt'))
    # for from_id in graph.vertList:
    #         t = tuple(f'vertex {v.id} with a cost of {cost}' for v, cost in graph.getVertex(from_id).connectedTo.items())
    #         print(f"edge: {from_id} to: {t} \n")

    # print(graph)

