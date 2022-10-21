import pygame
import sys,os
import processIO as IO
from pathlib import Path

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
CHEEMSG=None
BANANAS=None
#Init pygame
WIDTH = 1440 #screen width
HEIGHT = 600 #screen height
SCREEN_SIZE = [WIDTH, HEIGHT]
TILE = 0 #size of each tile
FPS = 60








def MazeInitialize(MAZE):
    cnt =0;
    bana=[]
    bns=[]
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
                bns.append((row,col))
                
            if MAZE[row][col] == 'b':
                bana.append((row,col))
                pygame.draw.rect(screen, GOODBLUE, (col * TILE, row * TILE, TILE, TILE))
    for cell in bns:
        screen.blit(CHEEMSG,(cell[1] * TILE, cell[0] * TILE))          
    for cell in bana:
        screen.blit(BANANAS,(cell[1] * TILE, cell[0] * TILE))
               

def draw_window():
    MazeInitialize(MAZE)


def run_visualization(pathIn,alg):
    
    global MAZE ,BONUS,VIS,SOL,SRC,DST,ALGNAME,screen,TILE,CHEEMSG,BANANAS
    BONUS,MAZE=IO.read_file(pathIn)
    if len(MAZE) >= 40 or len(MAZE[0]) >= 80:
        TILE = 18
    else: 
        TILE = 20
    WIDTH = TILE*len(MAZE[0])  # screen width
    HEIGHT = TILE*len(MAZE)  # screen height
    SCREEN_SIZE = [WIDTH, HEIGHT]
    B= list(BONUS.keys())
    out = alg(MAZE,BONUS)
    # VIS=list(out[2].keys())
    VIS=out[2]
    SOL=out[3]
    SRC=out[0]
    DST=out[1]
    # print(len(VIS))
    if len(SOL)>0:
        SOL.pop(0)
    else:
        print("Visualization warning: No solution found!")
    TILE=int(HEIGHT/len(MAZE))
    ALGNAME=alg.__name__.upper()
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE) #set screen size
    pygame.display.set_caption("VISUALIZATION {}".format(ALGNAME)) #set caption

    CHEEMSG=pygame.image.load("./img/gcheems.png").convert_alpha()
    CHEEMSG = pygame.transform.scale(CHEEMSG, (TILE*1.2, TILE*1.2))
    
    BANANAS=pygame.image.load("./img/banana.png").convert_alpha()
    BANANAS=pygame.transform.scale(BANANAS, (TILE, TILE))

    screen.fill((255,255,255))
    algorithm_running = True
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
                # print(current)
                if current in B :
                    tmp[y]='b' #visited bonus
                    # screen.blit(CHEEMSG,(y * TILE,x * TILE))
                MAZE[x] = ''.join(tmp)
                pygame.draw.rect(screen, BLUE, (y * TILE, x * TILE, TILE, TILE))
                pygame.time.wait(30)
                pygame.display.update()
            else:              
                for node in SOL:
                    
                    pygame.draw.rect(screen, GREEN, (node[1] * TILE, node[0] * TILE, TILE, TILE))
                    if node in B:
                        screen.blit(BANANAS,(node[1] * TILE,node[0] * TILE))
                         
                        
                    pygame.time.wait(70)
                    pygame.display.update()
           
                pathIn=Path(pathIn).stem       
                if not os.path.exists('./visualize_img'):
                    os.makedirs('./visualize_img')
                pygame.image.save(screen, "./visualize_img/{}_{}.jpeg".format(ALGNAME,pathIn))
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
import advanceAlg as adv

# alg=adv.algo1
# alg=astar.astar_heuristic_1
# alg=gbfs.gbfs_heuristic_1

alg={}
alg["dfs"]=dfs.dfs
alg["bfs"]=bfs.bfs
alg["ucs"]=ucs.ucs
alg["gbfs1"]=gbfs.gbfs_heuristic_1
alg["gbfs2"]=gbfs.gbfs_heuristic_2
alg["astar1"]=astar.astar_heuristic_1
alg["astar2"]=astar.astar_heuristic_2
alg["adv"]=adv.algo1


if __name__ == "__main__":
    
    path = "./input/level_{0}/input{1}.txt".format(sys.argv[1],sys.argv[2])
    algName=sys.argv[3]
    print("Visualizing {} on input {}".format(algName,path))
    run_visualization(path,alg[algName])
   
   