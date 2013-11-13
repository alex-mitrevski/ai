import copy

class ProblemVariables(object):
    """Defines storage for variables of a CSP problem.

    Author -- Aleksandar Mitrevski

    """
    def __init__(self, problem_variables, variables_object):
        """Initializes an object for storing variables of a CSP problem.
        One of the inpur parameters should not be None.

        Keyword arguments:
        problem_variables -- A list of 'variable.Variable' objects; if the value is None, uses 'variables_object' for assigning the variables.
        variables_object -- A 'ProblemVariables' object that is copied; if the value is None, uses 'problem_variables' for assigning the variables.

        """
        self.variables = dict()
        if problem_variables != None:
            for _,variable in enumerate(problem_variables):
                self.variables[variable.key] = variable.copy()
        else:
            for key, variable in variables_object.variables.items():
                self.variables[key] = variable.copy()

    def all_variables_assigned(self):
        """Returns 'True' if all variables are assigned and 'False' otherwise."""
        for key, value in self.variables.items():
            if len(value.values) != value.number_of_allowed_values:
                return False
        return True

    def select_unassigned_variable(self):
        """Finds the first variable that is still not assigned.
        Returns the variable key and a list of values that have not already been assigned to it."""
        for key, value in self.variables.items():
            if len(value.values) != value.number_of_allowed_values:
                allowed_values = set(value.allowed_values) - set(value.values)
                return key, list(allowed_values)
