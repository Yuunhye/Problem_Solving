from collections import defaultdict
def solution(tickets) :
    tickets.sort()  #같은 출발지인 경우 도착지가 알파벳 순서로 정렬됨
    graph = defaultdict(list) 
    
    for a,b in tickets :    #각 공항(key)에서 갈 수 있는 모든 공항을 value로 저장
        graph[a].append(b)
    
		#DFS
    stack = ["ICN"]
    path = []
    while stack :
        top = stack[-1]

				#가다가 막힌 경우 되돌아 가서 다른 경로로 감
        if top not in graph or len(graph[top]) == 0 : 
            path.append(stack.pop())

        else : 
            stack.append(graph[top][0])
            graph[top] = graph[top][1:]

    return path[::-1]