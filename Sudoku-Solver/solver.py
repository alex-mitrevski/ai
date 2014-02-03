import numpy
from sudoku import SudokuTable

class SudokuSolver(object):
    def solve_sudoku(self, sudoku_table):
        return self._sudoku_search(sudoku_table)

    def _sudoku_search(self, sudoku_table):
        if sudoku_table.table_filled():
            return sudoku_table

        row, column, allowed_values = sudoku_table.select_unassigned_field()
        for _,value in enumerate(allowed_values):
            if self.constraints_satisfied(sudoku_table, row, column, value):
                sudoku_table.table[row, column] = value
                result = self._sudoku_search(sudoku_table)
                if isinstance(result, SudokuTable):
                    return result
                sudoku_table.table[row, column] = -1

        return False

    def constraints_satisfied(self, sudoku_table, row, column, value):
        sudoku_table.table[row, column] = value

        row_values = sudoku_table.table[row, numpy.where(sudoku_table.table[row]>0)[0]]
        unique_elements = numpy.unique(row_values)
        if len(row_values) > len(unique_elements):
            sudoku_table.table[row, column] = -1
            return False

        full_column = numpy.array(sudoku_table.table[:,column])
        column_values = full_column[numpy.where(full_column>0)[0]]
        unique_elements = numpy.unique(column_values)
        if len(column_values) > len(unique_elements):
            sudoku_table.table[row, column] = -1
            return False

        closest_row = row - row % 3
        closest_column = column - column % 3
        full_square = numpy.array([sudoku_table.table[closest_row, closest_column:closest_column+3], sudoku_table.table[closest_row+1, closest_column:closest_column+3], sudoku_table.table[closest_row+2, closest_column:closest_column+3]]).flatten()
        square_values = full_square[numpy.where(full_square>0)[0]]
        unique_elements = numpy.unique(square_values)
        if len(square_values) > len(unique_elements):
            sudoku_table.table[row, column] = -1
            return False

        sudoku_table.table[row, column] = -1
        return True