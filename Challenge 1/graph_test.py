#!python

from graph2 import Graph
import unittest

class GraphTest(unittest.TestCase):
    
    def test_init(self):
        g = Graph()
        assert isinstance(g, Graph)

    def test_size(self):
        g = Graph()

        assert g.size == 0
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_vertex('D')
        assert g.size == 4
        g.add_edge('A', 'B')
        g.add_edge('C', 'D')
        g.add_edge('E', 'F')
        g.add_edge('G', 'H')
        assert g.size == 8

        with self.assertRaises(KeyError):
            g.add_vertex('A')
        assert g.size == 8
        
    def test_add_vertex(self):
        g = Graph()

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_vertex('D')

        assert g.has_vertex('A') is True
        assert g.has_vertex('B') is True
        assert g.has_vertex('C') is True
        assert g.has_vertex('D') is True

        assert g.has_vertex('E') is False
        assert g.has_vertex('F') is False
        assert g.has_vertex('G') is False
        assert g.has_vertex('H') is False
        
        g.add_edge('A', 'B')
        g.add_edge('C', 'D')
        
        self.assertCountEqual(g.get_neighbors('A'), ['B'])
        self.assertCountEqual(g.get_neighbors('B'), [])
        self.assertCountEqual(g.get_neighbors('C'), ['D'])
        self.assertCountEqual(g.get_neighbors('D'), [])

        g.add_edge('A', 'F')
        g.add_edge('B', 'E')

        self.assertCountEqual(g.get_neighbors('A'), ['B','F'])
        self.assertCountEqual(g.get_neighbors('B'), ['E'])


    def test_has_vertex(self):
        g = Graph()

        assert g.has_vertex('A') is False
        g.add_vertex('B')
        assert g.has_vertex('B') is True
        g.add_edge('C', 'D')
        assert g.has_vertex('C') is True
        assert g.has_vertex('D') is True

    def test_get_vertices(self):
        g = Graph()

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_vertex('D')

        self.assertCountEqual(g.get_vertices(), ['A', 'B', 'C', 'D'])

    def test_get_neighbors(self):
        g = Graph()

        g.add_edge('A', 'B')
        g.add_edge('C', 'D')
        g.add_edge('E', 'F')
        g.add_edge('G', 'H')

        self.assertCountEqual(g.get_neighbors('A'), ['B'])
        self.assertCountEqual(g.get_neighbors('B'), [])
        self.assertCountEqual(g.get_neighbors('C'), ['D'])
        self.assertCountEqual(g.get_neighbors('D'), [])

        with self.assertRaises(KeyError):
            g.get_neighbors('Z')

    def test_get_edge_list(self):
        g = Graph(weighted=True, directed=False)

        g.add_weighted_edge('A', 'B', 5)
        g.add_weighted_edge('C', 'D', 3)
        g.add_weighted_edge('E', 'F', 2)
        g.add_weighted_edge('G', 'H', 1)

        self.assertCountEqual(g.get_edge_list(), [('A', 'B', 5), ('C', 'D', 3), ('E', 'F', 2), ('G', 'H', 1)])
        
    


    


if __name__ == '__main__':
    unittest.main()