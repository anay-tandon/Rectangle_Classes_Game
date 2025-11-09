import pygame
from random import randint
pygame.init()

screen = pygame.display.set_mode((600, 600))
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

class Rectangle:
    def __init__(screen, self, rect, color, width = 0):
        self.rect = rect
        self.color = color
        self.width = width
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.rect, self.color, self.width)

width = 2
rect = (100, 100, 100, 150)

pygame.draw.rect(screen, red, rect, width)
pygame.display.update()