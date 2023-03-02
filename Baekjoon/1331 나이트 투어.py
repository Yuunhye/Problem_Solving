#나이트의 현재 위치에서 갈 수 있는 위치를 모두 반환해주는 함수
def can_move(alpha, num) :
    res = []
    A = ['A','B','C','D','E','F']
    N = ['1','2','3','4','5','6']
    alpha_index = A.index(alpha)
    num_index = N.index(num)
    
    d = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    for x,y in d :
        if 0<=(x+alpha_index)<6 and 0<=(y+num_index)<6 :
            res.append(A[x+alpha_index] + N[y+num_index])
    return res

visited = set() #나이트가 이전에 방문했었는지 확인하기 위함
ans = "Valid"

start_pos = input() #시작점
alpha, num = start_pos  
visited.add(start_pos)
for i in range(35) :    
    nxt_pos = input()
    if nxt_pos in visited : #나이트가 이전에 방문했던 곳을 또 방문한 경우
        ans = "Invalid"
    elif nxt_pos not in can_move(alpha,num) : #나이트가 이동할 수 없는 위치로 이동한 경우
        ans = "Invalid"
    visited.add(nxt_pos)    
    alpha,num = nxt_pos

if start_pos not in can_move(alpha,num) :   #나이트가 마지막으로 방문한 칸에서 시작점으로 돌아올 수 없는 경우
    ans = "Invalid"

print(ans)