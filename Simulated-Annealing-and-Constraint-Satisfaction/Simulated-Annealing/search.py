import random
import math
import matplotlib.pyplot as pyplot
import time

class CitySearchLibrary(object):
    """Defines a search library for finding minimum cost paths between cities.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, cities):
        """Initializes a library.

        Keyword arguments:
        cities -- A list of 'CityData' objects.

        """
        self.cities = cities
        self.number_of_cities = len(self.cities)

    def search(self, maximum_runtime_allowed):
        """Looks for a shortest cost cycle that connects all cities
        (i.e. looks for a solution to the traveling salesman problem)
        using simulated annealing. Returns:

        - The minimum cost found.
        - The number of moves (ascends and descends) made by the algorithm.

        Keyword arguments:
        maximum_runtime_allowed -- Maximum time (in seconds) allowed for the search.

        """

        print 'Running simulated annealing...'

        #we start with a random initial state
        current_state = self._get_initial_state()

        #we find the total cost of the initial configuration
        #because we will need to use it for comparing with the costs
        #of the neighbour states
        cost = self._calculate_cost(current_state)

        current_cost = cost

        #used for visualization purposes
        cost_at_each_move = [current_cost]

        #used for counting the number of moves made by the algorithm
        number_of_moves = 0

        start_time = time.clock()
        time_elapsed = 0.

        #as long as the descends are optimistic, the algorithm looks for neighbour states
        #and chooses the one that offers the biggest cost improvement
        while time_elapsed < maximum_runtime_allowed:
            temperature = self._schedule(number_of_moves)
            if temperature < 1e-200:
                break

            #we generate a random neighbour of the current state
            neighbour = self._generate_neighbour(current_state)
            neighbour_cost = self._calculate_cost(neighbour)

            delta_cost = neighbour_cost - current_cost

            #if the neighbour improves the cost, we definitely make a move to it
            if delta_cost < 0:
                current_state = list(neighbour)
                current_cost = neighbour_cost
            #if the neighbour doesn't offer an improvement, we only select it with a certain probability
            else:
                change_state = self._change_state(delta_cost, temperature)
                if change_state:
                    current_state = list(neighbour)
                    current_cost = neighbour_cost

            cost_at_each_move.append(current_cost)
            number_of_moves += 1
            time_elapsed = time.clock() - start_time

        #we visualize the results of the algorithm
        self.visualize_iterations(number_of_moves, cost_at_each_move)
        return current_cost, number_of_moves

    def _get_initial_state(self):
        """Generates a random city configuration that contains each city
        once. Assumes that the cities form a complete graph. Returns a list 
        of indices corresponding to cities in 'self.cities'.

        """
        indices = [i for i in xrange(self.number_of_cities)]
        city_arrangement = []

        for i in xrange(self.number_of_cities):
            city_index = random.randint(0, len(indices)-1)
            city_arrangement.append(indices[city_index])
            del indices[city_index]

        city_arrangement.append(city_arrangement[0])
        return city_arrangement

    def _calculate_cost(self, city_arrangement):
        """Calculates costs between all cities in a given city configuration,
        given the longitude and latitude coordinates of the cities.
        Returns the total cost between the cities.

        Keyword arguments:
        city_arrangement -- A list of city indices.

        """
        total_cost = 0.
        number_of_cities = len(self.cities)

        #we calculate the distance between two consecutive
        #cities in the list; uses the Haversine formula for calculating distance
        #(source http://www.movable-type.co.uk/scripts/latlong.html)
        for i in xrange(number_of_cities):
            current_city = self.cities[city_arrangement[i]]
            neighbour = self.cities[city_arrangement[i+1]]
            radius_of_earth = 6371.

            longitude_distance = (current_city.longitude - neighbour.longitude) * math.pi / 180.
            latitude_distance = (current_city.latitude - neighbour.latitude) * math.pi / 180.
            current_city_latitude_radians = current_city.latitude * math.pi / 180.0
            neighbour_latitude_radians = neighbour.latitude * math.pi / 180.0

            a = math.sin(latitude_distance / 2.)**2 + math.sin(longitude_distance / 2.)**2 * math.cos(current_city_latitude_radians) * math.cos(neighbour_latitude_radians)
            c = 2. * math.atan2(math.sqrt(a), math.sqrt(1.-a))
            distance = radius_of_earth * c
            total_cost += distance

        return total_cost

    def _schedule(self, iteration_counter):
        """Returns temperature as a function of 'iteration_counter'.

        Keyword arguments:
        iteration_counter -- Iteration counter of the simulated annealing algorithm.

        """
        temperature = 1e10 * 0.999**iteration_counter
        return temperature

    def _generate_neighbour(self, city_arrangement):
        """Generates neighbour states for the given city arrangement
        by choosing a random list position and swapping the element
        in that position with all the other elements.
        Once the neighbours have been generated, randomly picks one neighbour and returns it.

        Keyword arguments:
        city_arrangement -- A list of city indices.

        """
        city_to_swap = random.randint(0, self.number_of_cities-1)

        neighbours = []
        for i in xrange(self.number_of_cities):
            if i == city_to_swap:
                continue

            neighbour = list(city_arrangement)
            temp = neighbour[i]
            neighbour[i] = neighbour[city_to_swap]
            neighbour[city_to_swap] = temp

            if city_to_swap == 0:
                neighbour[len(neighbour)-1] = neighbour[i]

            neighbours.append(neighbour)

        neighbour_index = random.randint(0, len(neighbours)-1)
        return neighbours[neighbour_index]

    def _change_state(self, delta_cost, temperature):
        """Returns 'True' if we want to accept the state change and 'False' otherwise.
        The acceptance probability is exp(-delta_cost/temperature).

        Keyword arguments:
        delta_cost -- Difference between the cost of a neighbour state and the cost of the current state.
        temperature -- A temperature that determines the acceptance probability.

        """
        probability_of_changing = math.exp(-delta_cost/temperature)
        random_number = random.random()
        if random_number < probability_of_changing:
            return True
        return False

    def visualize_iterations(self, number_of_moves, cost_at_each_move):
        """Visualizes the results of the simulated annealing algorithm.

        Keyword arguments:
        number_of_moves -- The number of moves in the simulated annealing algorithm.
        cost_at_each_move -- A list containing costs at each move of the algorithm.

        """
        moves = [x+1 for x in xrange(number_of_moves + 1)]
        pyplot.xlabel('Number of moves')
        pyplot.ylabel('Total cost')
        pyplot.plot(moves, cost_at_each_move, 'b-')

        pyplot.show()
