from collections import deque
import copy
def combination(arr, r):    #바이러스들 중 m개를 고르는 함수
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:], r-1):
                yield [arr[i]] + next

def bfs(board, queue):  #바이러스 퍼뜨리는 함수
    global N
    delta = [(-1,0), (1,0), (0,-1), (0,1)]
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if board[nx][ny] == 0:
                cnt = int(board[x][y]) + 1
                board[nx][ny] = cnt
                queue.append((nx,ny))
            elif board[nx][ny] == '*':  #비활성 바이러스인 경우
                board[nx][ny] = int(board[x][y]) + 1
                queue.append((nx,ny))
    if check(board):
        return cnt
    else:
        return "False"
def check(board):   #빈 칸이 남아있는지 확인하는 함수
    for arr in board:
        if 0 in arr:
            return False
    return True

N, M = map(int, input().split())
board, virus = [], []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] == 1:
            board[i][j] = '-'
        elif board[i][j] == 2:
            board[i][j] = '*'   #비활성 바이러스
            virus.append((i,j))

run_virus = combination(virus, M)
minimum = 1e9
for v in run_virus:
    new_board = copy.deepcopy(board)
    queue = deque()
    for x,y in v:
        new_board[x][y] = '0'
        queue.append((x,y))
    t = bfs(new_board, queue)
    if t == "False":    #빈칸이 남아있으면 바이러스를 다 퍼뜨리지 못한 것이므로 pass
        pass
    else:
        minimum = min(t, minimum)
if minimum == 1e9:  #모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우
    print(-1)
else:
    print(minimum)