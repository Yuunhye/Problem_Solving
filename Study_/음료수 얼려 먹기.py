N , M = map(int, input().split())   #N행 M열
ice = [list(map(int, input())) for i in range(N)]

def dfs(arr, row, col) :
    arr[row][col] = -1  #해당 위치 방문 처리
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(4) : #상하좌우 방문처리
        y = row + dy[i] #행
        x = col + dx[i] #열
        if x<0 or y<0 or x>=M or y>=N :
            continue
        if arr[y][x] == 0 :
            dfs(arr,y,x)
    return 1

count = 0
for i in range(N) :
    while (0 in ice[i]) :
        count += dfs(ice, i, ice[i].index(0))
print(count)

#풀이
"""
#DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y) :
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=N or y<=-1 or y>=M :
        return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0 :
        #해당 노드 방문 처리
        graph[x][y] = 1
        #상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


N , M = map(int, input().split())
graph = [list(map(int, input())) for i in range(N)]

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(N) :
    for j in range(M) :
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True :
            result += 1
print(result)
"""