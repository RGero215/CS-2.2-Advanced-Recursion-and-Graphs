class Graph(object):
    '''
    Adjacency list Graph implementation
    '''

    def __init__(self, weighted=False, directed=True):
        '''Initialized a graph'''
        self.graph = {}
        self.weights = {}
        self.weighted = weighted
        self.directed = directed

    def __repr__(self):
        '''String representation of the graph'''
        return f'Graph({self.graph})'

    @property
    def size(self):
        '''Return the size'''
        return len(self.graph)

    def add_vertex(self, vertex):
        '''Add a vertex to the graph'''
        if vertex in self.graph:
            raise KeyError(f'{vertex} is already in the graph.')
        self.graph[vertex] = set()

    def add_edge(self, from_vertex, to_vertex):
        '''Connects two vertex with directed vertex'''
        if self.weighted:
            raise TypeError('add_edge() cannot be weighted')
        
        if from_vertex not in self.graph:
            self.add_vertex(from_vertex)
        
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)

        if to_vertex not in self.graph[from_vertex]:
            self.graph[from_vertex].add(to_vertex)

            if self.directed is False:
                self.graph[to_vertex].add(from_vertex)
    
    def add_weighted_edge(self, from_vertex, to_vertex, weight):
        '''Add weighted directed edge to the graph'''
        assert isinstance(weight, int), f'weight is not an int: {weight}'

        if self.weighted is False:
            raise TypeError('add_weighted_edge() cannot be call on unweighted graph')

        if from_vertex not in self.graph:
            self.add_vertex(from_vertex)

        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)

        if to_vertex not in self.graph[from_vertex]:
            self.graph[from_vertex].add(to_vertex)
            self.weights[(from_vertex, to_vertex)] = weight

            if self.directed:
                self.graph[to_vertex].add(from_vertex)
                self.weights[(to_vertex, from_vertex)] = weight

    def has_vertex(self, vertex_key):
        '''Find vertex by the key and return True or False'''
        if vertex_key not in self.graph:
            return False
        return True

    def get_vertices(self):
        '''Return the list of all vertices in the graph'''
        return [vertex for vertex in self.graph.keys()]

    def get_neighbors(self, from_vertex):
        '''List all vertices neighbors'''
        if from_vertex not in self.graph:
            raise KeyError(f'{from_vertex} is not in the graph')
        return self.graph[from_vertex]

    def get_edge_list(self):
        '''Return a list of edges'''
        edge_list = set()

        for from_vertex in self.graph:
            for to_vertex in self.get_neighbors(from_vertex):
                if self.weighted:
                    weight = self.weights[(from_vertex, to_vertex)]
                
                if self.directed and self.weighted:
                    edge_list.add((from_vertex, to_vertex, weight))
                if self.directed and not self.weighted:
                    edge_list.add((from_vertex, to_vertex))

                if not self.directed and self.weighted:
                    if (to_vertex, from_vertex, weight) not in edge_list:
                        edge_list.add((from_vertex, to_vertex, weight))
                if not self.directed and not self.weighted:
                    if(to_vertex, from_vertex) not in edge_list:
                        edge_list.add((from_vertex, to_vertex))

        return  edge_list

if __name__ == "__main__":
    pass
