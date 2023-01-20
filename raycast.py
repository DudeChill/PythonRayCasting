import pygame
from pygame.locals import *
import sys
import math
pygame.init()
fps=60
fpsclock=pygame.time.Clock()
res = w,h = (500, 500)
flags = pygame.NOFRAME
white = 255,255,255
black = 0,0,0
red = 255,0,0
blue = 0,0,255
squares = []
walls = []
Pi = math.pi
fov = Pi/3
half_fov = fov/2
playerAngle = Pi
leg = 100
coord = [250,250]
rays = 10
stepAngle = fov/rays
map = [["#","#","#","#","#","#","#","#","#","#"],
       ["#","#","#","#","#","#","#","#","#","#"],
       ["#","#","#","a","a","a","a","#","#","#"],
       ["#","#","#","#","a","#","#","#","#","#"],
       ["#","#","#","#","#","#","#","#","#","#"],
       ["#","#","#","#","#","#","#","#","#","#"],
       ["#","#","#","#","#","#","#","#","#","#"],
       ["#","#","#","#","#","#","#","#","#","#"],
       ["#","#","#","#","#","#","#","#","#","#"],
       ["#","#","#","#","#","#","#","#","#","#"]]
scale = w/len(map)


def square(left,top,color,wi):
    return pygame.draw.rect(screen,color,pygame.Rect(left,top,scale,scale),width=wi)

def grid():
    for m in range(len(map)):
        for n in range(len(map[m])):
            if(map[m][n]=="#"):
                squares.append(square(scale*m,scale*n,black,1))
            else:
                walls.append(square(scale*m,scale*n,black,0))
screen = pygame.display.set_mode(res,flags,vsync=1)

def hit(line,cord):
    for short in squares:
        break
             
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    lineTrig = [coord[0] + math.sin(playerAngle)*leg,coord[1] + math.cos(playerAngle)*leg]
    screen.fill(white)
    grid()
    player = pygame.draw.circle(screen,red,coord,10)
    view = pygame.draw.line(screen,blue,coord,lineTrig,width=2)
    hit(lineTrig,coord)
    key_input = pygame.key.get_pressed()
    if key_input[K_UP]:
        coord[0] += math.sin(playerAngle)*5
        coord[1] += math.cos(playerAngle)*5
    if key_input[K_DOWN]:
        coord[0] -= math.sin(playerAngle)*5
        coord[1] -= math.cos(playerAngle)*5
    if key_input[K_a]:
        playerAngle += 0.05
    if key_input[K_d]:
        playerAngle -= 0.05
    pygame.display.update()
    fpsclock.tick(fps)
