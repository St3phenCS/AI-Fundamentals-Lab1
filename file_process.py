# with open('maze_map.txt', 'w') as outfile:
#   outfile.write('0\n')
#   outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
#   outfile.write('x   x   xx xx        x\n')
#   outfile.write('x     x     xxxxxxxxxx\n')
#   outfile.write('x x   xxx  xxxx xxx xx\n')
#   outfile.write('  x   x x xx   xxxx  x\n')
#   outfile.write('x          xx xxx  x x\n')
#   outfile.write('xxxxxxx x      xx  x x\n')
#   outfile.write('xxxxxxxxx  x x  xx   x\n')
#   outfile.write('x          x x Sx x  x\n')
#   outfile.write('xxxxx x  x x x     x x\n')
#   outfile.write('xxxxxxxxxxxxxxxxxxxxxx')

import os
import matplotlib.pyplot as plt

def visualize_maze(matrix, bonus, start, end, route=None,output='output'):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
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
    ax=plt.figure(dpi=300).add_subplot(111)

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
    plt.savefig(output)
    # plt.show()

    # print(f'Starting point (x, y) = {start[0], start[1]}')
    # print(f'Ending point (x, y) = {end[0], end[1]}')
    
    for _, point in enumerate(bonus):
      print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')


def read_file(file_name: str = 'maze_map.txt'):
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


bonus_points, matrix = read_file('./input/maze1.txt')
# bonus_points, matrix = read_file('maze_map.txt')

# print(f'The height of the matrix: {len(matrix)}')
# print(f'The width of the matrix: {len(matrix[0])}')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]=='S':
            start=(i,j)

        elif matrix[i][j]==' ':
            if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                end=(i,j)
                
        else:
            pass

import dfs
import bfs
import ucs
sol1,cost1 = dfs.DFS(matrix)
print("DFS: ",cost1)
visualize_maze(matrix,bonus_points,start,end,sol1,"dfs")

# sol2,cost2=bfs.BFS(matrix)
# print("BSF: ",cost2)
# visualize_maze(matrix,bonus_points,start,end,sol2)

sol3,cost3=ucs.UCS(matrix)
print("UCS: ",cost3)
visualize_maze(matrix,bonus_points,start,end,sol3,"ucs")

#test push
