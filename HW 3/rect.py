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
    def __init__(self, screen, pos, rw, rh, color, width = 0):
        self.rw = rw
        self.rh = rh
        self.pos = pos
        self.color = color
        self.width = width
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.rw, self.rh), self.width)

    def grow(self):
        self.rw += 10
        self.rh += 10
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.rw, self.rh), self.width)

    def shrink(self):
        self.rw -= 10
        self.rh -= 10
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.rw, self.rh), self.width)

rect1 = Rectangle(screen, (200, 200), 100, 150, red, 0)
rect2 = Rectangle(screen, (200, 200), 150, 200, green, 5)
rect3 = Rectangle(screen, (200, 200), 200, 250, yellow, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            rect1.draw()
            rect2.draw()
            rect3.draw()
            pygame.display.update()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            rect1.grow()
            rect2.grow()
            rect3.grow()
            pygame.display.update()

        elif event.type == pygame.KEYDOWN:
            rect1.shrink()
            rect2.shrink()
            rect3.shrink()
            pygame.display.update()



            
