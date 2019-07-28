# from graph import Graph
from graph2 import Graph
import sys

def read_graph_from_file(file_name):
    file = open(file_name, 'r') 
    file_list = file.readlines()
    vertices = file_list[1].rstrip().split(',')
    valid_types = 'gGdD'
    graph_type = ''
    directed = False
    weighted = False
    edges_list = []

    if file_list[0].rstrip() in valid_types:
        graph_type = file_list[0].upper()
    else:
        raise ValueError('G or D is not specified')

    if graph_type == 'D':
        directed = True
    
    for item in range(2, len(file_list)):
        edge = file_list[item].rstrip().replace('(', '').replace(')', '').split(',')
        if len(edge) == 3:
            weighted = True
        edges_list.append(edge)
    
    graph = Graph(weighted, directed)

    for edge in edges_list:
        if weighted:
            graph.add_weighted_edge(int(edge[0]), int(edge[1]), int(edge[2]))
        else:
            graph.add_edge(int(edge[0]), int(edge[1]))

    return graph


def graph_data(graph):
    print(f"# Vertices: {graph.size}")
    print(f"# Edges: {len(graph.get_edge_list())}")
    print("Edge List:")
    for edge in graph.get_edge_list():
        print(edge)



if __name__ == "__main__":
    file_name = sys.argv[1]
    graph = read_graph_from_file(file_name)
    graph_data(graph)
    print(graph)

    
