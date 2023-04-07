from collections import deque

def bfs(queue):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    visited = set()
    global N, M
    while queue:
        rx, ry, bx, by, cnt = queue.popleft()
        if cnt == 10:
            return -1
        for d in delta:
            dx, dy = d
            nx, ny, nbx, nby = rx+dx, ry+dy, bx+dx, by+dy
            #R 이동
            while board[nx][ny] == '.':
                nx, ny = nx+dx, ny+dy
            #B 이동
            while board[nbx][nby] not in ['#', 'O']:
                nbx, nby = nbx+dx, nby+dy

            if board[nbx][nby] == 'O':
                continue
            if board[nx][ny] == 'O':
                return cnt+1

            if (nx, ny) == (nbx, nby):
                if dx == 0:
                    if abs(ny-ry) > abs(nby-by):
                        ny -= dy
                    else:
                        nby -= dy
                else:
                    if abs(nx-rx) > abs(nbx-bx):
                        nx -= dx
                    else:
                        nbx -= dx

            if (nx-dx, ny-dy, nbx-dx, nby-dy) not in visited:
                visited.add((nx-dx, ny-dy, nbx-dx, nby-dy))
                queue.append((nx-dx, ny-dy, nbx-dx, nby-dy, cnt+1))

    #queue에 더이상 원소가 존재하지 않은 경우 구멍을 통해 빠져나갈 수 없는 것이므로 -1 return
    return -1

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

board[rx][ry] = '.'
board[bx][by] = '.'

queue = deque([(rx, ry, bx, by, 0)])
result = bfs(queue)
print(result)