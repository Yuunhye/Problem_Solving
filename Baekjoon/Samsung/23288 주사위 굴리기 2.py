from collections import deque

def dice_move(d):
    if d == 0:  #북쪽으로 이동
        a, b = dice[0][0],dice[0][1]
        dice[0][0], dice[0][1] = dice[1][2], dice[1][0]
        dice[1][0], dice[1][2] = a, b
    elif d == 1:    #동쪽으로 이동
        a, b = dice[0][0], dice[0][1]
        dice[0][0], dice[0][1] = dice[1][3], dice[1][1],
        dice[1][1], dice[1][3] = a, b
    elif d == 2:    #남쪽으로 이동
        a, b = dice[0][0], dice[0][1]
        dice[0][0], dice[0][1] = dice[1][0], dice[1][2]
        dice[1][0], dice[1][2] = b, a
    else:
        a, b = dice[0][0], dice[0][1]
        dice[0][0], dice[0][1] = dice[1][1], dice[1][3],
        dice[1][1], dice[1][3] = b, a

def bfs(x, y, B):
    global N, M
    queue = deque([(x,y)])
    visited = {(x,y)}
    delta = [(-1,0), (1,0), (0,-1), (0,1)]
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in delta:
            dx, dy = i
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if (nx,ny) not in visited and board[nx][ny] == B:
                queue.append((nx,ny))
                visited.add((nx,ny))
                cnt += 1
    return cnt

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [0,1,2,3]  #[북, 동, 남, 서]. -1: 반시계 방향 회전, -3: 시계 방향 회전, -2: 반대 방향
dir_move = [(-1,0), (0,1), (1,0), (0,-1)]
dice = [[1,6],[2,3,5,4]]    #초기 주사위 형태. [[위, 아래][북, 동, 남, 서]]
d = 1   #초기 이동 방향 : 동쪽
x, y = 0, 0 #초기 주사위 위치
result = 0
for _ in range(K):
    dx, dy = dir_move[d]
    nx, ny = x+dx, y+dy
    if 0<=nx<N and 0<=ny<M: #이동 방향에 칸이 있는 경우
        dice_move(d)
    else:   #이동 방향에 칸이 없는 경우
        d = dir[d-2]
        dx, dy = dir_move[d]
        nx, ny = x+dx, y+dy
        dice_move(d)

    A, B = dice[0][1], board[nx][ny]
    if A > B:  # 이동 방향을 90도 시계 방향으로 회전
        d = dir[d - 3]
    elif A < B:  # 이동 방향을 90도 반시계 방향으로 회전
        d = dir[d - 1]

    #점수 구하기
    result += bfs(nx, ny, B) * B
    x,y = nx, ny
print(result)