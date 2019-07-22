class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {} # key is vertex obj, value is cost
    
    def addNeighbor(self, nbr, cost=None): # nbr is vertex obj
        self.connectedTo[nbr] = cost
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self): #returns vertex objects List
        return self.connectedTo.keys()

    def getId(self):
        return self.id
    
    def getWeight(self, nbr): # nbr vertex object
        return self.connectedTo[nbr]
    
class Graph:
    def __init__(self):
        self.vertList = {} #dict of id key and vertex obj value
        self.numVertices = 0
    
    def __str__(self):
        result = ''
        for from_id in self.getVertices():
            t = tuple(f'vertex {v.id} with a cost of {cost}' for v, cost in self.getVertex(from_id).connectedTo.items())
            result += f"edge: {from_id} to: {t} \n"
        return result
    
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n): # returns Vertex obj with id n
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n): # check if vertex obj n in self
        return n in self.vertList
    
    # graph user will need to call this twice for undirected graph
    def addEdge(self, f, t, cost= 0): # f: from, t: to
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    # for undirected, need both directions
    def add_both_edges(self, key1, key2):
        self.addEdge(key1, key2)
        self.addEdge(key2,key1)
    
    def getVertices(self): # gets List of ids, not vertex obj
        return self.vertList.keys()

    def bfs_connected_component(self, start):
        """
        Visit all the vertex of the graph connected component using BFS
        """
        explored = [] # keep track of all visited vertex
        queue = [start] #keep track of vertex checked

        while queue: # loops until there are vertex
            vertex = queue.pop(0) # pop first vertex from queue
            if vertex not in explored:
                explored.append(vertex) # add vertex to list of checked nodes
                neighbours = self.getVertex(vertex)

                for neighbour in neighbours.connectedTo.keys(): #add neighbour of vertex to queue
                    queue.append(neighbour.id)
        return explored

    def bfs_shortest_path(self, start, end):
        """
        finds shortest path between 2 nodes of a graph using BFS
        """
        explored = [] # Keep track of explored vertex
        queue = [[start]] # Keep track of all the paths to be checked

        if start == end: # return path if start is end
            return start
        
        while queue: # Keep looping until all possible path have been checked
            path = queue.pop(0) # pop the first path from the queue
            vertex = path[-1] #get the las vertex from the path
            if vertex not in explored:
                neighbours = self.getVertex(vertex)
                # Goes through the neighbours and construct a new path
                # and push it into the queue
                for neighbour in neighbours.connectedTo.keys():
                    new_path = list(path)
                    new_path.append(neighbour.id)
                    queue.append(new_path)
                    
                    if neighbour.id == end: # return new path if neighbour is end
                        return new_path
                explored.append(vertex)
        return "Connecting path doesn't exist"

    def num_of_edges_in_bfs(self, start, end):
        return f'Number of edges in shortest path: {len(self.bfs_shortest_path(start, end))}'

    
    def __iter__(self):
        return iter(self.vertList.values())

if __name__ == "__main__":
    
    g = Graph()
    
    g.add_both_edges(1,2)
    g.add_both_edges(1,4)
    g.add_both_edges(2,3)
    g.add_both_edges(2,4)
    g.add_both_edges(2,5)
    g.add_both_edges(3,5)

    print(g.getVertices())
    print(g)
    print("BFS: ", g.bfs_connected_component(1))
    print("BFS Shortest Path: ", g.bfs_shortest_path(1, 5))
    print(g.num_of_edges_in_bfs(1,5))
    print(g.vertList)


    # g = Graph()
    
    # g.add_both_edges(g,'A','B')
    # g.add_both_edges(g,'A','C')
    # g.add_both_edges(g,'A','E')
    # g.add_both_edges(g,'B','D')
    # g.add_both_edges(g,'B','E')
    # g.add_both_edges(g,'C','F')
    # g.add_both_edges(g,'C','G')
    # g.add_both_edges(g,'E','D')
    
    # print(g.getVertices())
    # print(g)
    # print("BFS: ", g.bfs_connected_component('A'))
    # print("BFS Shortest Path: ", g.bfs_shortest_path('G', 'D'))

    d = Graph()
    d.addEdge(1,2,10)
    d.addEdge(1,4,5)
    d.addEdge(2,3,5)
    d.addEdge(2,4,7)

    print(d.getVertices())
    print(d)

