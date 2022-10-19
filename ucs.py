from dis import dis
import queue
MAX= 100
INF = int(1e9)

class Node:
    def __init__(self,cell,dist) :
        self.cell=cell
        self.dist=dist
    
    def __lt__(self,other):
        return self.dist<=other.dist



def isValid(MAZE,cell):
    row=len(MAZE)
    col =len(MAZE[0])
    x=cell[0]
    y=cell[1]
    if x<0 or y<0 or x>=col or y>=col or MAZE[x][y]=='x':
        return False
    return True

def ucs(MAZE):
    start = ()
    goal = () 
    solution = []
    visited = {}
    pq = queue.PriorityQueue()
    dx=[-1, 0, 1, 0, -1]
    cost=0
    for row in range(len(MAZE)):
        for col in range(len(MAZE[row])):
            if MAZE[row][col] == 'S':
                start = (row, col)
            if row == 0 or row == len(MAZE) - 1 or col == 0 or col == len(MAZE[row]) - 1:
                if MAZE[row][col] == ' ':
                    goal = (row, col)
    pq.put(Node(start,0))
    visited[start]=start
    while not pq.empty():
        node =  pq.get()
        # print(node.cell)
        (x,y)=node.cell
        dist=node.dist
        if (x,y) == goal:
            print('Solution found')
            backtrack_node = goal
            solution.insert(0,backtrack_node)
            while backtrack_node != start:
                backtrack_node = visited[backtrack_node]
                solution.insert(0,backtrack_node)
            return start,goal,visited,solution,cost     
      
        for i in range(4):
            newX=x+dx[i]
            newY=y+dx[i+1]
            if isValid(MAZE,(newX,newY)) and (newX,newY) not in visited:
                pq.put(Node((newX,newY),dist+1))
                visited[(newX, newY)]=(x,y)
                cost+=1
    return start,goal,visited,solution,-1 


