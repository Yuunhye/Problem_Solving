import sys
input = sys.stdin.readline
N, M = map(int, input().split())
L = [int(x) for x in input().split()]
Min = 1         #DVD 크기의 최솟값
Max = sum(L)    #DVD 크기의 최댓값
while (Min <= Max) :
    mid = (Min+Max)//2  #DVD의 크기(녹화 가능한 길이)
    count, temp = 0, 0
    for x in L :
        temp += x
        if mid < temp :
            count += 1
            temp = x
    count += 1  #마지막 DVD 고려

    #M보다 더 적은 DVD가 나온 경우 DVD의 크기를 줄여야 한다.
    #M개의 DVD가 나온 경우 그때의 DVD의 크기가 최소인지 알 수 없으므로 DVD의 크기를 줄여서 확인해본다.
    if count <= M :   
        Max = mid-1
        ans = mid
    elif count > M :  #M보다 더 많은 DVD가 나온 경우 DVD의 크기를 더 키워야 한다.
        Min = mid+1

print(ans)