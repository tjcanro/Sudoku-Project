import pygame
from constants import *
from board import Board




#The draw_game_start function creates the start screen as well as the menu options
def draw_game_start(screen):
    start_title_font = pygame.font.Font(None, 80)
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
    #While Loop that verifies which difficulty button is chosen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 30
                if medium_rectangle.collidepoint(event.pos):
                    return 40
                if hard_rectangle.collidepoint(event.pos):
                    return 50
        pygame.display.update()

#draw_game_win function makes the screen in the event of a game win and accounts for restart
def draw_game_win(screen):
    win_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill(BG_COLOR)

    win_surface = win_title_font.render("Game Won!", True, LINE_COLOR)
    win_rectangle = win_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(win_surface, win_rectangle)
    #Creates exit button and creates its space on the screen
    exit_text = button_font.render("Exit", True, BG_COLOR)

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(exit_surface, exit_rectangle)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    pygame.quit()
        pygame.display.update()

#The draw_game_loss function accounts for if the sudoku game has been lost and creates the screen for this condition
def draw_game_loss(screen):
    loss_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill(BG_COLOR)

    loss_surface = loss_title_font.render("Game Over :(", True, LINE_COLOR)
    loss_rectangle = loss_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(loss_surface, loss_rectangle)

    restart_text = button_font.render("Restart", True, BG_COLOR)

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    #screen.blit places the restart button on the screen
    screen.blit(restart_surface, restart_rectangle)

    while True:
        #This for loop accounts for the options to quit and restart the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    main()
        pygame.display.update()


def main():
    #The main starts by initializing the main menu and creates variables that account for the state of the game
    game_over = False
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    difficulty = draw_game_start(screen)
    current_board = Board(WIDTH, HEIGHT, screen, difficulty)
    current_board.draw()
    reset_rect, restart_rect, exit_rect = current_board.draw()
    selected = False
    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #This if statement accounts for when the game is actively being played
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                column, row = current_board.click(x, y)
                #This if statement accounts for the reset, restart, and quit implementations
                if reset_rect.collidepoint(x,y):
                    current_board.reset_to_original()
                if exit_rect.collidepoint(x, y):
                    pygame.quit()
                if restart_rect.collidepoint(x, y):
                    main()
                if 0 <= row <= 8 and 0 <= column <= 8:
                    if current_board.original[int(row)][int(column)] == 0:
                        current_cell = current_board.select(row, column)
                        selected = True
                        current_board.draw()
            pygame.display.update()
        #This while loop accounts for when a specific cell is selected
        while selected:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        current_cell.set_cell_value(0)
                    # This accounts for every case of either adding or deleting a cell
                    if event.key == pygame.K_1:
                        current_cell.set_cell_value(1)
                    if event.key == pygame.K_2:
                        current_cell.set_cell_value(2)
                    if event.key == pygame.K_3:
                        current_cell.set_cell_value(3)
                    if event.key == pygame.K_4:
                        current_cell.set_cell_value(4)
                    if event.key == pygame.K_5:
                        current_cell.set_cell_value(5)
                    if event.key == pygame.K_6:
                        current_cell.set_cell_value(6)
                    if event.key == pygame.K_7:
                        current_cell.set_cell_value(7)
                    if event.key == pygame.K_8:
                        current_cell.set_cell_value(8)
                    if event.key == pygame.K_9:
                        current_cell.set_cell_value(9)
                    #This if statement accounts for deleting the value in the cell
                    if event.key == pygame.K_BACKSPACE:
                        current_cell.set_cell_value(0)
                        current_cell.selected = True
                        current_board.draw()
                        pygame.display.update()
                    current_board.update_board()
                    current_cell.draw(screen)
                    current_board.check_board()
                    current_cell.selected = True
                    current_board.draw()
                    #This statement checks for the win condition if the board is full
                    if current_board.is_full():
                        if current_board.check_board():
                            draw_game_win(screen)
                        else:
                            draw_game_loss(screen)
                        game_over = True
                        selected = False
                #This accounts for the reset, restart, and quit functions
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if reset_rect.collidepoint(x, y):
                        current_board.reset_to_original()
                    if exit_rect.collidepoint(x, y):
                        pygame.quit()
                    if restart_rect.collidepoint(x, y):
                        main()
                    column, row = current_board.click(x, y)
                    if 0 <= row <= 8 and 0 <= column <= 8:
                        if current_board.original[int(row)][int(column)] == 0:
                            current_cell = current_board.select(row, column)
                            selected = True
                            current_board.draw()
                pygame.display.update()
            pygame.display.update()

#Implements the main
if __name__ == "__main__":
    main()
