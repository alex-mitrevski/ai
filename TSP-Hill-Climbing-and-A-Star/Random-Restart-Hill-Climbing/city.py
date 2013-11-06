class CityData(object):
    """Defines objects for storing city data.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, name, longitude, latitude):
        """Initializes a city data object.

        Keyword arguments:
        name -- Name of a city.
        longitude -- City longitude.
        latitude -- City latitude.

        """
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
