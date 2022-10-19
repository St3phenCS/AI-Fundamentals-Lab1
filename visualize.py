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
SOl=[]
SRC=(0,0)
DST=(0,0)
ALGNAME=''
#Init pygame
WIDTH = 1000 #screen width
HEIGHT = 500 #screen height
SCREEN_SIZE = [WIDTH, HEIGHT]
TILE = 0 #size of each tile
FPS = 60








def MazeInitialize(MAZE):
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
                pygame.draw.rect(screen, GREEN, (col * TILE, row * TILE, TILE, TILE))


def draw_window():
    MazeInitialize(MAZE)


def run_visualization(pathIn,alg):
    
    global MAZE ,BONUS,VIS,SOl,SRC,DST,ALGNAME,screen,TILE
    BONUS,MAZE=IO.read_file(pathIn)
    out = alg(MAZE)
    VIS=list(out[2].keys())
    SOl=out[3]
    SRC=out[0]
    DST=out[1]
    TILE=int(HEIGHT/len(MAZE))
    ALGNAME=bfs.bfs.__name__.upper()
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE) #set screen size
    pygame.display.set_caption("VISUALIZATION {}".format(ALGNAME)) #set caption
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
                #mark cell VISited
                tmp = list(MAZE[x])
                tmp[y]='v'
                MAZE[x] = ''.join(tmp)
                ##
                
                pygame.draw.rect(screen, BLUE, (y * TILE, x * TILE, TILE, TILE))
                pygame.time.wait(50)
                pygame.display.update()
            else:
                for node in SOl:
                    pygame.draw.rect(screen, GREEN, (node[1] * TILE, node[0] * TILE, TILE, TILE))
                    pygame.time.wait(50)
                    pygame.display.update()
                algorithm_running = False
            pygame.time.wait(50)
            
        else:
            pygame.time.wait(1000)
            pygame.quit()
            sys.exit()

import bfs
import dfs
import ucs
import greedy as gbfs
import astar
path = './input/level_1/input3.txt'
alg =astar.astar_heuristic_2
run_visualization(path,alg)