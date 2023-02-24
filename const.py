import pygame
from pygame.locals import *
res = w, h = (500, 500)
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
blue = 0, 0, 255
flags = pygame.NOFRAME
map = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "a", "a", "a", "a", "#", "#", "#"],
       ["#", "#", "#", "#", "a", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]
scale = w / len(map)
def square(left, top, color, wi):
    return pygame.draw.rect(screen, color, pygame.Rect(left, top, scale, scale), width=wi)


def grid():
    wall = []
    squares = []
    for m in range(len(map)):
        for n in range(len(map[m])):
            if (map[n][m] == "#"):
                squares.append(square(scale * m, scale * n, black, 1))
            else:
                wall.append(square(scale * m, scale * n, black, 0))
    return wall
screen = pygame.display.set_mode(res, flags, vsync=1)
walls = grid()