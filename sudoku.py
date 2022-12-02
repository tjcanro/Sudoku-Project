import pygame, sys
from constants import *
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
    game_mode_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_mode_surface, game_mode_rectangle)



def main():
    game_over = False

    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    number_font = pygame.font.SysFont(NUMBER_FONT, NUMBER_FONT_SIZE)

    draw_game_start(screen)


    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


if __name__ == "__main__":
    main()
