from cell import Cell
from sudoku_generator import *
from constants import *
import pygame


class Board:
    # Initializes the Board class with dimensions as well as the difficulty
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board, self.filled, self.original = generate_sudoku(9, difficulty)
        # Initializes cells to be a cell objecthat is 9 rows by 9 columns on the screen
        self.cells = [
            [Cell(self.board[i][j], i, j, screen) for j in range(9)]
            for i in range(9)
        ]

    def draw(self):
        # This function sets up th board screen in pygame and includes bold lines to indicate parts of the grid
        self.screen.fill(BG_COLOR)
        for i in range(1, BOARD_ROWS + 1):
            if i % 3 != 0:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH
                )
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    BOLD_LINE_WIDTH
                )

        # draw vertical lines
        for j in range(1, BOARD_COLS):
            if j % 3 != 0:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (j * SQUARE_SIZE, 0),
                    (j * SQUARE_SIZE, HEIGHT - (HEIGHT - WIDTH)),
                    LINE_WIDTH
                )
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (j * SQUARE_SIZE, 0),
                    (j * SQUARE_SIZE, HEIGHT - (HEIGHT - WIDTH)),
                    BOLD_LINE_WIDTH
                )
        # This for loop goes through each cell in the list of cell objects and draws each individual cells
        for i in self.cells:
            for j in i:
                j.draw(self.screen)

        button_font = pygame.font.Font(None, 40)

        reset_text = button_font.render("Reset", True, (255, 255, 255))
        restart_text = button_font.render("Restart", True, (255, 255, 255))
        exit_text = button_font.render("Exit", True, (255, 255, 255))

        # Initialize button background color and text
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surface.fill(LINE_COLOR)
        reset_surface.blit(reset_text, (10, 10))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill(LINE_COLOR)
        restart_surface.blit(restart_text, (10, 10))
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(LINE_COLOR)
        exit_surface.blit(exit_text, (10, 10))

        # Initialize button rectangle
        reset_rectangle = reset_surface.get_rect(
            center=(WIDTH // 2 - 200, HEIGHT // 2 + 300))
        restart_rectangle = restart_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 300))
        exit_rectangle = exit_surface.get_rect(
            center=(WIDTH // 2 + 200, HEIGHT // 2 + 300))

        # Draw buttons
        self.screen.blit(reset_surface, reset_rectangle)
        self.screen.blit(restart_surface, restart_rectangle)
        self.screen.blit(exit_surface, exit_rectangle)

        return reset_rectangle, restart_rectangle, exit_rectangle

    # The select function marks the cell that is being edited
    def select(self, row, col):
        for i in self.cells:
            for j in i:
                if j.row == row and j.col == col:
                    j.selected = True
                    return j

    # The click function returns a tuple that generalizes the position of the row and column
    def click(self, x, y):
        row = x // SQUARE_SIZE
        col = y // SQUARE_SIZE
        return row, col

    # reset_to_original resets the board to its original state
    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.original[i][j]
                (self.cells[i][j]).value = self.board[i][j]
        self.update_board()
        self.draw()

    # is_full determines whether or not a particular cell was filled or not
    def is_full(self):
        for row in self.board:
            for num in row:
                if num == 0:
                    return False
        return True

    # update_board updates the board to account for changes inside the cell
    def update_board(self):
        for i in self.cells:
            for j in i:
                self.board[j.row][j.col] = j.value

    # check_board checks the board to verify that the sudoku is solved correctly
    def check_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != self.filled[i][j]:
                    return False
        return True
