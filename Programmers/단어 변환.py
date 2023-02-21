from collections import deque
#단어 w1과 w2의 알파벳이 몇 개 같은지를 확인하는 함수
def similarity(w1, w2) :
    count = 0
    for a,b in zip(w1,w2) :
        if a==b :
            count+=1
    return count

def solution(begin, target, words):
    if target not in words :
        return 0
    queue = deque([(begin,0)])
    l = len(begin)

		#BFS 
    while queue :
        word, t = queue.popleft()
        if word == target :   #변환이 완료됨
            break
        for w in words :
            if similarity(word,w) == l-1 : #알파벳이 1개 다른 경우에 수행
                queue.append((w,t+1))
                words.remove(w)  #한 번 검사한 단어는 다시 검사하지 않기 위해 지운다.
    if word != target :  #target이 words에 있지만 변환할 수 없는 경우 고려
        return 0

    return t