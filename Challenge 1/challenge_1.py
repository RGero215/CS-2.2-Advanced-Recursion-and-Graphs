from graph import Graph

def create_graph_obj_from_file(file_name):
    file = open(file_name, 'r') 
    file_list = file.readlines()
    vertices = file_list[1].rstrip().split(',')
    g = {}

    for item in vertices:
        g[item] = []

    # print(g)
    
    for item in range(2, len(file_list)):
        vertex = file_list[item].rstrip().replace('(', '').replace(')', '').split(',')
        if len(vertex) == 3:
            # print(vertex[:len(vertex) - 1])
            if vertex[0] in g:
                g[vertex[0]] += [vertex[1]]
        else:
            if vertex[0] in g:
                g[vertex[0]] += [vertex[1]]
      
    # print(g)
    return g


if __name__ == "__main__":
    create_graph_obj_from_file('graph_data.txt')
    graph = Graph(create_graph_obj_from_file('graph_data.txt'))

    print("Vertices: {}".format(graph.vertices_count()))
    print("Edges: {}".format(graph.edges_count()))

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())
