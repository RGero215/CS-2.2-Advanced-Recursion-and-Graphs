from graph import Graph
import sys

def main():
    graph_file = sys.argv[1]
    graph = Graph()
    graph.directed = False
    graph.read_graph_from_file(graph_file)
    result = graph.is_Eulerian()
    if result == 0:
        print('Graph is not Eulerian')
    elif result == 1:
        print('Graph has a Euler path')
    else:
        print(f'Graph has a Euler cycle: {True}')

if __name__ == "__main__":
    main()