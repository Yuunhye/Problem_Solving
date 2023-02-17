N,C = map(int, input().split())
X = [int(x) for x in input().split()]
X.sort()    #좌표 정렬
Min,Max = 1, X[-1]-X[0]  # 1<=M<=(Xn-X1)
while(Min<=Max) :
    M = (Max+Min)//2    #가장 가까운 두 말의 거리 : M
    val = X[0] + M
    count = 1
    for i in range(1,N) :
        if X[i] >= val :
            val = X[i] + M
            count += 1
    
    if count >= C :
        Min = M+1
        ans = M
    else :  #count < C
        Max = M-1
print(ans)