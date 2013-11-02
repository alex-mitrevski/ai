from collections import deque

class SearchNode(object):
    """Defines a grid search node.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, nodeLabel=0, level=0):
        self.nodeLabel = nodeLabel
        self.level = level


class SearchLibrary(object):
    """Defines a grid search library.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, graph):
        self.graph = graph

    def _generate_neighbours(self, currentNode):
        """Returns a list of 'SearchNode' objects representing all neighbours of 'currentNode'.

        Keyword arguments:
        currentNode -- A 'SearchNode' object.

        """
        adjacentNodes = []

        for _,child in enumerate(self.graph.nodes[currentNode.nodeLabel].children):
            childLabel = child.connectedNode
            newNode = SearchNode(childLabel, currentNode.level+1)
            adjacentNodes.append(newNode)

        return adjacentNodes

    #<summary>Explores a grid of nodes using a depth-first search strategy.</summary>
    #<returns>A list of 'grid.Coordinates' objects that store the positions of the goal nodes found.</returns>
    def depthFirstSearch(self, start, goal):
        """Explores a graph using a depth-first search strategy.
        Finds the first path from the node with label 'start' to the node with label 'goal'.
        Returns 'True' if the path is found and 'False' otherwise.

        Keyword arguments:
        start -- A label (an integer) representing the start node.
        goal -- A label (an integer) representing the goal node.

        """
        startPosition = SearchNode(start,0)

        stack = [startPosition]
        goalPositionFound = False

        #as long as we have nodes to process, we take
        #the neighbours of the current node, append them to the stack,
        #and stop the search if the goal node is found
        while len(stack) > 0 and not goalPositionFound:
            currentNode = stack.pop()

            if currentNode.nodeLabel == goal:
                goalPositionFound = True
                continue

            neighbours = self._generate_neighbours(currentNode)
            numberOfNeighbours = len(neighbours)

            while len(neighbours) > 0:
                neighbour = neighbours.pop()
                stack.append(neighbour)

        return goalPositionFound

    def breadthFirstSearch(self, start, goal):
        """Explores a graph using a breadth-first search strategy.
        Finds the first path from the node with label 'start' to the node with label 'goal'.
        Returns 'True' if the path is found and 'False' otherwise.

        Keyword arguments:
        start -- A label (an integer) representing the start node.
        goal -- A label (an integer) representing the goal node.

        """
        startPosition = SearchNode(start,0)

        queue = deque([startPosition])
        goalPositionFound = False

        #as long as we have nodes to process, we take
        #the neighbours of the current node, append them to the queue,
        #and stop the search if the goal node is found
        while len(queue) > 0 and not goalPositionFound:
            currentNode = queue.popleft()

            if currentNode.nodeLabel == goal:
                goalPositionFound = True
                continue

            neighbours = self._generate_neighbours(currentNode)
            numberOfNeighbours = len(neighbours)

            while len(neighbours) > 0:
                neighbour = neighbours.pop()
                queue.append(neighbour)

        return goalPositionFound

    def iterativeDeepeningSearch(self, start, goal, maximumLevelToExplore):
        """Explores a graph using an iterative deepening depth-first search strategy.
        Finds the first path from the node with label 'start' to the node with label 'goal'.
        Returns 'True' if the path is found and 'False' otherwise.

        Keyword arguments:
        start -- A label (an integer) representing the start node.
        goal -- A label (an integer) representing the goal node.
        maximumLevelToExplore -- The maximum depth level that should be explored.

        """
        startPosition = SearchNode(start,0)
        goalPositionFound = False
        maxLevel = -1

        #as long as we have nodes to process, we take
        #the neighbours of the current node, append them to the stack,
        #and stop the search if the goal node is found
        while not goalPositionFound and maxLevel < maximumLevelToExplore:
            stack = [startPosition]
            maxLevel += 1

            while len(stack) > 0 and not goalPositionFound:
                currentNode = stack.pop()

                if currentNode.nodeLabel == goal:
                    goalPositionFound = True
                    continue

                #we get the neighbours of the current node only if
                #they don't exceed the maximum level that we want to explore
                if(currentNode.level < maxLevel):
                    neighbours = self._generate_neighbours(currentNode)
                    numberOfNeighbours = len(neighbours)

                    while len(neighbours) > 0:
                        neighbour = neighbours.pop()
                        stack.append(neighbour)

            if goalPositionFound:
                break

        return goalPositionFound
