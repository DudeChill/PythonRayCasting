import pygame
from pygame.locals import *
import sys
import math
import const
pygame.init()
fps = 144
fpsclock = pygame.time.Clock()
res = w, h = (500, 500)
flags = pygame.NOFRAME
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
blue = 0, 0, 255
squares = []
walls = []
wall = const.walls
Pi = math.pi
fov = Pi / 3
half_fov = fov / 2
playerAngle = Pi
leg = 100
coord = [250, 250]
rays = 10
stepAngle = fov / rays
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
    walls = []
    squares = []
    for m in range(len(map)):
        for n in range(len(map[m])):
            if (map[n][m] == "#"):
                squares.append(square(scale * m, scale * n, black, 1))
            else:
                walls.append(square(scale * m, scale * n, black, 0))

screen = pygame.display.set_mode(res, flags, vsync=1)
def gridline(wall):
    gl = []
    for w in wall:
        gl.append((w.left/scale, w.top/scale, (w.left/scale)+1, (w.top/scale)+1))
    return gl
    
def hit(lineTrig, coord, gl):
    playerTan = 0
    if lineTrig[0] - coord[0] != 0 and lineTrig[1] - coord[1] != 0:
        playerTan = (lineTrig[1] - coord[1]) / (lineTrig[0] - coord[0])
        gx = scale / playerTan
        gy = scale * playerTan
        print(gx,gy)
        for g in gl:
            if lineTrig[0]/scale > g[0] or lineTrig[0]/scale < g[2] or lineTrig[1]/scale > g[1] or lineTrig[1]/scale < [3]:
                pass
            else:
                lineTrig[0] += gx
                lineTrig[1] += gy
                
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(white)
    grid()
    gl = gridline(wall)
    A = 0
    lineTrig = [coord[0] + math.sin(playerAngle) * leg, coord[1] + math.cos(playerAngle) * leg]
    print(lineTrig[0]/scale,lineTrig[1]/scale)
    player = pygame.draw.circle(screen, red, coord, 10)
    view = pygame.draw.line(screen, blue, coord, lineTrig, width=2)
    hit(lineTrig, coord, gl)
    key_input = pygame.key.get_pressed()
    if key_input[K_UP]:
        coord[0] += math.sin(playerAngle) / 2
        lineTrig[0] = coord[0] + math.sin(playerAngle) * leg
        coord[1] += math.cos(playerAngle) / 2
        lineTrig[1] = coord[1] + math.cos(playerAngle) * leg
    if key_input[K_DOWN]:
        coord[0] -= math.sin(playerAngle) / 2
        lineTrig[0] = coord[0] + math.sin(playerAngle) * leg
        coord[1] -= math.cos(playerAngle) / 2
        lineTrig[1] = coord[1] + math.cos(playerAngle) * leg
    if key_input[K_a]:
        playerAngle += 0.01
        print(playerAngle)
    if key_input[K_d]:
        playerAngle -= 0.01
        print(playerAngle)
    pygame.display.update()
    fpsclock.tick(fps)
