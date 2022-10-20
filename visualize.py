from hashlib import algorithms_available
from pickle import GLOBAL
import pygame
import time
import sys
import processIO as IO

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 172, 28)
DARK_ORANGE = (139, 64, 0)
GRAY = (128, 128, 128)

GOODBLUE='#20B2AA'

MAZE = []
BONUS=[]
VIS=[]
SOL=[]
SRC=(0,0)
DST=(0,0)
ALGNAME=''
STAR=None
#Init pygame
WIDTH = 1440 #screen width
HEIGHT = 600 #screen height
SCREEN_SIZE = [WIDTH, HEIGHT]
TILE = 0 #size of each tile
FPS = 60








def MazeInitialize(MAZE):
    cnt =0;
    for row in range(len(MAZE)):
        for col in range(len(MAZE[row])):
            if MAZE[row][col] == 'x':
                pygame.draw.rect(screen, DARK_ORANGE, (col * TILE, row * TILE, TILE, TILE))
                pygame.draw.rect(screen, GRAY, (col * TILE, row * TILE, TILE - 2, TILE - 2))

            if MAZE[row][col] == 'v':
                
                
                pygame.draw.rect(screen, GOODBLUE, (col * TILE, row * TILE, TILE, TILE))
            if MAZE[row][col] == ' ':
                pygame.draw.rect(screen, WHITE, (col * TILE, row * TILE, TILE, TILE))
            if (row,col) == SRC:
                pygame.draw.rect(screen, RED, (col * TILE, row * TILE, TILE, TILE))
            if (row, col) == DST:
                pygame.draw.rect(screen, ORANGE, (col * TILE, row * TILE, TILE, TILE))
            if MAZE[row][col] == '+':
                screen.blit(STAR,(col * TILE, row * TILE))

def draw_window():
    MazeInitialize(MAZE)


def run_visualization(pathIn,alg):
    
    global MAZE ,BONUS,VIS,SOL,SRC,DST,ALGNAME,screen,TILE,STAR
    BONUS,MAZE=IO.read_file(pathIn)
    if len(MAZE) >= 40 or len(MAZE[0]) >= 80:
        TILE = 18
    else: 
        TILE = 20
    WIDTH = TILE*len(MAZE[0])  # screen width
    HEIGHT = TILE*len(MAZE)  # screen height
    SCREEN_SIZE = [WIDTH, HEIGHT]
    out = alg(MAZE,BONUS)
    VIS=list(out[2].keys())
  
    SOL=out[3]
    SRC=out[0]
    DST=out[1]
    SOL.pop(0)
    TILE=int(HEIGHT/len(MAZE))
    ALGNAME=alg.__name__.upper()
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE) #set screen size
    pygame.display.set_caption("VISUALIZATION {}".format(ALGNAME)) #set caption

    STAR=pygame.image.load("./img/gcheems.png").convert_alpha()
    STAR = pygame.transform.scale(STAR, (TILE*1.2, TILE*1.2))
    screen.fill((255,255,255))

    algorithm_running = True
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        draw_window()
        
        if algorithm_running:
            if len(VIS)>0:
                current =VIS.pop(0)
                x=current[0]
                y=current[1]
                if (x,y)==DST:
                    VIS.clear()
                #mark cell VISited
                tmp = list(MAZE[x])
                tmp[y]='v'
                MAZE[x] = ''.join(tmp)
                ##
                
                pygame.draw.rect(screen, BLUE, (y * TILE, x * TILE, TILE, TILE))
                pygame.time.wait(30)
                pygame.display.update()
            else:
                for node in SOL:
                    pygame.draw.rect(screen, GREEN, (node[1] * TILE, node[0] * TILE, TILE, TILE))
                    pygame.time.wait(70)
                    pygame.display.update()
                algorithm_running = False
            pygame.time.wait(50)
            
        else:
            pygame.time.wait(1500)
            pygame.quit()
            sys.exit()

import bfs
import dfs
import ucs
import greedy as gbfs
import astar
import alg1
path = './input/level_2/input3.txt'
# alg =bfs.bfs
# alg=alg1.ALG_heuristic_1
alg=alg1.ALG_heuristic_1
run_visualization(path,alg)

