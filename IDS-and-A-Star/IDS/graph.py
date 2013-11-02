import math
import matplotlib.pyplot as pyplot

class GraphNode(object):
    """Defines graph nodes.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, label=-1):
        """Creates a graph node.

        Keyword arguments:
        label -- A node label which is expected to be an integer (default -1)

        """
        self.label = label
        self.children = []


class GraphEdge(object):
    """Defines a graph edge.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, connectedNode):
        """Creates a directed graph edge.

        Keyword arguments:
        connectedNode -- Node label.

        """
        self.connectedNode = connectedNode


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
            parentToChildEdge = GraphEdge(childNodeKey)
            self.nodes[parentNodeKey].children.append(parentToChildEdge)
            return True
        else:
            return False
