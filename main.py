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


input_path = './input/level_2/'
fileList=sorted(glob.glob(os.path.join(input_path, '*.txt')))


# for filename in fileList :
#     intputName=Path(filename).stem
#     bonus_points, matrix = IO.read_file(filename)
#     for alg in algList:
#         out= alg(matrix)
#         sol=out[3]
#         pcost=out[4]
#         cost = len(sol)
#         print(alg.__name__+" "+intputName+ " sol cost: "+str(cost) + " process cost: "+str(pcost))
#         costPath=IO.visualize_maze(matrix,bonus_points,intputName,alg.__name__,sol)
#         with open(costPath, 'w') as costFile:
#             costFile.write(str(cost))

import alg1
p='./input/level_2/input3.txt'
bonus_points, matrix = IO.read_file(p)
intputName=Path(p).stem
al=alg1.ALG_heuristic_2
bonus=list(bonus_points.keys())
out= al(matrix,bonus_points)
sol=out[3]
# print(bonus)
# print(bonus_points)
costPath=IO.visualize_maze(matrix,bonus,intputName,al.__name__,sol)
    # sol=out[3]
    # cost=out[4]
    # costPath=IO.visualize_maze(matrix,bonus_points,intputName,al.__name__,sol)
    # with open(costPath, 'w') as costFile:
    #     costFile.write(str(cost))
