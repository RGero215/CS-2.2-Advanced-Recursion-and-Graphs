from graph import Graph
import sys

def dfs_path_exist(path, start, end):
    '''Prints the data of the graph'''
    for v in path:
        if v.id == end:
            print(f'There exists a path between vertex {start} and {end}: TRUE')
            print(f'Vertices in the path: {path}')
            return True
    print(f'There is no path between vertex {start} and {end}: FALSE')
    print(path)
    return False

def main():
    '''Run path from graph file name'''
    if len(sys.argv) < 4:
        raise RuntimeError('Expecting file name, start vertex and end vertex')
    graph_file = sys.argv[1]
    start_vertex = int(sys.argv[2])
    end_vertex = int(sys.argv[3])

    graph = Graph()
    print('Type: ', graph.directed)
    graph.read_graph_from_file(graph_file)
    dfs_path_exist(graph.depth_first_search(start_vertex, end_vertex), start_vertex, end_vertex)

if __name__ == "__main__":
    main()