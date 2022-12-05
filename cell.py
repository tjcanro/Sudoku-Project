import pygame
from constants import *


class Cell:

   #Default constructor for the Cell class
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
    #Setter function for the Cell class
    def set_cell_value(self, value):
        self.value = value
    #Draws the cell with the number inside of it
    def draw(self, screen):
        number_font = pygame.font.SysFont(NUMBER_FONT, NUMBER_FONT_SIZE)
        #Sets up the fonts and colors for each possible number on the board
        num0_sur = number_font.render('0', True, NUM_COLOR)
        num1_sur = number_font.render('1', True, NUM_COLOR)
        num2_sur = number_font.render('2', True, NUM_COLOR)
        num3_sur = number_font.render('3', True, NUM_COLOR)
        num4_sur = number_font.render('4', True, NUM_COLOR)
        num5_sur = number_font.render('5', True, NUM_COLOR)
        num6_sur = number_font.render('6', True, NUM_COLOR)
        num7_sur = number_font.render('7', True, NUM_COLOR)
        num8_sur = number_font.render('8', True, NUM_COLOR)
        num9_sur = number_font.render('9', True, NUM_COLOR)
        #This part make the outline of the cell turn red when the selected cell when the cell is the clicked
        if self.selected:
            pygame.draw.rect(screen, OUTLINE_COLOR, pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE,
                             SQUARE_SIZE, SQUARE_SIZE), 2)
            self.selected = False

        #This sequence of if-statements helps ensure that each value is drawn correctly and in the correct position
        if self.value == 0:
            num_rect = num0_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
        if self.value == 1:
            num_rect = num1_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num1_sur, num_rect)
        if self.value == 2:
            num_rect = num2_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num2_sur, num_rect)
        if self.value == 3:
            num_rect = num3_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num3_sur, num_rect)
        if self.value == 4:
            num_rect = num4_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num4_sur, num_rect)
        if self.value == 5:
            num_rect = num5_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            #screen.blit places numbers inside the actual screen
            screen.blit(num5_sur, num_rect)
        if self.value == 6:
            num_rect = num6_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num6_sur, num_rect)
        if self.value == 7:
            num_rect = num7_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num7_sur, num_rect)
        if self.value == 8:
            num_rect = num8_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num8_sur, num_rect)
        if self.value == 9:
            num_rect = num9_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num9_sur, num_rect)
