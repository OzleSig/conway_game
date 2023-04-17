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
cells = [[random.randint(0, 1) for x in range(box_number)] for x in range(box_number)]

def update(cells):
    cell_len = range(box_number)
    for row in cell_len:
        for cell in cell_len:
            neighbour = 0
            for x in range(3):
                x = x-2
                row_next = row + x
                for y in range(3):
                    y = y-2
                    cell_next = cell + y
                    if not (row_next == row and cell_next == cell):
                        neighbour += cells[row_next][cell_next]
            if cells[row][cell] == 0 and neighbour == 3:
                cells[row][cell] = 1
            elif cells[row][cell] == 1:
                if 3 >= neighbour >= 2:
                    cells[row][cell] = 1
                else:
                    cells[row][cell] = 0
    return(cells)

def handle_events(event):
    ''
    
def render(cells):
    surface.fill(white)
    for y in range(len(cells)):
        y_cell = y
        y = float(y) * box_size
        for x in range(len(cells)):
            x_cell = x
            x =float(x) *  box_size
            if cells[y_cell][x_cell] == 1:
                square = (x, y, box_size, box_size)
                pygame.draw.rect(surface, black, square)

def game_loop():
    global running
    global cells
    while running:
        update(cells)
        render(cells)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
game_loop()