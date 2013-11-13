import file_manager
import search

file_library = file_manager.CityFileLibrary('cities.txt')
city_data = file_library.get_city_data()
search_library = search.CitySearchLibrary(city_data)
distance_found, number_of_moves = search_library.search(3600.)

print 'Minimum distance found'
print distance_found

print ''
print 'Number of moves'
print number_of_moves
