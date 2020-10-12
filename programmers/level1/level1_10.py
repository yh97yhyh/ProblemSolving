'''
< 문자열 다루기 기본 >
'''

s1 = "a234"
s2 = "1234"

def solution(s):
    if (s.isdigit() == True) and (len(s) == 4 or len(s) == 6):
        return True
    else:
        return False

print(solution(s1))
print(solution(s2))