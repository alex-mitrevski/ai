import grid
from collections import deque
import matplotlib.pyplot as pyplot
import numpy

#<summary>Defines a grid search library.</summary>
#<author>Aleksandar Mitrevski</author>
class SearchLibrary:
    #<summary>Creates a new search library object.</summary>
    #<param name='world'>A two dimensional list of characters that describes the world.</param>
    #<param name='startMarker'>A character defining the starting search position in the map.</param>
    #<param name='obstacleMarkers'>A list of characters defining the obstacle markers in the world.</param>
    #<param name='goalMarker'>A character defining a goal position.</param>
    #<param name='visualize'>If set to 'True', the search algorithm will be visualized.</param>
    def __init__(self, world, startMarker, obstacleMarkers, goalMarker, visualize = True):
        self.worldConfiguration = world
        self.startMarker = startMarker
        self.obstacleMarkers = obstacleMarkers
        self.goalMarker = goalMarker
        self.visualize = visualize

        #used when searching for neighbours
        #in order to avoid generating neighbours that are
        #out of the world boundaries
        self.numberOfRows = len(world)
        self.numberOfColumns = len(world[0])

        #used for visualization purposes, in order to
        #avoid recomputing the obstacle positions
        #each time the figure will be refreshed
        self.obstacles = self._findObstaclePositions()

    #<summary>Finds the coordinates of the obstacle positions in the world.</summary>
    #<returns>A numpy array of [row, column] coordinates.</returns>
    def _findObstaclePositions(self):
        obstacles = []
	for i in range(self.numberOfRows):
            for j in range(self.numberOfColumns):
                if self.worldConfiguration[i][j] in self.obstacleMarkers:
                    obstacles.append([j, i])
        return numpy.array(obstacles) 

    #<summary>Looks for the position where the search should start.</summary>
    #<returns>A 'grid.Coordinates' object that stores the position of the starting search position.</returns>
    def _findStartPosition(self):
        startFound = False
        startPosition = grid.Coordinates()

        for i in range(self.numberOfRows):
            for j in range(self.numberOfColumns):
                if self.worldConfiguration[i][j] == self.startMarker:
                    startPosition.row = i
                    startPosition.column = j
                    startFound = True
                    break
            if startFound:
                break

        return startPosition

    #<summary>Finds all the neighbours of a node; takes into account
    #         the constraint that diagonal movements are not allowed.
    #</summary>
    #<param name='currentNode'>The node whose neighbours we want to find.</param>
    #<returns>A list of 'grid.Coordinates' objects.</returns>
    def _generateNeighbours(self, currentNode):
        row = currentNode.getRow()
        column = currentNode.getColumn()
        neighbours = []

        #we take the node down if it is not an obstacle and doesn't go out of bounds
        if row + 1 < self.numberOfRows and self.worldConfiguration[row+1][column] not in self.obstacleMarkers:
            newCoordinates = grid.Coordinates(row + 1, column)
            neighbours.append(newCoordinates)

        #we take the node up if it is not an obstacle and doesn't go out of bounds
        if row - 1 > -1 and self.worldConfiguration[row-1][column] not in self.obstacleMarkers:
            newCoordinates = grid.Coordinates(row - 1, column)
            neighbours.append(newCoordinates)

        #we take the node to the right if it is not an obstacle and doesn't go out of bounds
        if column + 1 < self.numberOfColumns and self.worldConfiguration[row][column+1] not in self.obstacleMarkers:
            newCoordinates = grid.Coordinates(row, column + 1)
            neighbours.append(newCoordinates)

        #we take the node to the left if it is not an obstacle and doesn't go out of bounds
        if column - 1 > -1 and self.worldConfiguration[row][column-1] not in self.obstacleMarkers:
            newCoordinates = grid.Coordinates(row, column - 1)
            neighbours.append(newCoordinates)

        return neighbours

    #<summary>Checks if a node has already been visited by a search algorithm.</summary>
    #<param name='node'>The node that we want to check.</param>
    #<param name='visitedNodes'>A list of visited nodes.</param>
    #<returns>'True' if 'node' has already been visited and 'False' otherwise.</returns>
    def _alreadyVisited(self, node, visitedNodes):
        numberOfVisitedPositions = len(visitedNodes)
        alreadyVisited = False

        for i in range(numberOfVisitedPositions):
            if visitedNodes[i] == node:
                alreadyVisited = True
                break

        return alreadyVisited

    #<summary>Visualizes the search by plotting the currently processed nodes, 
    #the obstacles, and the explore dgoal nodes.
    #</summary>
    #<param name='currentNode'>The node currently processed by the search algorithm.</param>
    #<param name='goalPositions'>A list of explored goal nodes.</param>
    def _visualizeGrid(self, currentNode, goalPositions):
        pyplot.figure(1)

        #we make the figure interactive because we want to avoid
        #blocking the flow of the rest of the code
        pyplot.ion()

        #we clear the figure before plotting
	pyplot.clf()

        #we plot the obstacles
	pyplot.plot(self.obstacles[..., 0], self.obstacles[..., 1], 'ko', label='obstacles')

        #we convert the goal positions to a numpy array (more convenient for plotting)
        goalPositionsList = []
	for i in range(len(goalPositions)):
            goalPositionsList.append([goalPositions[i].getColumn(), goalPositions[i].getRow()])
        goalPositionsArray = numpy.array(goalPositionsList)

        #if we have goal nodes to plot, we do that
        if len(goalPositionsList) > 0:
            pyplot.plot(goalPositionsArray[..., 0], goalPositionsArray[..., 1], 'b*', label='goals')

        #we plot the current node
        pyplot.plot(currentNode.getColumn(), currentNode.getRow(), 'ro', label='current position')

        #we set a legend above the plot
	pyplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)

        #we set the range of the axes
        pyplot.axis([0, self.numberOfColumns, 0, self.numberOfRows])

        #we invert the y axis because we want it to grow from top to bottom
        pyplot.gca().invert_yaxis()

        #we finally draw the figure
        pyplot.draw()

    #<summary>Explores a grid of nodes using a depth-first search strategy.</summary>
    #<returns>A list of 'grid.Coordinates' objects that store the positions of the goal nodes found.</returns>
    def depthFirstSearch(self):
        startPosition = self._findStartPosition()

        stack = [startPosition]
        visitedNodes = [startPosition]
        goalPositions = []

        #as long as we have nodes to process, we take
        #the neighbours of the current node, append them to the stack,
        #and add the current node to the goal list if it is a goal node
        while len(stack) > 0:
            currentNode = stack.pop()

            if self.visualize:
                self._visualizeGrid(currentNode, goalPositions)

            if self.worldConfiguration[currentNode.getRow()][currentNode.getColumn()] == self.goalMarker:
                goalPositions.append(currentNode)

            neighbours = self._generateNeighbours(currentNode)
            numberOfNeighbours = len(neighbours)

            #we only add the nodes to the stack if they have not been visited already
            while len(neighbours) > 0:
                neighbour = neighbours.pop()
                if not self._alreadyVisited(neighbour, visitedNodes):
                    stack.append(neighbour)
                    visitedNodes.append(neighbour)

        return goalPositions

    #<summary>Explores a grid of nodes using a breadth-first search strategy.</summary>
    #<returns>A list of 'grid.Coordinates' objects that store the positions of the goal nodes found.</returns>
    def breadthFirstSearch(self):
        startPosition = self._findStartPosition()

        queue = deque([startPosition])
        visitedNodes = [startPosition]
        goalPositions = []

        #as long as we have nodes to process, we take
        #the neighbours of the current node, append them to the queue,
        #and add the current node to the goal list if it is a goal node
        while len(queue) > 0:
            currentNode = queue.popleft()

            if self.visualize:
                self._visualizeGrid(currentNode, goalPositions)

            if self.worldConfiguration[currentNode.getRow()][currentNode.getColumn()] == self.goalMarker:
                goalPositions.append(currentNode)

            neighbours = self._generateNeighbours(currentNode)
            numberOfNeighbours = len(neighbours)

            #we only add the nodes to the queue if they have not been visited already
            while len(neighbours) > 0:
                neighbour = neighbours.pop()
                if not self._alreadyVisited(neighbour, visitedNodes):
                    queue.append(neighbour)
                    visitedNodes.append(neighbour)

        return goalPositions
