class AStarNode(object):
    """Defines a node used for A* search.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, nodeLabel=-1, coordinates=None, parent=-1, cost=-1, totalCost=-1):
        """Creates a new node used for A* search.

        Keyword arguments:
        nodeLabel -- A label (an integer) for the node.
        coordinates -- A 'Coordinates' object describing the x and y coordinates of the node.
        parent -- The parent node that generates the new node.
        cost -- The cost to reach the current node.
        totalCost -- The total cost to the goal, which is a sum of the cost to reach the current node and the estimated cost to reach the goal.

        """
        self.nodeLabel = nodeLabel
        self.coordinates = coordinates
        self.cost = cost
        self.totalCost = totalCost
        self.parent = parent
