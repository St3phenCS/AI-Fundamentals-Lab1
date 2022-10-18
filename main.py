from hashlib import algorithms_available
import bfs
import dfs
import pygame
import time
import sys
#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 172, 28)
DARK_ORANGE = (139, 64, 0)
GRAY = (128, 128, 128)

MAZE = []

#inputMaze = input("Choose maze (1, 2, 3, 4, 5):")
MAZE_LIST = ['maze1','maze2','maze3', 'maze4', 'maze5']

directory = f"Input/{MAZE_LIST[0]}.txt"
with open(directory,'r') as inputFile:
    n = inputFile.readline()
    for line in inputFile:
        MAZE.append(line.rstrip())




#Init pygame
WIDTH = 1000 #screen width
HEIGHT = 500 #screen height
SCREEN_SIZE = [WIDTH, HEIGHT]
TILE = int(HEIGHT/len(MAZE)) #size of each tile
FPS = 60
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE) #set screen size
pygame.display.set_caption("Maze Solver") #set caption


def MazeInitialize(MAZE):
    for row in range(len(MAZE)):
        for col in range(len(MAZE[row])):
            if MAZE[row][col] == 'x':
                pygame.draw.rect(screen, DARK_ORANGE, (col * TILE, row * TILE, TILE, TILE))
                pygame.draw.rect(screen, ORANGE, (col * TILE, row * TILE, TILE - 2, TILE - 2))

            if MAZE[row][col] == 'S':
                pygame.draw.rect(screen, RED, (col * TILE, row * TILE, TILE, TILE))
            if MAZE[row][col] == ' ':
                pygame.draw.rect(screen, WHITE, (col * TILE, row * TILE, TILE, TILE))
            if (row, col) == bfs.goal:
                pygame.draw.rect(screen, GREEN, (col * TILE, row * TILE, TILE, TILE))


def draw_window():
    MazeInitialize(MAZE)


def main(alg,):
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
            # bfs.BFS(MAZE, screen, TILE)
            #dfs.DFS(MAZE, screen, TILE)
            alg(MAZE, screen, TILE)
            algorithm_running = False
            pygame.time.wait(1000)
            # input()
        else:
            pygame.quit()
            sys.exit()

main(bfs.BFS)