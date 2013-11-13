import variables

class CSP(object):
    """Defines a library for solving constraint satisfaction problems.

    Author -- Aleksandar Mitrevski

    """
    def search(self, problem_variables, value_consistent):
        """Looks for a solution to a constraints satisfaction problem.

        Keyword arguments:
        problem_variables -- A list of 'variable.Variable' objects.
        value_consistent -- A callback that checks the variable constraints. The callback is expected to accept three parameters: a 'variables.ProblemVariables' object, a variable key, and a new value for the variable with the given key.

        """
        print 'Running constraint satisfaction problem search...'
        return self._recursive_backtracking_search(variables.ProblemVariables(problem_variables, None), value_consistent)

    def _recursive_backtracking_search(self, variable_assignment, value_consistent):
        """Looks for a solution to a constraints satisfaction problem.

        Keyword arguments:
        variable_assignment -- A 'variables.ProblemVariables' object.
        value_consistent -- A callback that checks the variable constraints. The callback is expected to accept three parameters: a 'variables.ProblemVariables' object, a variable key, and a new value for the variable with the given key.

        """
        #if all the variables are assigned, we just return the current assignment
        if variable_assignment.all_variables_assigned():
            return variable_assignment

        #we pick an unassigned variable
        variable, allowed_values = variable_assignment.select_unassigned_variable()

        #for each of the allowed values for selected variable, we check whether the value satisfies
        #the problem constraints; if it does, we save the assignment and make a recursive call
        for _, value in enumerate(allowed_values):
            if value_consistent(variables.ProblemVariables(None, variable_assignment), variable, value):
                variable_assignment.variables[variable].values.append(value)
                result = self._recursive_backtracking_search(variables.ProblemVariables(None, variable_assignment), value_consistent)
                if isinstance(result, variables.ProblemVariables):
                    return result
                variable_assignment.variables[variable].values.remove(value)

        return False
