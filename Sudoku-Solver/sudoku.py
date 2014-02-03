import numpy

class SudokuTable(object):
    def __init__(self, values):
        table = list()

        for i in xrange(9):
            row = list()
            for j in xrange(9):
                try:
                    current_value = int(values[i*9 + j])
                    row.append(current_value)
                except ValueError:
                    row.append(-1)
            table.append(row)
        self.table = numpy.array(table)

    def table_filled(self):
        for i in xrange(9):
            row_values = self.table[i, numpy.where(self.table[i]>0)[0]]
            if len(row_values) != 9:
                return False

        return True

    def select_unassigned_field(self):
        row = -1
        column = -1

        for i in xrange(9):
            for j in xrange(9):
                if self.table[i,j] == -1:
                    row = i
                    column = j
                    break

            if row > -1:
                break

        allowed_values = numpy.array([i+1 for i in xrange(9)])

        row_values = self.table[row, numpy.where(self.table[row]>0)[0]]
        allowed_values = numpy.setdiff1d(allowed_values, row_values)

        full_column = numpy.array(self.table[:,column])
        column_values = full_column[numpy.where(full_column>0)[0]]
        allowed_values = numpy.setdiff1d(allowed_values, column_values)

        closest_row = row - row % 3
        closest_column = column - column % 3
        full_square = numpy.array([self.table[closest_row, closest_column:closest_column+3], self.table[closest_row+1, closest_column:closest_column+3], self.table[closest_row+2, closest_column:closest_column+3]]).flatten()
        square_values = full_square[numpy.where(full_square>0)[0]]
        allowed_values = numpy.setdiff1d(allowed_values, square_values)

        return row, column, allowed_values