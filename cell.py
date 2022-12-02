import pygame
from sudoku import *
from constants import *


class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self, screen):
        number_font = pygame.font.SysFont(NUMBER_FONT, NUMBER_FONT_SIZE)
        num1_sur = number_font.render('1', True, NUM_COLOR)
        num2_sur = number_font.render('2', True, NUM_COLOR)
        num3_sur = number_font.render('3', True, NUM_COLOR)
        num4_sur = number_font.render('4', True, NUM_COLOR)
        num5_sur = number_font.render('5', True, NUM_COLOR)
        num6_sur = number_font.render('6', True, NUM_COLOR)
        num7_sur = number_font.render('7', True, NUM_COLOR)
        num8_sur = number_font.render('8', True, NUM_COLOR)
        num9_sur = number_font.render('9', True, NUM_COLOR)

        if self.value == '1':
            num1_rect = num1_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num1_sur, num1_rect)
        if self.value == '2':
            num2_rect = num1_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num2_sur, num2_rect)
        if self.value == '3':
            num3_rect = num1_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num2_sur, num3_rect)
        if self.value == '4':
            num4_rect = num1_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num1_sur, num4_rect)
        if self.value == '5':
            num5_rect = num1_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num1_sur, num5_rect)
        if self.value == '6':
            num6_rect = num1_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num1_sur, num6_rect)
        if self.value == '7':
            num7_rect = num1_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num1_sur, num7_rect)
        if self.value == '8':
            num8_rect = num1_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num1_sur, num8_rect)
        if self.value == '9':
            num9_rect = num1_sur.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num1_sur, num9_rect)
