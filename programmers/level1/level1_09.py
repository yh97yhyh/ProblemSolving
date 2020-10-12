'''
< 문자열 내림차순으로 배치하기 >
'''

s = "Zbcdefg"

def solution(s):
    s = list(s)
    s.sort(reverse=True)
    s = ''.join(s)
    return s

print(solution(s))