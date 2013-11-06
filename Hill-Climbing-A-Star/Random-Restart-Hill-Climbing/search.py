import random
import math
import matplotlib.pyplot as pyplot

class CitySearchLibrary(object):
    """Defines a search library for finding paths between cities.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, cities):
        """Initializes a library.

        Keyword arguments:
        cities -- A list of 'CityData' objects.

        """
        self.cities = cities
        self.number_of_cities = len(self.cities)

    def search(self, number_of_restarts, threshold):
        """Looks for a shortest cost cycle that connects all cities
        (i.e. looks for a solution to the traveling salesman problem)
        using a random-restart hill-climbing strategy. Returns:

        - A list of minimum costs found after each restart.
        - A list of descends after each restart.

        Keyword arguments:
        number_of_restarts -- Number of times we want to restart the hill-climbing algorithm.
        threshold -- Smallest difference between two descends that we want to reach.

        """

        print 'Running hill climbing with ' + str(number_of_restarts) + ' restarts'

        #list of the minimum costs found after each restart of the algorithm
        minimum_costs_found = []

        #A 2D list that stores the total cost after each descend
        #for each restart; used for visualization purposes
        costs_at_each_iteration = []

        #list of the number of descends at each restart
        number_of_descends = []

        for i in xrange(number_of_restarts+1):
            print 'Running hill climbing iteration ' + str(i+1) + '...'

            #we start with a random initial state
            current_state = self._get_initial_state()

            #we find the total cost of the initial configuration
            #because we will need to use it for comparing with the costs
            #of the neighbour states
            cost = self._calculate_cost(current_state)

            #we suppose that the initial cost is also the minimum cost
            minimum_cost = cost
            cost_at_each_descend = [minimum_cost]

            #we make sure that the condition in the while loop below is true
            best_cost_difference = threshold + 1.

            #used for counting the number of descends before the difference threshold is reached
            descends = 0

            #as long as the descends are optimistic, the algorithm looks for neighbour states
            #and chooses the one that offers the biggest cost improvement
            while best_cost_difference > threshold:
                #we generate neighbours of the current state
                neighbours = self._generate_neighbours(current_state)

                #we take the best neighbour among the generated ones, along with the cost improvement
                #that moving to this neighbour gives and the actual cost of this state
                best_neighbour_cost, best_cost_difference, best_neighbour = self._get_best_neighbour(neighbours, minimum_cost)

                #if the best neighbour offers a significant cost improvement,
                #we move update the variables that store the current state
                if best_cost_difference > threshold:
                    current_state = list(neighbours[best_neighbour])
                    minimum_cost = best_neighbour_cost
                    cost_at_each_descend.append(minimum_cost)
                    descends += 1

            minimum_costs_found.append(minimum_cost)
            number_of_descends.append(descends)
            costs_at_each_iteration.append(cost_at_each_descend)

        #we visualize the results of the algorithm after all restarts have been performed
        self.visualize_iterations(number_of_restarts, number_of_descends, costs_at_each_iteration)
        return minimum_costs_found, number_of_descends

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

    def _generate_neighbours(self, city_arrangement):
        """Generates neighbour states for the given city arrangement
        by choosing a random list position and swapping the element
        in that position with all the other elements.
        Returns a 2D list of all neighbour states, where each list
        represents a new city configuration.

        Keyword arguments:
        city_arrangement -- A list of city indices.

        """
        city_to_swap = random.randint(0, self.number_of_cities-1)

        neighbours = []
        for i in xrange(self.number_of_cities):
            if i == city_to_swap:
                continue

            if city_to_swap == 0:
                neighbour[len(neighbour)-1] = neighbour[i]

            neighbour = list(city_arrangement)
            temp = neighbour[i]
            neighbour[i] = neighbour[city_to_swap]
            neighbour[city_to_swap] = temp
            neighbours.append(neighbour)

        return neighbours

    def _get_best_neighbour(self, neighbours, current_cost):
        """Finds the neighbour configuration that offers the greatest cost improvement.
        Returns:

        - The cost of the best neighbour.
        - The difference between the cost of the current state and the cost of the best neighbour.
        - The best neighbour state (a list of city indices).

        Keyword arguments:
        neighbours -- A 2D list containing city configurations that are neighbours of the current state.
        current_cost -- The cost of the current state.

        """
        number_of_neighbours = len(neighbours)

        #we assume that the first neighbour state is the best state
        cost = self._calculate_cost(neighbours[0])
        best_cost_difference = current_cost - cost
        best_neighbour = 0

        costs = [cost]

        #we look for the least-cost neighbour state
        for neighbour in xrange(1, number_of_neighbours):
            cost = self._calculate_cost(neighbours[neighbour])
            costs.append(cost)
            cost_difference = current_cost - cost
            if cost_difference > best_cost_difference:
                best_cost_difference = cost_difference
                best_neighbour = neighbour

        return costs[best_neighbour], best_cost_difference, best_neighbour

    def visualize_iterations(self, number_of_restarts, number_of_descends, costs_at_each_iteration):
        """Visualizes the results of the algorithm. Plots one figure with subplots for
        each restart. If the number of restarts is less than 3, the subplots are organized in one row;
        otherwise, they are organized in multiple rows, such that each row contains five subplots.

        Keyword arguments:
        number_of_restarts -- The number of restarts of the hill-climbing algorithm.
        number_of_descends -- A list containing the number of descends at each restart.
        costs_at_each_iteration -- A 2D list containing costs at each descend and each restart of the algorithm.

        """
        number_of_rows = (number_of_restarts) / 3 + 1
        number_of_columns = min(3, number_of_restarts + 1)
        current_subplot = 1

        pyplot.figure(1)
        for i in xrange(number_of_restarts+1):
            descends = [x+1 for x in xrange(number_of_descends[i] + 1)]
            pyplot.subplot(number_of_rows, number_of_columns, current_subplot)
            pyplot.xlabel('Number of iterations')
            pyplot.ylabel('Total cost')
            pyplot.plot(descends, costs_at_each_iteration[i], 'b-')
            current_subplot += 1

        pyplot.show()
