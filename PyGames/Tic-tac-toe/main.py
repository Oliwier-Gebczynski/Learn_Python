import pygame, sys
import numpy as np

pygame.init()
running = True

# variables
bgc = (100, 100, 255)
line_c = (150, 100, 255)

# display settings
screen_width = 900
screen_height = 900

screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(bgc)

# board
board = np.zeros((3, 3))
print(board)

# draw lines
line_width = 20

def draw_lines():
    # horizontal
    pygame.draw.line(screen, line_c, (15, 300), (885, 300), line_width)
    pygame.draw.line(screen, line_c, (15, 600), (885, 600), line_width)
    # vertical
    pygame.draw.line(screen, line_c, (300, 15), (300, 885), line_width)
    pygame.draw.line(screen, line_c, (600, 15), (600, 885), line_width)

# mark on board
def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0



# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.update()
    draw_lines()