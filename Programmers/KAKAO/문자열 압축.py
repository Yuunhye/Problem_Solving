def slice(s, n) :
    slices = list()
    rest = len(s) % n
    for i in range(0,len(s)-rest,n) :
        slices.append(s[i:i+n])
    if (rest != 0) :
        slices.append(s[-rest:])

    return slices

def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2 + 1) :
        slices = slice(s, i)
        
        if len(set(slices)) != len(slices) :
            count = 1
            result = ''
            for a, b in zip(slices, slices[1:]+['']) :
                if a == b :
                    count += 1
                else :
                    if count > 1 :
                        result += str(count)
                    result += a
                    count = 1
            if answer > len(result) :
                answer = len(result)
    return answer