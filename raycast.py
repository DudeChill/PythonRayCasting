import pygame
from pygame.locals import *
import sys
import math
pygame.init()
fps=144
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
    walls = []
    squares = []
    for m in range(len(map)):
        for n in range(len(map[m])):
            if(map[n][m]=="#"):
                squares.append(square(scale*m,scale*n,black,1))
            else:
                walls.append(square(scale*m,scale*n,black,0))
screen = pygame.display.set_mode(res,flags,vsync=1)

def hit(lineTrig,coord,walls):
    gl = []
    for w in walls:
        gl.append((math.floor(w[0]/scale),math.floor(w[1]/scale)))
    while lineTrig[0]-coord[0] != 0 and lineTrig[1]-coord[1] != 0:
        playerTan = (lineTrig[1]-coord[1])/(lineTrig[0]-coord[0])
        Xa = scale/playerTan
        Ya = scale/playerTan
        fx = math.floor(lineTrig[0]/scale)
        fy = math.floor(lineTrig[1]/scale)
        print(lineTrig)
        for g in gl:
            if g != (fx,fy):
                lineTrig[0] += Xa*(fx-g[0])
                lineTrig[1] += Ya*(fy-g[1])    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(white)
    grid()
    lineTrig = [coord[0] + math.sin(playerAngle)*leg,coord[1] + math.cos(playerAngle)*leg]
    player = pygame.draw.circle(screen,red,coord,10)
    view = pygame.draw.line(screen,blue,coord,lineTrig,width=2)
    #hit(lineTrig,coord,walls)
    key_input = pygame.key.get_pressed()
    if key_input[K_UP]:
        coord[0] += math.sin(playerAngle)/2
        coord[1] += math.cos(playerAngle)/2
    if key_input[K_DOWN]:
        coord[0] -= math.sin(playerAngle)/2
        coord[1] -= math.cos(playerAngle)/2
    if key_input[K_a]:
        playerAngle += 0.01
        print(playerAngle)
    if key_input[K_d]:
        playerAngle -= 0.01
        print(playerAngle)
    pygame.display.update()
    fpsclock.tick(fps)
