import math, random


class SudokuGenerator:
    def __init__(self, removed_cells, row_length=9):
        self.remove_cells = removed_cells
        self.row_length = row_length
        self.box_length = math.sqrt(row_length)
        self.board = []
        for i in range(0, self.row_length):
            self.board.append([])
            for j in range(0, self.row_length):
                self.board[i].append(0)

    def get_board(self):
        return self.board

    def print_board(self):
        for i in range(0, self.row_length):
            print(self.board[i])

    def valid_in_row(self, row, num):
        if num in self.get_board()[row]:
            return False
        else:
            return True

    def valid_in_col(self, col, num):
        for i in self.board:
            if self.board[col] == num:
                return False
            else:
                return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        pass

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        pass

    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                self.board[i][j] = random.randint(1, 9)

    def fill_diagonal(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.board[i][j] = random.randint(1, 9)
        for i in range(3, 6):
            for j in range(3, 6):
                self.board[i][j] = random.randint(1, 9)
        for i in range(6, 9):
            for j in range(6, 9):
                self.board[i][j] = random.randint(1, 9)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        pass


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed=0):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


# sudo = SudokuGenerator(0)
# print(sudo.valid_in_row(3, 6))
# sudo.print_board()
# print(sudo.valid_in_col(3, 6))
# sudo.fill_diagonal()
# sudo.print_board()
# print(sudo.fill_remaining(0, 3))
# sudo.fill_values()
# sudo.print_board()
generate_sudoku(9)
