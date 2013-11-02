import search

#we define known constants about the world maps
startMarker = 's'
dirtMarker = '*'
obstacleMarkers = ['=', '|']

#we give the user an opportunity to make choose the map,
#the algorithm, and whether the search should be visualized or not
while True:
    #'fileIdentifier' should be set to '1', '2', or '3', denoting map 1, 2, or 3 respectively
    fileIdentifier = '0'
    while fileIdentifier != '1' and fileIdentifier != '2' and fileIdentifier != '3':
        fileIdentifier = raw_input('Select the map file\nType 1 for map 1\nType 2 for map 2\nType 3 for map 3\n')
        if fileIdentifier != '1' and fileIdentifier != '2' and fileIdentifier != '3':
            print 'Wrong input'

    #if 'algorithmIdentifier' is '1', we run depth-first search and if it is '2', we run breadth-first search
    algorithmIdentifier = '0'
    while algorithmIdentifier != '1' and algorithmIdentifier != '2':
        algorithmIdentifier = raw_input('Which search algorithm would you like to use?\nType 1 for Depth-first search\nType 2 for Breadth-first search\n')
        if algorithmIdentifier != '1' and algorithmIdentifier != '2':
            print 'Wrong input'

    #if 'visualizeFlag' is '1', we visualize the search; if it is '2', we don't
    visualizeFlag = '0'
    while visualizeFlag != '1' and visualizeFlag != '2':
        visualizeFlag = raw_input('Would you like to visualize the search?\nType 1 for YES\nType 2 for NO\n')
        if visualizeFlag != '1' and visualizeFlag != '2':
            print 'Wrong input'

    #we load the map and get rid of newline characters
    worldFile = open('maps/map' + fileIdentifier + '.txt')
    world = worldFile.readlines()
    world = [line.strip() for line in world]
    worldFile.close()

    #we create a new instance of the search library with the new parameters
    searchLibrary = search.SearchLibrary(world, startMarker, obstacleMarkers, dirtMarker, visualizeFlag == '1')

    if algorithmIdentifier == '1':
        dirtPositions = searchLibrary.depthFirstSearch()
    else:
        dirtPositions = searchLibrary.breadthFirstSearch()

    #we print the number of goals found after the search is over,
    #regardless of whether the search was visualized or not
    print 'Found reachable dirt locations: ' + str(len(dirtPositions))

    #we give the user a chance to continue experimenting with the program
    tryAgain = '0'
    while tryAgain != '1' and tryAgain != '2':
        tryAgain = raw_input('Would you like to try again?\nType 1 for YES\nType 2 for NO\n')
        if tryAgain != '1' and tryAgain != '2':
            print 'Wrong input'

    if tryAgain == '2':
        break
