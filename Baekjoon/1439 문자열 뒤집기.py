S = input()
a = S.count('01') #S에 '01'이 몇 개 있는지 return
b = S.count('10') #S에 '10'이 몇 개 있는지 return
if a<b :
    print(b)
else :
    print(a)