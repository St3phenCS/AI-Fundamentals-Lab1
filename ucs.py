import queue
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

def ucs(MAZE,bonus=None):
    start = ()
    goal = () 
    solution = []
    visited = {}
    pq = queue.PriorityQueue()
    dx=[-1, 0, 1, 0, -1]
    cntNode=-1
    dist={}
    vis=[]
    cost=-1
    for row in range(len(MAZE)):
        for col in range(len(MAZE[row])):
            if MAZE[row][col] == 'S':
                start = (row, col)
            if row == 0 or row == len(MAZE) - 1 or col == 0 or col == len(MAZE[row]) - 1:
                if MAZE[row][col] == ' ':
                    goal = (row, col)
    pq.put(Node(start,0))
    # visited[start]=start
    vis.append(start)
    dist[start]=0
    while not pq.empty():
        node =  pq.get()
        # print(node.cell)
        (x,y)=node.cell
        cntNode+=1
        vis.append((x,y))
        if (x,y) == goal:
            backtrack_node = goal
            solution.insert(0,backtrack_node)
            while backtrack_node != start:
                backtrack_node = visited[backtrack_node]
                solution.insert(0,backtrack_node)
            cost+=len(solution)
            
            return start,goal,vis,solution,cntNode,cost     
      
        for i in range(4):
            newX=x+dx[i]
            newY=y+dx[i+1]
            # print(dist[(newX,newY)])
            if isValid(MAZE,(newX,newY)) and ((newX,newY) not in visited or (dist[(newX,newY)]>dist[(x,y)]+1)):
                g=dist[(x,y)]+1
                dist[(newX,newY)]=g
                newNode=Node((newX,newY),g)
                pq.put(newNode)
                visited[(newX, newY)]=(x,y)
                
    print(ucs.__name__+" warning: No solution found!")
    return start,goal,vis,solution,cntNode,cost 


