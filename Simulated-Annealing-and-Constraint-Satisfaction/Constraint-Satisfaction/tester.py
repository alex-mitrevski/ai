from csp import CSP
from variable import Variable

def value_consistent(variable_assignment, variable, value):
    """Checks all the problem constraints; passed as a callback to the
    constraint satisfaction search method.

    Keyword arguments:
    variable_assignment -- An object of type 'variables.ProblemVariables' that contains the current variable assignment.
    variable -- A key denoting the type of variable that is assigned.
    value -- A value for the variable of type 'variable'.

    """

    #we assign the new value to the variable and check if the assignment satisfies the problem constraints
    variable_assignment.variables[variable].values.append(value)

    if 'englishman' in variable_assignment.variables['people'].values and 'red' in variable_assignment.variables['houses'].values:
        if variable_assignment.variables['people'].values.index('englishman') != variable_assignment.variables['houses'].values.index('red'):
            return False

    if 'spaniard' in variable_assignment.variables['people'].values and 'dog' in variable_assignment.variables['animals'].values:
        if variable_assignment.variables['people'].values.index('spaniard') != variable_assignment.variables['animals'].values.index('dog'):
            return False

    if 'green' in variable_assignment.variables['houses'].values and 'coffee' in variable_assignment.variables['drinks'].values:
        if variable_assignment.variables['houses'].values.index('green') != variable_assignment.variables['drinks'].values.index('coffee'):
            return False

    if 'ukrainian' in variable_assignment.variables['people'].values and 'tea' in variable_assignment.variables['drinks'].values:
        if variable_assignment.variables['people'].values.index('ukrainian') != variable_assignment.variables['drinks'].values.index('tea'):
            return False

    if 'green' in variable_assignment.variables['houses'].values and 'ivory' in variable_assignment.variables['houses'].values:
        if variable_assignment.variables['houses'].values.index('green') != variable_assignment.variables['houses'].values.index('ivory') + 1:
            return False

    if 'old gold' in variable_assignment.variables['cigarettes'].values and 'snails' in variable_assignment.variables['animals'].values:
        if variable_assignment.variables['cigarettes'].values.index('old gold') != variable_assignment.variables['animals'].values.index('snails'):
            return False

    if 'yellow' in variable_assignment.variables['houses'].values and 'kools' in variable_assignment.variables['cigarettes'].values:
        if variable_assignment.variables['cigarettes'].values.index('kools') != variable_assignment.variables['houses'].values.index('yellow'):
            return False

    if 'milk' in variable_assignment.variables['drinks'].values:
        if variable_assignment.variables['drinks'].values.index('milk') != 2:
            return False

    if 'norwegian' in variable_assignment.variables['people'].values:
        if variable_assignment.variables['people'].values.index('norwegian') != 0:
            return False

    if 'chesterfields' in variable_assignment.variables['cigarettes'].values and 'fox' in variable_assignment.variables['animals'].values:
        chesterfields_index = variable_assignment.variables['cigarettes'].values.index('chesterfields')
        fox_index = variable_assignment.variables['animals'].values.index('fox')
        if chesterfields_index != fox_index + 1 and chesterfields_index != fox_index - 1:
            return False

    if 'kools' in variable_assignment.variables['cigarettes'].values and 'horse' in variable_assignment.variables['animals'].values:
        kools_index = variable_assignment.variables['cigarettes'].values.index('kools')
        horse_index = variable_assignment.variables['animals'].values.index('horse')
        if kools_index != horse_index + 1 and kools_index != horse_index - 1:
            return False

    if 'lucky strike' in variable_assignment.variables['cigarettes'].values and 'orange juice' in variable_assignment.variables['drinks'].values:
        if variable_assignment.variables['cigarettes'].values.index('lucky strike') != variable_assignment.variables['drinks'].values.index('orange juice'):
            return False

    if 'parliaments' in variable_assignment.variables['cigarettes'].values and 'japanese' in variable_assignment.variables['people'].values:
        if variable_assignment.variables['cigarettes'].values.index('parliaments') != variable_assignment.variables['people'].values.index('japanese'):
            return False

    if 'blue' in variable_assignment.variables['houses'].values:
        if variable_assignment.variables['houses'].values.index('blue') != 1:
            return False

    return True

#we define a list of problem variables and their domains
variables = [Variable('people', ['englishman', 'japanese', 'norwegian', 'ukrainian', 'spaniard']),
Variable('houses', ['red', 'green', 'blue', 'yellow', 'ivory']), Variable('animals', ['fox', 'dog', 'horse', 'zebra', 'snails']), Variable('cigarettes', ['old gold', 'kools', 'chesterfields', 'lucky strike', 'parliaments']), Variable('drinks', ['coffee', 'tea', 'milk', 'orange juice', 'water'])]

#we run the search
csp_search = CSP()
solution = csp_search.search(variables, value_consistent)

#we print the results in a nice way
print '1. ' + solution.variables['people'].values[0] + ' -- ' + solution.variables['houses'].values[0] + ' -- ' + solution.variables['animals'].values[0] + ' -- ' + solution.variables['drinks'].values[0] + ' -- ' + solution.variables['cigarettes'].values[0]

print '2. ' + solution.variables['people'].values[1] + ' -- ' + solution.variables['houses'].values[1] + ' -- ' + solution.variables['animals'].values[1] + ' -- ' + solution.variables['drinks'].values[1] + ' -- ' + solution.variables['cigarettes'].values[1]

print '3. ' + solution.variables['people'].values[2] + ' -- ' + solution.variables['houses'].values[2] + ' -- ' + solution.variables['animals'].values[2] + ' -- ' + solution.variables['drinks'].values[2] + ' -- ' + solution.variables['cigarettes'].values[2]

print '4. ' + solution.variables['people'].values[3] + ' -- ' + solution.variables['houses'].values[3] + ' -- ' + solution.variables['animals'].values[3] + ' -- ' + solution.variables['drinks'].values[3] + ' -- ' + solution.variables['cigarettes'].values[3]

print '5. ' + solution.variables['people'].values[4] + ' -- ' + solution.variables['houses'].values[4] + ' -- ' + solution.variables['animals'].values[4] + ' -- ' + solution.variables['drinks'].values[4] + ' -- ' + solution.variables['cigarettes'].values[4]

print
print  'The ' + solution.variables['people'].values[solution.variables['drinks'].values.index('water')] + ' drinks water'
print 'The ' + solution.variables['people'].values[solution.variables['animals'].values.index('zebra')] + ' owns the zebra'
