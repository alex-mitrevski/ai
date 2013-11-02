import coordinates
import math
import matplotlib.pyplot as pyplot

class GraphNode(object):
    """Defines graph nodes.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, label=-1, coordinates=None):
        """Creates a graph node.

        Keyword arguments:
        label -- A node label which is expected to be an integer (default -1)
        coordinates -- A 'Coordinates' object defining the x/y coordinates of the node (default None)

        """
        self.label = label
        self.coordinates = coordinates
        self.children = []


class GraphEdge(object):
    """Defines a graph edge.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, connectedNode, cost):
        """Creates a directed graph edge.

        Keyword arguments:
        connectedNode -- Label of the children node.
        cost -- Cost of the edge, which is calculated as a straight-line distance between the nodes.

        """
        self.connectedNode = connectedNode
        self.cost = cost


class Graph(object):
    """Defines a graph data structure.

    Author: Aleksandar Mitrevski

    """
    def __init__(self):
        """Creates a graph."""
        self.nodes = dict()

    def add_node(self, node):
        """Adds a node to the graph.

        Keyword arguments:
        node -- A 'GraphNode' object.
        """
        self.nodes[node.label] = node

    def add_edge(self, parentNodeKey, childNodeKey):
        """Adds a node between the nodes with labels
        'parentNodeKey' and 'childNodeKey'.
        Returns 'True' if the edge is added successfully.
        If the edge already exists, does not add it to the graph and returns 'False'.

        Keyword arguments:
        parentNodeKey -- Label of the parent node.
        childNodeKey -- Label of the child node.

        """
        if childNodeKey not in self.nodes[parentNodeKey].children:
            cost = self._distance(parentNodeKey, childNodeKey)
            parentToChildEdge = GraphEdge(childNodeKey, cost)
            self.nodes[parentNodeKey].children.append(parentToChildEdge)
            return True
        else:
            return False

    def node_exists(self, nodeKey):
        """Returns 'True' if the node with with key 'nodeKey' exists in the graph and 'False' otherwise.

        nodeKey -- A node key (an integer).

        """
        if nodeKey in self.nodes:
            return True
        else:
            return False

    def visualize_graph(self, shortestPathNodes):
        """Visualizes the graph after finding a shortest path between two nodes.

        Keyword arguments:
        shortestPathNodes -- A list of labels of nodes that belong to the shortest path between two nodes.

        """
        pyplot.ion()
        for key, value in self.nodes.items():
            pyplot.plot(value.coordinates.x, value.coordinates.y, 'ro')

        startCoordinates = self.nodes[shortestPathNodes[0]].coordinates
        goalCoordinates = self.nodes[shortestPathNodes[len(shortestPathNodes)-1]].coordinates

        pyplot.plot(startCoordinates.x, startCoordinates.y, 'go')
        pyplot.plot(goalCoordinates.x, goalCoordinates.y, 'yo')

        for i in xrange(len(shortestPathNodes) - 1):
            coord1 = self.nodes[shortestPathNodes[i]].coordinates
            coord2 = self.nodes[shortestPathNodes[i+1]].coordinates

            pyplot.plot([coord1.x, coord2.x], [coord1.y, coord2.y], 'b-')
            
        pyplot.show()

    def _distance(self, node1, node2):
        """Returns the straight-line distance between two nodes.

        Keyword arguments:
        node1 -- Label of a node in the graph (an integer).
        node2 -- Label of another node in the graph (an integer).

        """
        node1Coordinates = self.nodes[node1].coordinates
        node2Coordinates = self.nodes[node2].coordinates
        distance = math.sqrt((node1Coordinates.x - node2Coordinates.x)**2 + (node1Coordinates.y - node2Coordinates.y)**2)
        return distance
