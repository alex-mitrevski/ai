import city

class CityFileLibrary(object):
    """Defines a library for reading city-related
    data and storing it into appropriate 'city.CityData' object.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, file_name):
        """Initializes a file library.

        Keyword arguments:
        file_name -- Name of a file that should be read.

        """
        self.file_name = file_name

    def get_city_data(self):
        """Reads a file and returns a list of 'city.CityData' objects
        storing the related city data. Assumes that the city details
        are stored in one file line, separated by a tab character.

        """
        fileLines = self._read_file()

        cityData = []
        for _,line in enumerate(fileLines):
            name, longitude, latitude = line.split('\t')
            cityDataObject = city.CityData(name, float(longitude), float(latitude))
            cityData.append(cityDataObject)

        return cityData

    def _read_file(self):
        """Reads a file and returns a list of all file lines."""
        cityFile = open(self.file_name)
        fileContents = cityFile.read()
        cityFile.close()

        fileLines = fileContents.split('\n')
        return fileLines[:len(fileLines)-1]
