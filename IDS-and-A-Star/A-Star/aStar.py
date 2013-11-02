import graph
import heap
import aStarNode
import coordinates
import math

class AStarLibrary(object):
    """Defines a library for finding shortest paths using A*.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, nodeGraph):
        """Creates a new A* search library.

        Keyword arguments:
        graph -- A 'Graph' object.

        """
        self.nodeGraph = nodeGraph

    def find_shortest_path(self, source, goal):
        """Finds a shortest path between 'source' and 'goal'.

        Keyword arguments:
        source -- Either a label of a node in the graph or a 'Coordinates' object representing the coordinates of the initial position.
        goal -- Either a label of a node in the graph or a 'Coordinates' object representing the coordinates of the goal position.

        """
        stationsExist = True
        if not isinstance(source, coordinates.Coordinates) and not self.nodeGraph.node_exists(source):
            stationsExist = False

        if not isinstance(goal, coordinates.Coordinates) and not self.nodeGraph.node_exists(goal):
            stationsExist = False

        if not stationsExist:
            return 'At least one of the specified stations does not exist'

        if isinstance(source, coordinates.Coordinates):
            source = self._find_closest_neighbour(source)

        if isinstance(goal, coordinates.Coordinates):
            goal = self._find_closest_neighbour(goal)

        openList = heap.MinHeap()
        closedList = []

        sourceNode = aStarNode.AStarNode(source, self.nodeGraph.nodes[source].coordinates, -1, 0, 0)
        openList.insert(sourceNode)

        pathFound = False
        while not openList.empty() and not pathFound:
            currentNode = openList.extract_min()
            closedList.append(currentNode)

            if currentNode.nodeLabel == goal:
                pathFound = True
                continue

            adjacent = self._get_adjacent_nodes(currentNode, goal)
            for _,node in enumerate(adjacent):
                nodePosition = openList.get_index(node)
                if nodePosition != -1:
                    if openList.nodes[nodePosition].totalCost > node.totalCost:
                        openList.nodes[nodePosition] = node
                        openList.bubble_up(nodePosition)
                else:
                    nodeClosed = False
                    for _,closedNode in enumerate(closedList):
                        if node.nodeLabel == closedNode.nodeLabel:
                            nodeClosed = True
                            break

                    if not nodeClosed:
                        openList.insert(node)

        if currentNode.nodeLabel != goal:
            return 'A path between the stations was not found'
        else:
            shortestPath = []
            shortestPath.append(closedList[len(closedList)-1].nodeLabel)
            parentNode = closedList[len(closedList)-1].parent

            if parentNode != -1:
                while True:
                    shortestPath.append(parentNode)
                    for _,node in enumerate(closedList):
                        if node.nodeLabel == parentNode:
                            parentNode = node.parent
                            break

                    if parentNode == -1:
                        break

            return shortestPath[::-1]

    def _get_adjacent_nodes(self, currentNode, goal):
        """Returns a list of 'AStarNode' objects representing the nodes adjacent to 'currentNode'.

        Keyword arguments:
        currentNode -- An 'AStarNode' object representing a node currently processed by the search algorithm.
        goal -- A node label (an integer) representing the goal node.

        """
        adjacentNodes = []

        for _,child in enumerate(self.nodeGraph.nodes[currentNode.nodeLabel].children):
            childLabel = child.connectedNode
            childCoordinates = self.nodeGraph.nodes[childLabel].coordinates
            cost = currentNode.cost + child.cost
            heuristic = self._calculate_heuristic(childLabel, goal)
            totalCost = cost + heuristic

            newNode = aStarNode.AStarNode(childLabel, childCoordinates, currentNode.nodeLabel, cost, totalCost)
            adjacentNodes.append(newNode)

        return adjacentNodes

    def _calculate_heuristic(self, node, goal):
        """Calculates a value for the heuristic between 'node' and 'goal'.

        Keyword arguments:
        node -- A node label (an integer) representing a node in the graph.
        goal -- A node label (an integer) representing the goal node.

        """
        nodeCoordinates = self.nodeGraph.nodes[node].coordinates
        goalCoordinates = self.nodeGraph.nodes[goal].coordinates

        distance = math.sqrt((nodeCoordinates.x - goalCoordinates.x)**2 + (nodeCoordinates.y - goalCoordinates.y)**2)
        return distance

    def _find_closest_neighbour(self, nodeCoordinates):
        """Returns the key of a node (an integer) representing the graph node
        whose coordinates are closest (using a straight-line distance) to 'nodeCoordinates'.

        Keyword arguments:
        nodeCoordinates -- A 'Coordinates' object representing the coordinates of a point.

        """
        minKey = -1
        minDistance = 10000000000000000.0
        for key, value in self.nodeGraph.nodes.items():
            distance = math.sqrt((value.coordinates.x - nodeCoordinates.x)**2 + (value.coordinates.y - nodeCoordinates.y)**2)
            if distance < minDistance:
                minDistance = distance
                minKey = key

        return minKey
