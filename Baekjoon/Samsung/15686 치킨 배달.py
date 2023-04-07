def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:], r-1):
                yield [arr[i]] + next

N, M = map(int, input().split())
board = []
home, chicken = [], []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] == 1:
            home.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))
            
nCr = combination(chicken, M)   #가능한 치킨집 조합
result, ans = 0, 1e9

for c in nCr:
    c.sort()
    for x,y in home:
        minimum = 1e9
        for i,j in c:
            d = abs(x-i) + abs(y-j)
            if minimum > d:
                minimum = d

        result += minimum
    ans = min(ans, result)
    result = 0
print(ans)