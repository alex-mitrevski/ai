Traveling Salesman Problem using Simulated Annealing
====================================================

Uses simulated annealing for finding an optimal solution to the traveling salesman problem. The temperature function used is decreasing very slowly - f(i) = 1e10 * 0.999*i.

"Cities.txt" contains test data for the problem. Runs for a predefined amount of time (the time can be adjusted in tester.py), but stops earlier if the temperature goes below 1e-200 (though it is highly unlikely that the temperature will ever reach such low values).

Code written in Python 2.7.4.
