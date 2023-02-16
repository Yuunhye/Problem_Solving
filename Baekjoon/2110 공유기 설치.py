import sys
input = sys.stdin.readline
N,C = map(int, input().split())
X = list()
for _ in range(N) :
    X.append(int(input()))

X.sort()    #좌표 정렬
Max = X[-1] - X[0]  #가장 인접한 두 공유기 사이의 거리의 최댓값
Min = 1     #가장 인접한 두 공유기 사이의 거리의 최솟값
while(Min <= Max) :
    M = (Max+Min)//2
    val = X[0]+M
    count = 1
    for i in range(1,N) : #가장 인접한 두 공유기 사이의 거리를 M이라고 할 때, 공유기를 놓을 수 있는 좌표의 수를 구한다. 
        if X[i] >= val :
            val = X[i]+M
            count += 1
    #공유기를 놓을 수 있는 좌표의 총 개수가 공유기의 개수보다 큰 경우에는 M의 값이 더 커져야 하므로 M의 최솟값을 1 증가시켜주고 
    #좌표의 개수가 공유기의 개수보다 작은 경우에는 M의 값을 줄여야 하므로 M의 최댓값을 1 감소시켜준다.
    #좌표의 개수와 공유기의 개수가 같으면 그 때의 M값이 M의 최댓값인지 알 수 없으므로 M의 값을 키워서 더 확인해본다.
    if count >= C : 
        M_max = M
        Min = M+1
    else :
        Max = M-1
print(M_max)