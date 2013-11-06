import coordinates
import math
import random

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
        self.children = dict()


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
        """Adds an undirected edge between the nodes with labels
        'parentNodeKey' and 'childNodeKey'.
        Returns 'True' if the edge is added successfully.
        If the edge already exists, does not add it to the graph and returns 'False'.

        Keyword arguments:
        parentNodeKey -- Label of the parent node.
        childNodeKey -- Label of the child node.

        """
        if childNodeKey not in self.nodes[parentNodeKey].children:
            cost = self._distance(parentNodeKey, childNodeKey)
            self.nodes[parentNodeKey].children[childNodeKey] = cost
            self.nodes[childNodeKey].children[parentNodeKey] = cost
            return True
        else:
            return False

    def number_of_nodes(self):
        return len(self.nodes.keys())

    def node_exists(self, nodeKey):
        """Returns 'True' if the node with with key 'nodeKey' exists in the graph and 'False' otherwise.

        nodeKey -- A node key (an integer).

        """
        if nodeKey in self.nodes:
            return True
        else:
            return False

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

    def minimum_spanning_tree_cost(self, node_keys):
        """Finds the cost of a minimum spanning tree for the nodes
        whose keys are given in 'node_keys'; uses Prim's algorithm
        for finding the mininum spanning tree.

        Keyword arguments:
        node_keys -- A list of node keys for which we want to find a minimum spanning tree, assuming that these keys are already contained in the graph.

        """
        source = random.randint(0, len(node_keys)-1)
        visited = [node_keys[source]]
        unvisited = list(set(node_keys) - set(visited))
        tree_cost = 0.

        while len(visited) != len(node_keys):
            distances = self._calculate_distances(visited, unvisited)
            minimum_distance_index = self._find_minimum_distance(distances)
            tree_cost += distances[minimum_distance_index][2]
            visited.append(distances[minimum_distance_index][1])
            unvisited = list(set(node_keys) - set(visited))

        return tree_cost

    def _calculate_distances(self, set_A, set_B):
        """Calculates distances between all nodes in 'set_A' and 'set_B'.
        Returns a 2D list; each list contains node labels and the distance
        between the nodes.

        Keyword arguments:
        set_A -- A list of node keys.
        set_B -- A list of node keys.

        """
        set_a_cardinality = len(set_A)
        set_b_cardinality = len(set_B)
        distances = []

        for i in xrange(set_a_cardinality):
            for j in xrange(set_b_cardinality):
                distance = self.nodes[set_A[i]].children[set_B[j]]
                distances.append([set_A[i], set_B[j], distance])

        return distances

    def _find_minimum_distance(self, distances):
        """Returns the index of the minimum distance in the list, assuming that 'distances'
        has the form returned by 'self._calculate_distances'.

        Keyword arguments:
        distances -- A 2D list; each list contains node labels and the distance between the nodes.

        """
        minimum_distance = distances[0][2]
        minimum_distance_index = 0
        number_of_distances = len(distances)

        for i in xrange(1, number_of_distances):
            if distances[i][2] < minimum_distance:
                minimum_distance = distances[i][2]
                minimum_distance_index = i

        return minimum_distance_index
