import sys
from graph import Graph, Vertex


def main():
    g = Graph()
    g.read_graph_from_file('graph_data.txt')
    start = int(sys.argv[2])
    end = int(sys.argv[3])
   
    shortest_path = g.find_shortest_path(start, end)
    print(f'Vertices in shortest path: {shortest_path}')
    print(f'Number of edges in shortest path: {len(shortest_path ) - 1}')
    

if __name__ == "__main__":
    main()

    
    

