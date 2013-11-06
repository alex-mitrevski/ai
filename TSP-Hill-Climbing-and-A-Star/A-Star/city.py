class CityData(object):
    """Defines objects for storing city data.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, name, x, y):
        """Initializes a city data object.

        Keyword arguments:
        name -- Name of a city.
        x -- x coordinate of a node.
        y -- y coordinate of a node.

        """
        self.name = name
        self.x = x
        self.y = y
