import pygame, sys
from constants import *
from cell import Cell
from board import Board


def draw_game_start(screen):
    start_title_font = pygame.font.Font(None, 100)
    game_mode_font = pygame.font.Font(None, 60)
    button_font = pygame.font.Font(None, 40)

    screen.fill(BG_COLOR)

    title_surface = start_title_font.render("Welcome to Sudoku", True, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(title_surface, title_rectangle)

    game_mode_surface = game_mode_font.render("Select Game Mode:", True, LINE_COLOR)
    game_mode_rectangle = game_mode_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_mode_surface, game_mode_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", True, (255, 255, 255))
    medium_text = button_font.render("Medium", True, (255, 255, 255))
    hard_text = button_font.render("Hard", True, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 150, HEIGHT // 2 + 150))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2 + 150, HEIGHT // 2 + 150))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)


def draw_game_win(screen):
    win_title_font = pygame.font.Font(None, 100)
    exit_mode_font = pygame.font.Font(None, 60)

    screen.fill(BG_COLOR)

    win_surface = win_title_font.render("Game Won!", True, LINE_COLOR)
    win_rectangle = win_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(win_surface, win_rectangle)

    exit_mode_surface = exit_mode_font.render("Select Game Mode:", True, LINE_COLOR)
    exit_mode_rectangle = exit_mode_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(exit_mode_surface, exit_mode_rectangle)


def draw_game_loss(screen):
    loss_title_font = pygame.font.Font(None, 100)
    restart_mode_font = pygame.font.Font(None, 60)

    screen.fill(BG_COLOR)

    loss_surface = loss_title_font.render("Game Over :(", True, LINE_COLOR)
    loss_rectangle = loss_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(loss_surface, loss_rectangle)

    restart_mode_surface = restart_mode_font.render("Select Game Mode:", True, LINE_COLOR)
    restart_mode_rectangle = restart_mode_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(restart_mode_surface, restart_mode_rectangle)


def main():
    game_over = False

    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    x = Board(WIDTH, HEIGHT, screen, 10)
    x.draw()

    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


if __name__ == "__main__":
    main()
