#<summary>Defines objects that store grid coordinates.</summary>
#<author>Aleksandar Mitrevski</author>
class Coordinates:
    #<summary>Creates a new coordinates object.</summary>
    #<param name='row'>A number denoting grid row.</param>
    #<param name='column'>A number denoting grid column.</param>
    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column

    #<summary>Compares the row and column values of two 'Coordinates' objects.</summary>
    #<param name='coordinates'>The object that we want to compare with the current one.</param>
    #<returns>'True' if the row and column values are equal and false otherwise.</returns>
    def __eq__(self, coordinates):
        return self.row == coordinates.row and self.column == coordinates.column

    #<summary>Calculates the current object's hash value.</summary>
    #<returns>The current object's hash value</returns>
    def __hash__(self):
        return (hash(self.row) ^ hash(self.b) ^ hash((self.row, self.column)))

    #<returns>The row value of the current object.</returns>
    def getRow(self):
        return self.row

    #<returns>The column value of the current object.</returns>
    def getColumn(self):
        return self.column

    #<summary>Sets the row value of the current object.</summary>
    #<param name='row'>The new row value.</param>
    def setRow(self, row):
        self.row = row
        return self

    #<summary>Sets the column value of the current object.</summary>
    #<param name='column'>The new row value.</param>
    def setColumn(self, column):
        self.column = column
        return self

    #<summary>Prints the coordinates in a nice format.</summary>
    def printCoordinates(self):
        print '[' + str(self.row) + ', ' + str(self.column) + ']'
