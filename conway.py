import pygame
import time
from pygame.locals import *
pygame.init()

window_size = 800
surface = pygame.display.set_mode((window_size, window_size))
box_number = 50
box_size = window_size/box_number
black = (0, 0, 0)
white = (255, 255,255)
running = True
cells = [[0 for i in range(box_number)] for i in range(box_number)]
neigh_nums = [[0 for i in range(box_number)] for i in range(box_number)]
mouse_down = False
pause = True

def neighbour(y_index, x_index):
        neigh_nums[y_index][x_index] = 0
        for y_mod in range(3):
            y_mod_index = y_mod-1
            y_neigh = y_index+y_mod_index
            for x_mod in range(3):
                x_mod_index = x_mod-1
                x_neigh = x_index+x_mod_index
                if not (y_mod_index == x_mod_index == 0 or y_neigh<0 or x_neigh<0 or y_neigh>=box_number or x_neigh>=box_number):
                    if cells[y_neigh][x_neigh] == 1:
                        neigh_nums[y_index][x_index] += 1

def update():
    if mouse_down:
        mouse_pos = pygame.mouse.get_pos()
        if not (mouse_pos[0] < 0 or mouse_pos[1] < 0 or mouse_pos[0]>= window_size or mouse_pos[1] >= window_size):
            x = int((mouse_pos[0]*box_number)/window_size)
            y = int((mouse_pos[1]*box_number)/window_size)
            cells[y][x] = 1
    if not pause:
        for y_index in range(box_number):
            for x_index in range(box_number):
                neighbour(y_index, x_index)
        for y_index in range(box_number):
            for x_index in range(box_number):
                if neigh_nums[y_index][x_index]>3 or neigh_nums[y_index][x_index]<2:
                    cells[y_index][x_index] = 0
                if neigh_nums[y_index][x_index]==3:
                    cells[y_index][x_index] = 1                

def handle_events(event):
    global mouse_down
    global pause
    if event.type == MOUSEBUTTONDOWN:
        mouse_down = True
    elif event.type == MOUSEBUTTONUP:
        mouse_down = False
    elif event.type == KEYDOWN:
        if event.key == K_SPACE:
            if pause == True:
                pause = False
            else:
                pause = True
    
def render():
    surface.fill(white)
    for y in range(len(cells)):
        y_index = y
        y = float(y) * box_size
        for x in range(len(cells)):
            x_index = x
            x = float(x) * box_size
            if cells[y_index][x_index] == 1:
                square = (x, y, box_size, box_size)
                pygame.draw.rect(surface, black, square)

def game_loop():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            handle_events(event)
        render()
        update()
        pygame.display.flip()
game_loop()