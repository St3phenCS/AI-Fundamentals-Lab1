import queue
import heuristics as heu

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

def AStar(MAZE,heuristic):
    start = ()
    goal = () 
    solution = []
    visited = {}
    dist={}
    pq = queue.PriorityQueue()
    dx=[-1, 0, 1, 0, -1]
    cntNode=-1
    cost=-1
    VIS=[]
    for row in range(len(MAZE)):
        for col in range(len(MAZE[row])):
            if MAZE[row][col] == 'S':
                start = (row, col)
            if row == 0 or row == len(MAZE) - 1 or col == 0 or col == len(MAZE[row]) - 1:
                if MAZE[row][col] == ' ':
                    goal = (row, col)
    pq.put(Node(start))
    visited[start]=(-1,-1)
    dist[start]=0;
    while not pq.empty():
        node =  pq.get()
        (x,y)=node.cell
        cntNode+=1
        VIS.append(node.cell)
        if (x,y) == goal:
            backtrack_node = goal
            solution.insert(0,backtrack_node)
            while backtrack_node != start:
                backtrack_node = visited[backtrack_node]
                solution.insert(0,backtrack_node)
            cost+=len(solution)
            return start,goal,VIS,solution,cntNode,cost      
      
        for i in range(4):
            newX=x+dx[i]
            newY=y+dx[i+1]
            if isValid(MAZE,(newX,newY)) and ((newX,newY) not in visited or dist[(newX,newY)]>dist[(x,y)]+1):
                g=dist[(x,y)]+1
                dist[(newX,newY)]=g
                h=heuristic((newX,newY),goal)
                newNode=Node((newX,newY),g+h)
                pq.put(newNode)
                visited[(newX, newY)]=(x,y)
                
    print(AStar.__name__+" warning: No solution found!")
    return start,goal,visited,solution,cntNode,cost


def astar_heuristic_1(MAZE,bonus=None):
    return AStar(MAZE,heu.Euclid)

def astar_heuristic_2(MAZE,bonus=None):
    return AStar(MAZE,heu.Mahattan)


#astar algrithm find path between source(src) and destination(dst) with simplified output 
def findPath(MAZE,src,dst,heu):
    start = src
    goal = dst 
    solution = []
    visited = {}
    dist={}
    pq = queue.PriorityQueue()
    dx=[-1, 0, 1, 0, -1]
    cost=0
    pq.put(Node(start))
    visited[start]=start
    dist[start]=0;
    while not pq.empty():
        node =  pq.get()
        (x,y)=node.cell
        w=node.w
        if (x,y) == goal:
            backtrack_node = goal
            while backtrack_node != start:
                solution.insert(0,backtrack_node)
                backtrack_node = visited[backtrack_node]
            return solution      
        for i in range(4):
            newX=x+dx[i]
            newY=y+dx[i+1]
            if isValid(MAZE,(newX,newY)) and ((newX,newY) not in visited or dist[(newX,newY)]>dist[(x,y)]+1):
                g=dist[(x,y)]+1
                dist[(newX,newY)]=g
                h=heu((newX,newY),goal)
                newNode=Node((newX,newY),g+h)
                pq.put(newNode)
                visited[(newX, newY)]=(x,y)
                cost+=1
    print(findPath.__name__+" warning: No solution found!")
    return solution

