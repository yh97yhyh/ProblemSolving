'''
< 문자열 내 p와 y의 개수 >
'''

s1 = "pPoooyY"
s2 = "Pyy"

def solution(s):
    countP = countY = 0
    countP = s.count('p') + s.count('P')
    countY = s.count('y') + s.count('Y')
    if countP == countY:
        return True
    else:
        return False

print(solution(s1))
print(solution(s2))