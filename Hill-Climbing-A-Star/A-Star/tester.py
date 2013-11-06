import aStar
import file_manager
import city
import graph
import coordinates
import math

file_library = file_manager.CityFileLibrary('cities.txt')
city_data = file_library.get_city_data()
number_of_cities = len(city_data)

city_graph = graph.Graph()
for i in xrange(number_of_cities):
    node_coordinates = coordinates.Coordinates(city_data[i].x, city_data[i].y)
    node = graph.GraphNode(i, node_coordinates)
    city_graph.add_node(node)

for parent in xrange(number_of_cities-1):
    for child in xrange(number_of_cities):
        city_graph.add_edge(parent, child)

aStarLibrary = aStar.AStarLibrary(city_graph)
shortestPath, cost = aStarLibrary.find_shortest_path()

print 'Shortest cycle'
print shortestPath
print ''

print 'Cycle cost'
print cost
