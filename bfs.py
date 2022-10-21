
from asyncio.windows_events import NULL


def isValid(MAZE,cell):
    row=len(MAZE)
    col =len(MAZE[0])
    x=cell[0]
    y=cell[1]
    if x<0 or y<0 or x>=col or y>=col or MAZE[x][y]=='x':
        return False
    return True

def bfs(MAZE,bonus=NULL):
    start = ()
    goal = () 
    solution = []
    visited = {}
    vis=[]
    queue = []
    dx=[-1, 0, 1, 0, -1]
    cntNode=0
    cost=-1
    for row in range(len(MAZE)):
        for col in range(len(MAZE[row])):
            if MAZE[row][col] == 'S':
                start = (row, col)
            if row == 0 or row == len(MAZE) - 1 or col == 0 or col == len(MAZE[row]) - 1:
                if MAZE[row][col] == ' ':
                    goal = (row, col)
    queue.append(start)
    visited[start]=(-1,-1)
    vis.append(start)
    while len(queue) > 0:
        (x, y) = queue.pop(0)
        cntNode+=1
        if (x,y) == goal:
            backtrack_node = goal
            solution.insert(0,backtrack_node)
            while backtrack_node != start:
                backtrack_node = visited[backtrack_node]
                solution.insert(0,backtrack_node)
            cost+=len(solution)
            
            return start,goal,visited,solution,cntNode,cost   
      
        for i in range(4):
            newX=x+dx[i]
            newY=y+dx[i+1]
            if isValid(MAZE,(newX,newY)) and (newX,newY) not in visited:
                queue.append((newX,newY))
                visited[(newX, newY)]=(x,y)
                
    print(bfs.__name__+" warning: No solution found!")
    return start,goal,visited,solution,cntNode,cost


