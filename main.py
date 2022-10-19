import os,glob
from pathlib import Path
import processIO as IO
import bfs
import dfs
import ucs
import heuristics as h
import greedy as gbfs
import astar

algList=[]
algList.append(bfs.bfs)
algList.append(dfs.dfs)
algList.append(ucs.ucs)
algList.append(gbfs.gbfs_heuristic_1)
algList.append(gbfs.gbfs_heuristic_2)
algList.append(astar.astar_heuristic_1)
algList.append(astar.astar_heuristic_2)


input_path = './input/level_1/'
fileList=sorted(glob.glob(os.path.join(input_path, '*.txt')))


for filename in fileList :
    intputName=Path(filename).stem
    bonus_points, matrix = IO.read_file(filename)
    for alg in algList:
        out= alg(matrix)
        sol=out[3]
        cost=out[4]
        costPath=IO.visualize_maze(matrix,bonus_points,intputName,alg.__name__,sol)
        with open(costPath, 'w') as costFile:
            costFile.write(str(cost))