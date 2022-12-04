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
        self.board, self.filled, self.original = generate_sudoku(9, difficulty)
        self.cells = [
            [Cell(self.board[i][j], i, j, screen) for j in range(9)]
            for i in range(9)
        ]

    def draw(self):
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

    def select(self, row, col):
        for i in self.cells:
            for j in i:
                if j.row == row and j.col == col:
                    j.selected = True
                    return j

    def click(self, x, y):
        row = x // SQUARE_SIZE
        col = y // SQUARE_SIZE
        return row, col

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.original[i][j]
        self.update_board()
        self.draw()

    def is_full(self):
        for row in self.board:
            for num in row:
                if num == 0:
                    return False
        return True

    def update_board(self):
        for i in self.cells:
            for j in i:
                self.board[j.row][j.col] = j.value

    def check_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != self.filled[i][j]:
                    return False
        return True
