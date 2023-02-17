#https://school.programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    times.sort()
    Min, Max = 1, times[-1]*n

    while(Min <= Max) :
        mid = (Min+Max)//2  #모든 사람이 심사를 받는 데 걸리는 시간
        count = 0
        for x in times :
            count += mid//x

        if count < n : 
            Min = mid + 1
        else :
            Max = mid - 1
            answer = mid
    return answer