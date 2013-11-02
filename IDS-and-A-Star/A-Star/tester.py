import aStar
import graph
import coordinates
import random
import math

numberOfStations = 3500
numberOfConnections = 15000
maxX = 1000.
maxY = 1000.
stationGraph = graph.Graph()

for i in xrange(numberOfStations):
    xCoordinate = random.uniform(1.,maxX)
    yCoordinate = random.uniform(1.,maxY)
    nodeCoordinate = coordinates.Coordinates(xCoordinate, yCoordinate)
    node = graph.GraphNode(i+1, nodeCoordinate)
    stationGraph.add_node(node)

for i in xrange(numberOfConnections):
    parent = random.randint(1, numberOfStations)
    while True:
        child = random.randint(1, numberOfStations)

        if child != parent:
            added = stationGraph.add_edge(parent, child)
            if added:
                break

while True:
    stationSpecificationIdentifier = '0'
    while stationSpecificationIdentifier != '1' and stationSpecificationIdentifier != '2':
        stationSpecificationIdentifier = raw_input('How would you like to specify the stations:\nPress 1 for station identifier\nPress 2 for coordinates\n')
        if stationSpecificationIdentifier != '1' and stationSpecificationIdentifier != '2':
            print 'Wrong input'

    if stationSpecificationIdentifier == '1':
        sourceNode = ''
        while not sourceNode.isdigit() or int(sourceNode) < 1 or int(sourceNode) > numberOfStations:
            sourceNode = raw_input('Enter the initial station (a number between 1 and ' + str(numberOfStations) + '): ')
            if not sourceNode.isdigit() or int(sourceNode) < 1 or int(sourceNode) > numberOfStations:
                print 'Wrong input'
        sourceNode = int(sourceNode)

        goalNode = ''
        while not goalNode.isdigit() or int(goalNode) < 1 or int(goalNode) > numberOfStations:
            goalNode = raw_input('Enter the destination (a number between 1 and ' + str(numberOfStations) + '): ')
            if not goalNode.isdigit() or int(goalNode) < 1 or int(goalNode) > numberOfStations:
                print 'Wrong input'
        goalNode = int(goalNode)
    else:
        correctCoordinates = False
        sourceNode = coordinates.Coordinates()
        while not correctCoordinates:
            correctCoordinates = True
            coordinateString = raw_input('Enter the x and y coordinates of the initial station as numbers between 1 and ' + str(maxX) + '/' + str(maxY) + '; separate the coordinates with an empty space\n')
            coordinatesStrings = coordinateString.split(' ')
            if len(coordinatesStrings) != 2:
                correctCoordinates = False
                print 'Wrong input'
                continue

            try:
                sourceNode.x = float(coordinatesStrings[0])
                sourceNode.y = float(coordinatesStrings[1])

                if sourceNode.x < 1 or sourceNode.x > maxX or sourceNode.y < 1 or sourceNode.y > maxY:
                    correctCoordinates = False
            except ValueError:
                correctCoordinates = False

            if not correctCoordinates:
                print 'Wrong input'

        correctCoordinates = False
        goalNode = coordinates.Coordinates()
        while not correctCoordinates:
            correctCoordinates = True
            coordinateString = raw_input('Enter the x and y coordinates of the goal station as numbers between 1 and ' + str(maxX) + '/' + str(maxY) + '; separate the coordinates with an empty space\n')
            coordinatesStrings = coordinateString.split(' ')
            if len(coordinatesStrings) != 2:
                correctCoordinates = False
                print 'Wrong input'
                continue

            try:
                goalNode.x = float(coordinatesStrings[0])
                goalNode.y = float(coordinatesStrings[1])

                if goalNode.x < 1 or goalNode.x > maxX or goalNode.y < 1 or goalNode.y > maxY:
                    correctCoordinates = False
            except ValueError:
                correctCoordinates = False

            if not correctCoordinates:
                print 'Wrong input'

    aStarLibrary = aStar.AStarLibrary(stationGraph)
    shortestPath = aStarLibrary.find_shortest_path(sourceNode, goalNode)

    if not isinstance(shortestPath, basestring):
        stationGraph.visualize_graph(shortestPath)

    print shortestPath

    tryAgain = '0'
    while tryAgain != '1' and tryAgain != '2':
        tryAgain = raw_input('Would you like to try again?\nType 1 for YES\nType 2 for NO\n')
        if tryAgain != '1' and tryAgain != '2':
            print 'Wrong input'

    if tryAgain == '2':
        break
