from asyncio.windows_events import NULL
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

STAR=None
CHEEMS1=None
CHEEMSG=None
BCHEEMS=None
WCHEEMS=None


# STAR=pygame.transform.scale(STAR, (2, 2))
GOODBLUE='#20B2AA'

MAZE = []
BONUS=[]
VIS=[]
SOl=[]
SRC=(0,0)
DST=(0,0)
ALGNAME=''
#Init pygame
WIDTH = 1440 #screen width
HEIGHT = 720 #screen height
SCREEN_SIZE = [WIDTH, HEIGHT]
TILE = 0 #size of each tile
FPS = 60








def MazeInitialize(MAZE):
    for row in range(len(MAZE)):
        for col in range(len(MAZE[0])):
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
                # pygame.draw.rect(screen, GREEN, (col * TILE, row * TILE, TILE, TILE))
                screen.blit(CHEEMSG,(col * TILE*0.9, row * TILE))
            if MAZE[row][col] == '+':
                screen.blit(STAR,(col * TILE, row * TILE))
               
                


def draw_window():
    MazeInitialize(MAZE)


def run_visualization(pathIn,alg):
    
    global MAZE ,BONUS,VIS,SOl,SRC,DST,ALGNAME,screen,TILE,STAR,CHEEMS1,CHEEMSG
    BONUS,MAZE=IO.read_file(pathIn)
    out = alg(MAZE)
    VIS=list(out[2].keys())
    SOl=out[3]
    SRC=out[0]
    DST=out[1]
    TILE=int(HEIGHT/len(MAZE))
    ALGNAME=alg.__name__.upper()
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE) #set screen size
    pygame.display.set_caption("VISUALIZATION {}".format(ALGNAME)) #set caption

    STAR=pygame.image.load("./img/star.png").convert_alpha()
    CHEEMS1=pygame.image.load("./img/cheems1.png").convert_alpha()
    CHEEMSG=pygame.image.load("./img/cheemsGirl.png").convert_alpha()
    BCHEEMS=pygame.image.load("./img/bigcheems.png").convert_alpha()
    WCHEEMS=pygame.image.load("./img/wowcheems.png").convert_alpha()

    STAR = pygame.transform.scale(STAR, (TILE*0.8, TILE*0.8))
    CHEEMS1=pygame.transform.scale(CHEEMS1, (TILE, TILE))
    CHEEMSG=pygame.transform.scale(CHEEMSG, (TILE*1.5, TILE*1.5))
    BCHEEMS=pygame.transform.scale(BCHEEMS, (TILE, TILE))
    WCHEEMS=pygame.transform.scale(WCHEEMS, (TILE*1.2, TILE*1.2))

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
                #mark cell VISited
                tmp = list(MAZE[x])
                tmp[y]='v'
                MAZE[x] = ''.join(tmp)
                ##
                
                # pygame.draw.rect(screen, BLUE, (y * TILE, x * TILE, TILE, TILE))
                screen.blit(CHEEMS1,(y * TILE, x * TILE))
                pygame.time.wait(50)
                pygame.display.update()
            else:
                prenode=SOl.pop(0)
                pygame.draw.rect(screen, RED, (prenode[1] * TILE,prenode[0] * TILE, TILE*1.2, TILE*1.2))
                for node in SOl:  
                    if prenode != NULL:
                        pygame.draw.rect(screen, GREEN, (prenode[1] * TILE,prenode[0] * TILE, TILE*1.2, TILE*1.2))
                        
                    prenode=node
                    screen.blit(WCHEEMS,(node[1] * TILE, node[0] * TILE))
                    pygame.time.wait(50)
                    pygame.display.update()
                algorithm_running = False
            pygame.display.flip()
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
path = './input/level_1/input2.txt'
alg =astar.astar_heuristic_1

run_visualization(path,alg)