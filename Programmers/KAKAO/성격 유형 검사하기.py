import math

def solution(survey, choices):
    answer = ''
    char = ("R", "T", "C", "F", "J", "M", "A", "N")
    char_dict = dict.fromkeys(char, 0)
    
    for sur, cho in zip(survey, choices) :
        if cho < 4 :    #비동의인 경우
            char_dict[sur[0]] += math.ceil(1/cho * 3)
        else :          #동의인 경우
            char_dict[sur[1]] += cho % 4
        
    for j in range(0,8,2) :
        if (char_dict[char[j]] >= char_dict[char[j+1]]) :
            answer += char[j]
        else :
            answer += char[j+1]
        
    return answer