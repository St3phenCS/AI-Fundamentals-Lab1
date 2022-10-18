
import queue
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
MAX = 35
visited = [[False] * MAX for _ in range(MAX)]
maze = [None] * MAX

class Cell:
    def __init__(self, _r, _c):
        self.r = _r
        self.c = _c

def isValid(r, c):
    return r in range(H) and c in range(W)

def BFS(s):
    q = queue.Queue()
    q.put(s)
    visited[s.r][s.c] = True
    count = 1

    while not q.empty():
        u = q.get()

        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]

            if isValid(r, c) and maze[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r, c))
                count += 1
    
    return count

Q = int(input())

for k in range(1, Q + 1):
    W, H = map(int, input().split())

    for i in range(H):
        maze[i] = input()
    
    for i in range(H):    
        for j in range(W):
            if maze[i][j] == '@':
                s = Cell(i, j)
            visited[i][j] = False

    print("Case {}: {}".format(k, BFS(s)))