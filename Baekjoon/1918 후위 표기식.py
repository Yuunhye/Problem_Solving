def postfix_notation(expression) :
    operator = []
    result = ''
    count = 0
    for i in expression :
        if count == 0 and i == "(" :
            temp = []
            count += 1
        elif count>0 :
            if i == ")" :
                count -= 1
            elif i == "(" :
                count += 1
            if count == 0 :
                result += postfix_notation(temp)
                if operator and (operator[-1] == "*" or operator[-1] == "/") :
                    result += operator.pop()
            else : 
                temp.append(i)
        elif i =="+" or i =="-" :
            if operator and (operator[-1] == "+" or operator[-1] =="-") :
                result += operator.pop()
            operator.append(i)
        elif i =="*" or i =="/" :
            operator.append(i)

        else :  #숫자인 경우
            result += i
            if operator and (operator[-1] == "*" or operator[-1] == "/") :
                result += operator.pop()
    if operator :
        result += operator.pop()
    return result

expression = list(input())
print(postfix_notation(expression))

#다른 사람 풀이 - 연산자 사이의 우선순위 이용
"""
import sys
input = sys.stdin.readline

letters = input()
stack = []
ans = ''
for i in letters:
    if i.isalpha():
        ans += i
    else:
        if i == '(':
            stack.append(i)

				# 먼저 들어오고 같은 우선순위에 있는 */는 ans에 넣어줌
        elif i == '*' or i == '/': 
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(i)

				#이보다 낮은 우선 순위가 없어서 연산자이면 전부 ans에 넣어줌
        elif i == '+' or i == '-': 
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)
				
				# 닫음 괄호와 열음 괄호 사이에 있는 연산자들 전부 반환
        elif i == ')': 
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()

while stack:
    ans += stack.pop()
print(ans)
"""