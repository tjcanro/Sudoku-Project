import math
import random


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.remove_cells = removed_cells
        self.row_length = row_length
        self.box_length = int(math.sqrt(row_length))
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
        for i in range(0, self.row_length):
            if self.board[row][i] == num:
                return False
        return True

    def valid_in_col(self, col, num):
        for i in range(0, self.row_length):
            if self.board[i][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - (row % 3),
                                                                                             col - (col % 3), num):
            return True
        return False

    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                num = random.randint(1, 9)
                while not self.valid_in_box(row_start, col_start, num):
                    num = random.randint(1, 9)
                self.board[i][j] = num

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

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


def generate_sudoku(size, removed=0):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    # sudoku.remove_cells()
    board = sudoku.get_board()
    sudoku.print_board()
    return board


generate_sudoku(9, 0)
