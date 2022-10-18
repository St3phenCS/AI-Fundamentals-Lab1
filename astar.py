import queue
MAX= 100
INF = int(1e9)

class Node:
    def __init__(self,cell,w=0) :
        self.cell=cell
        self.w=w
    
    def __lt__(self,other):
        return self.w<=other.w



def isValid(MAZE,cell):
    row=len(MAZE)
    col =len(MAZE[0])
    x=cell[0]
    y=cell[1]
    if x<0 or y<0 or x>=col or y>=col or MAZE[x][y]=='x':
        return False
    return True

def AStart(MAZE,heuristic):
    start = ()
    goal = () 
    solution = []
    visited = {}
    dist={}
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
    pq.put(Node(start))
    visited[start]=start
    dist[start]=0;
    while not pq.empty():
        node =  pq.get()
        (x,y)=node.cell
        w=node.w
        if (x,y) == goal:
            print('Solution found')
            backtrack_node = goal
            solution.insert(0,backtrack_node)
            while backtrack_node != start:
                backtrack_node = visited[backtrack_node]
                solution.insert(0,backtrack_node)
            return solution,cost    
      
        for i in range(4):
            newX=x+dx[i]
            newY=y+dx[i+1]
            if isValid(MAZE,(newX,newY)) and (newX,newY) not in visited:
                g=dist[(x,y)]+1
                dist[(newX,newY)]=g
                h=heuristic((newX,newY),goal)
                newNode=Node((newX,newY),g+h)
                pq.put(newNode)
                visited[(newX, newY)]=(x,y)
                cost+=1
    return solution,-1

