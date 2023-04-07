from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split()) #d : 0(북쪽), 1(동쪽), 2(남쪽), 3(서쪽)
board = [list(map(int, input().split())) for x in range(N)]

dir = [0,1,2,3] #반시계 방향으로 회전: -1
dir_move = [[(-1,0),(1,0)], [(0,1),(0,-1)], [(1,0),(-1,0)], [(0,-1),(0,1)]]  #방향 : 전진, 후진

x, y = r, c
delta = [(-1,0), (1,0), (0,-1), (0,1)]  #상하좌우
cnt = 0
while (1) :
    flag = False
    if board[x][y] == 0:    #현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
        cnt += 1
        board[x][y] = -1
    for i in delta:
        dx, dy = i
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if board[nx][ny] == 0:
            flag = True
            d = dir[d-1]
            ndx, ndy = dir_move[d][0]
            if 0 <= x+ndx < N and 0 <= y+ndy < M and board[x+ndx][y+ndy] == 0:
                x, y = x+ndx, y+ndy
                break
    if not flag:
        ndx, ndy = dir_move[d][1]
        if 0 <= x+ndx < N and 0 <= y+ndy < M and board[x+ndx][y+ndy] in [-1, 0]:
            x, y = x+ndx, y+ndy
        else:
            break

print(cnt)