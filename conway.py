import pygame
import random
from pygame.locals import *
pygame.init()

window_size = 800
surface = pygame.display.set_mode((window_size, window_size))
box_number = 50
box_size = window_size/box_number
black = (0, 0, 0)
white = (255, 255,255)
running = True

def update():
    cells = [[random.randint(0, 1) for x in range(box_number)] for x in range(box_number)]
    return(cells)

def handle_events(event):
    ''
    
def render(cells):
    surface.fill(white)
    for y, row in enumerate(cells):
        y *= box_size
        for x, cell in enumerate(row):
            x *= box_size
            if cell == 1:
                square = (x, y, box_size, box_size)
                pygame.draw.rect(surface, black, square)

def game_loop():
    global running
    cells = update()
    while running:
        render(cells)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
game_loop()