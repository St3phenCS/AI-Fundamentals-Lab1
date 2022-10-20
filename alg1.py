import queue
import heuristics as h

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

def ALG1(MAZE,heuristic,bonus):
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
    pq.put(Node(start))
    visited[start]=start
    while not pq.empty():
        node =  pq.get()
        current=node.coord
        isBonus=False
        w=node.w
        if current == goal:
            print('Solution found')
            backtrack_node = goal
            solution.insert(0,backtrack_node)
            while backtrack_node != start:
                backtrack_node = visited[backtrack_node]
                solution.insert(0,backtrack_node)
            # tmp =len(solution)-1;
            # for b in bonus:
                
            #     bp=(b[0],b[1])
            #     if bp in solution:
            #         tmp+=b[2]
            # print("cost: ",tmp)
            return start,goal,visited,solution,cost     
            
        if node.coord in bonus:
                bonus.pop(node.coord)
                w=-1000
                isBonus=True
        for i in range(4):
            newX=current[0]+dx[i]
            newY=current[1]+dx[i+1]
            nextPoint=(newX,newY)
            
            
            if isValid(MAZE,nextPoint) and nextPoint not in visited:
                h=heuristic(nextPoint,goal)
                for bPoint,bCost in bonus.items():
                    if bPoint not in visited:
                        tmp1=heuristic(nextPoint,bPoint)
                        # if node == bPoint:
                        #     tmp1=0
                        tmpCost =tmp1+ heuristic(bPoint,goal)+bCost
                        if tmpCost<=h:
                            h=tmpCost
                   
                    
                    
                

                newNode=Node((newX,newY),h+w)
                pq.put(newNode)
                visited[(newX, newY)]=current
                cost+=1

            
        # print(current)
        # print(node in bonus)
        
    return start,goal,visited,solution,-1 


def ALG_heuristic_1(MAZE,bonus):
    return ALG1(MAZE,h.Euclid,bonus)


# def gbfs_heuristic_2(MAZE):
#     return GreedyBFS(MAZE,h.Mahattan)