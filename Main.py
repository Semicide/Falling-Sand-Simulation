import pygame as pg
import numpy as np
import sys

pg.init()
width=640
height=480
GRID_SIZE=10
def twoDarray(grid_x,grid_y):
    arr = [grid_x]
    for i in range(len(arr)):
        arr[i] =[grid_y]
    return arr
def clicked_grid():

def fill_grid():
    pg.draw.rect()
def window():
    screen= pg.display.set_mode(window,height)
    pg.display.set_caption("FallingSand")
    font=pg.font.SystemFont("Arial",18)
running=True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Get the position of the mouse click and convert it to grid coordinates
            mouse_x, mouse_y = pg.mouse.get_pos()
            grid_x = mouse_x // GRID_SIZE
            grid_y = mouse_y // GRID_SIZE
            clicked_grid.append((grid_x, grid_y))  # Store the clicked grid coordinates
            fill_grid(grid_x, grid_y)

