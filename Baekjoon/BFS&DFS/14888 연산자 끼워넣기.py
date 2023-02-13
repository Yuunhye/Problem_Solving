#DFS 풀이 -- 다른 사람 풀이
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:  #+가 남아있는 경우
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)

#순열 풀이 -- 내 풀이
"""
from itertools import permutations
import sys
input = sys.stdin.readline  #이거 없으면 시간초과 남

N = int(input())
num = [int(x) for x in input().split()]
operator = list()
lists = [int(y) for y in input().split()]
Max, Min = -(10**9),10**9   #연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나온다고 하였음
k = 0
for i in lists :
    for j in range(i) :
        operator.append(k)  #0: +, 1: -, 2: *, 3: //
    k += 1

P = set(list(permutations(operator, len(operator))))
for p in P :
    res = 0
    for n,op in zip(num, tuple(' ')+p) :
        if op == ' ' :
            res += n
        elif op == 0 :  #+인 경우
            res += n
        elif op == 1 :  #-인 경우
            res -= n
        elif op == 2 :  #*인 경우
            res *= n 
        else :          #//인 경우
            if res>=0 :
                res //= n
            else :
                res = -(abs(res) // n)
    Max = max(Max, res)
    Min = min(Min, res)

print(Max)
print(Min)
"""