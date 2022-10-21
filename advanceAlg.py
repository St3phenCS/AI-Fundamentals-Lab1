import ast
import queue
import heuristics as h
import astar
class Node:
    def __init__(self,coord,w=0) :
        self.coord=coord
        self.w=w
    
    def __lt__(self,other):
        return self.w<=other.w
def isValid(MAZE,coord):
    row=len(MAZE)
    col =len(MAZE[0])
    x=coord[0]
    y=coord[1]
    if x<0 or y<0 or x>=col or y>=col or MAZE[x][y]=='x':
        return False
    return True

def ALG(MAZE,heuristic,bonus):
    start = ()
    goal = () 
    solution = []
    visited = {}
    pq = queue.PriorityQueue()
    dx=[-1, 0, 1, 0, -1]
    cntNode=0
    cost =-1
    importantPoints=[]
    for row in range(len(MAZE)):
        for col in range(len(MAZE[row])):
            if MAZE[row][col] == 'S':
                start = (row, col)
            if row == 0 or row == len(MAZE) - 1 or col == 0 or col == len(MAZE[row]) - 1:
                if MAZE[row][col] == ' ':
                    goal = (row, col)
    pq.put(Node(start))
    visited[start]=start
    importantPoints.append(start)
    while not pq.empty():
        node =  pq.get()
        currPoint=node.coord
        w=node.w
        cntNode+=1
        if currPoint == goal:
            importantPoints.append(goal)
            src=importantPoints.pop(0)
            while len(importantPoints)>0:
                dst=importantPoints.pop(0)
                subSol=astar.findPath(MAZE,src,dst,heuristic)
                solution+=subSol
                src=dst
           
            solution.insert(0,start)   
            cost+=len(solution)   
            return start,goal,visited,solution,cntNode,cost       
        if currPoint in bonus:
                cost+=bonus[currPoint]
                cntNode-=bonus[currPoint]
                bonus.pop(currPoint)
                importantPoints.append(currPoint)
                
        for i in range(4):
            newX=currPoint[0]+dx[i]
            newY=currPoint[1]+dx[i+1]
            nextPoint=(newX,newY)
            if isValid(MAZE,nextPoint) and nextPoint not in visited:
                h=heuristic(nextPoint,goal)
                for bPoint,bCost in bonus.items():
                    tmpCost =heuristic(nextPoint,bPoint)+ heuristic(bPoint,goal)+bCost
                    if tmpCost<=h:
                        h=tmpCost
                        
                newNode=Node((newX,newY),h+w)
                pq.put(newNode)
                visited[(newX, newY)]=currPoint
                
    print(ALG.__name__+" warning: No solution found!")
    return start,goal,visited,solution,cntNode,cost 


def algo1(MAZE,bonus):
    return ALG(MAZE,h.Euclid,bonus)

# def ALG_heuristic_2(MAZE,bonus):
#     return ALG(MAZE,h.Mahattan,bonus)


