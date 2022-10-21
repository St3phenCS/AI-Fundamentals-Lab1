import os,glob
from pathlib import Path
import processIO as IO

import bfs as bfs
import dfs as dfs
import ucs as ucs
import greedy as gbfs
import astar as astar
import advanceAlg as adv






algList={}
algs1=[]
algs2=[]
algs1.append(bfs.bfs)
algs1.append(dfs.dfs)
algs1.append(ucs.ucs)
algs1.append(gbfs.gbfs_heuristic_1)
algs1.append(gbfs.gbfs_heuristic_2)
algs1.append(astar.astar_heuristic_1)
algs1.append(astar.astar_heuristic_2)

algs2.append(adv.algo1)

algList['level_1']=algs1
algList['level_2']=algs2

inputFolders=[]
inputFolders.append('level_1')
inputFolders.append('level_2')

for lvl in inputFolders:
    input_path = './input/{}/'.format(lvl)
    fileList=sorted(glob.glob(os.path.join(input_path, '*.txt')))
   
    for inPath in fileList :
        print('\n')
        inName=Path(inPath).stem
        folPath='./output/'+lvl+'/'+inName+'/'
        # print(folPath)
        bonus_points, matrix = IO.read_file(inPath)
        for alg in algList[lvl]:
            bonus=list(bonus_points.keys())
            out= alg(matrix,bonus_points)
            sol=out[3]
            pcost=out[4]
            cost = out[5]
            print(alg.__name__+" "+inName+ " sol cost: "+str(cost) + " process cost: "+str(pcost))
            textFile=IO.write_output(matrix,bonus,sol,folPath,alg.__name__)
            with open(textFile, 'w') as outFile:
                if len(sol)>0:
                    outFile.write(str(cost))
                else:
                    outFile.write(str('NO'))


# p='./input/level_1/input2.txt'
# bonus_points, matrix = IO.read_file(p)
# intputName=Path(p).stem
# al=adv.algo1
# bonus=list(bonus_points.keys())
# out= al(matrix,bonus_points)
# sol=out[3]
# costPath=IO.write_output(matrix,bonus,sol)

