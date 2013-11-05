import file_manager
import search

file_library = file_manager.CityFileLibrary('cities.txt')
city_data = file_library.get_city_data()
search_library = search.CitySearchLibrary(city_data)
distances_found, number_of_descends = search_library.search(0, 2500)

print 'Minumum distances found at each iteration'
print distances_found

print ''
print 'Number of descends at each iteration'
print number_of_descends
