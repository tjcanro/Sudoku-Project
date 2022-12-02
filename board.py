from cell import Cell
from sudoku_generator import *
from constants import *
import pygame

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = generate_sudoku(9, difficulty)
        self.cells = [
            [Cell(self.board[i][j], i, j, screen) for j in range(9)]
            for i in range(9)
        ]

    def draw(self):
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(BG_COLOR)
        for i in range(1, BOARD_ROWS):
            if i % 3 != 0:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH
                )
            else:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    BOLD_LINE_WIDTH
                )

        # draw vertical lines
        for j in range(1, BOARD_COLS):
            if j % 3 != 0:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (j * SQUARE_SIZE, 0),
                    (j * SQUARE_SIZE, HEIGHT),
                    LINE_WIDTH
                )
            else:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (j * SQUARE_SIZE, 0),
                    (j * SQUARE_SIZE, HEIGHT),
                    BOLD_LINE_WIDTH
                )
        for i in self.cells:
            for j in i:
                j.draw(screen)

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass

