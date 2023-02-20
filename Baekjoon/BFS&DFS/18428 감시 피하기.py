#모든 학생들이 감시를 피할 수 있는지 확인하는 함수. 감시를 피할 수 있으면 True, 아니면 False 리턴
def check(arr, teacher) :
    dx = [1,-1,0,0] #상하좌우
    dy = [0,0,1,-1]
    for (x,y) in teacher :
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
						#선생님의 위치에서 각 방향의 끝에 도달할 때까지 확인
            while 0<=nx<N and 0<=ny<N : 
                if arr[nx][ny] == 'O' :
                    break
                if arr[nx][ny] == 'S' :
                    return False
                nx += dx[i]  #같은 방향으로 계속 확인해본다.
                ny += dy[i]
    
    return True

import copy
from itertools import combinations
N = int(input())
info = [list(map(str, input().split())) for i in range(N)]

teacher, pos = [],[]
for i in range(N) :
    for j in range(N) :
        if info[i][j] == 'T' :
            teacher.append((i,j))
        elif info[i][j] == 'X' :
            pos.append((i,j))
wall = list(combinations(pos, 3))  #장애물을 놔둘 수 있는 좌표 조합
res = "NO"

while wall :
    arr = copy.deepcopy(info)  #복도의 정보 deep copy
    wall_pos = wall.pop()
    for (i,j) in wall_pos :    #장애물 설치
        arr[i][j] = 'O'
    if check(arr,teacher) :
        res = "YES"
        break
print(res)