import ast
import os
import re
import matplotlib.pyplot as plt

gbfs_rg=r'^(gbfs)'
astar_rg=r'^(astar)'


def visualize_maze(matrix, bonus,nameIn='input',nameOut='output',route=None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=(i,j)

            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)
                    
            else:
                pass
    #1. Define walls and array of direction based on the route
    walls=[(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j]=='x']

    if route:
        direction=[]
        for i in range(1,len(route)):
            if route[i][0]-route[i-1][0]>0:
                direction.append('v') #^
            elif route[i][0]-route[i-1][0]<0:
                direction.append('^') #v        
            elif route[i][1]-route[i-1][1]>0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    #2. Drawing the map
    ax=plt.figure(dpi=200).add_subplot(111)

    for i in ['top','bottom','right','left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls],[-i[0] for i in walls],
                marker='X',s=40,color='black')
    
    plt.scatter([i[1] for i in bonus],[-i[0] for i in bonus],
                marker='P',s=100,color='green')

    plt.scatter(start[1],-start[0],marker='*',
                s=50,color='gold')

    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1][1],-route[i+1][0],
                        marker=direction[i],color='#20B2AA')

    plt.text(end[1],-end[0],'EXIT',color='red',
         horizontalalignment='center',
         verticalalignment='center',size =7, rotation=-90,fontweight='bold')
    plt.xticks([])
    plt.yticks([])

    if re.match(gbfs_rg, nameOut):
        path='./output/'+nameIn+'/gbfs/'
    elif re.match(astar_rg, nameOut):
        path='./output/'+nameIn+'/astar/'
    else:
        path='./output/'+nameIn+'/'+nameOut+'/'
    if not os.path.exists(path):
        os.makedirs(path)
    fileName=path+nameOut
    plt.savefig(fileName)
    plt.close()
   

    for _, point in enumerate(bonus):
      print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')
    
    return fileName


def read_file(file_name: str = './input/level_1/input1.txt'):
        f=open(file_name,'r')
        n_bonus_points = int(next(f)[:-1])
        bonus_points = []
        for i in range(n_bonus_points):
            x, y, reward = map(int, next(f)[:-1].split(' '))
            bonus_points.append((x, y, reward))

        text=f.read()
        matrix=[list(i) for i in text.splitlines()]
        f.close()

        return bonus_points, matrix





