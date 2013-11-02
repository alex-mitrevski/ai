import graph
import random
import search

numberOfStations = 3000
numberOfConnections = 500
stationGraph = graph.Graph()

print 'Generating graph...'
for i in xrange(numberOfStations):
    node = graph.GraphNode(i+1)
    stationGraph.add_node(node)

for parent in xrange(numberOfStations):
    for j in xrange(numberOfConnections):
        while True:
            child = random.randint(1, numberOfStations)

            if child != (parent+1):
                added = stationGraph.add_edge(parent+1, child)
                if added:
                    break

searchLibrary = search.SearchLibrary(stationGraph)

print '\nIterative deepening search running...'
goalFound = searchLibrary.iterativeDeepeningSearch(10,241,10)
if goalFound:
    print 'Solution found by iterative deepening search (IDS)'
else:
    print 'Solution not found by iterative deepening search (IDS)'

algorithmChoice = '0'
while algorithmChoice != '1' and algorithmChoice != '2':
    algorithmChoice = raw_input('\nWhich algorithm would you like to compare with IDS\nPress 1 for depth-first search\nPress 2 for breadth-first search\n')
    if algorithmChoice != '1' and algorithmChoice != '2':
        print 'Wrong input'

if algorithmChoice == '1':
    print '\nDepth first search running...'
    goalFound = searchLibrary.depthFirstSearch(10,241)
    if goalFound:
        print 'Solution found by depth-first search'
    else:
        print 'Solution not found by depth-first search'
else:
    print '\nBreadth first search running...'
    goalFound = searchLibrary.breadthFirstSearch(10,241)
    if goalFound:
        print 'Solution found by breadth-first search'
    else:
        print 'Solution not found by breadth-first search'
