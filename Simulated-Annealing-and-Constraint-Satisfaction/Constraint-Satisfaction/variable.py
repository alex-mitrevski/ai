class Variable(object):
    """Defines variables that can be used for constraint satisfaction problems.

    Author -- Aleksandar Mitrevski

    """
    def __init__(self, key, allowed_values):
        """Initializes a variable.

        Keyword arguments:
        key -- A variable key.
        allowed_values -- A list containing the variable domain (assuming the domain is discrete).

        """
        self.key = key
        self.allowed_values = list(allowed_values)
        self.values = []
        self.number_of_allowed_values = len(allowed_values)

    def copy(self):
        """Returns a new copy of 'self'."""
        variable_copy = Variable(self.key, self.allowed_values)
        variable_copy.values = list(self.values)
        return variable_copy
