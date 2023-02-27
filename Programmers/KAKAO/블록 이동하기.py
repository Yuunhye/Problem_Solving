from collections import deque

def move(x1,y1,x2,y2,board) :
    res = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    #상하좌우 이동
    for i in range(4) :
        nx1, nx2, ny1, ny2 = x1+dx[i], x2+dx[i], y1+dy[i], y2+dy[i]
        if all(0<=k<N for k in (nx1,ny1,nx2,ny2)) and board[nx1][ny1] ==0 and board[nx2][ny2] == 0 :
            res.append((nx1,ny1,nx2,ny2))
    
    #회전
    if x1 == x2 :   #가로인 경우
        if 0<=x1+1<N and board[x1+1][y1] == 0 and board[x2+1][y2] == 0 :  #아래로 회전 가능
            res.append((x1,y1,x1+1,y1))   #시계 방향으로 회전
            res.append((x2,y2,x2+1,y2))   #반시계 방향으로 회전
        if 0<=x1-1<N and board[x1-1][y1] == 0 and board[x2-1][y2] == 0 :  #위로 회전 가능
            res.append((x2-1,y2,x2,y2))   #시계 방향으로 회전
            res.append((x1-1,y1,x1,y1))   #반시계 방향으로 회전
    else :  #세로인 경우
        if 0<=y1+1<N and board[x1][y1+1] == 0 and board[x2][y2+1] == 0 :    #오른쪽으로 회전
            res.append((x2,y2,x2,y2+1)) #시계 방향으로 회전
            res.append((x1,y1,x1,y1+1)) #반시계 방향으로 회전
        if 0<=y1-1<N and board[x1][y1-1] == 0 and board[x2][y2-1] == 0 :    #왼쪽으로 회전
            res.append((x1,y1-1,x1,y1)) #시계 방향으로 회전
            res.append((x2,y2-1,x2,y2)) #반시계 방향으로 회전
    return res
            
def solution(board):
    global N
    N = len(board)
    
    #bfs
    queue = deque([((0,0,0,1),0)])    #처음 로봇의 좌표 : (0,0),(0,1)
    visited = []
    while queue :
        robot_pos, t = queue.popleft()
        x1,y1,x2,y2 = robot_pos
        if (x1,y1) == (N-1,N-1) or (x2,y2) == (N-1,N-1) :
            break
        for pos in move(x1,y1,x2,y2,board) :
            if pos not in visited :
                queue.append((pos,t+1))
                visited.append(pos)
    return t