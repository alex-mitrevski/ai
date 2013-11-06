class Coordinates(object):
    """Defines x and y coordinates of a point.

    Author: Aleksandar Mitrevski

    """
    def __init__(self, x=-1., y=-1.):
        """Creates point coordinates.

        Keyword arguments:
        x -- The x coordinate of a point (default -1.)
        y -- The y coordinate of a point (default -1.)

        """
        self.x = x
        self.y = y

    def __eq__(self, rightHandObject):
        """Returns 'True' if 'rightHandObject' is equal to 'self' and 'False' otherwise.
        Returns 'NotImplemented' if 'rightHandObject' is not of type 'Coordinates'.

        Keyword arguments:
        rightHandObject - An object that we want to compare with 'self'.

        """
        if isinstance(rightHandObject, Coordinates):
            return abs(self.x - rightHandObject.x) < 0.05 and abs(self.y - rightHandObject.y) < 0.05
        return NotImplemented
