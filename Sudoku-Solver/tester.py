from sudoku import SudokuTable
from solver import SudokuSolver

table = SudokuTable('some string representing a table')
solver = SudokuSolver()

solution = solver.solve_sudoku(table)
if isinstance(solution, SudokuTable):
    for i in xrange(9):
        row = ''
        for j in xrange(9):
            row = row + str(solution.table[i,j]) + ' '
        print row