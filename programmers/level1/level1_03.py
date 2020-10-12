'''
< 가운데 글자 가져오기 >
'''

s1 = "abcde"
s2 = "qwer"

def solution(s):
    length = len(s)
    half = int(length / 2)
    answer = ''
    if length % 2 == 1:  # 홀수
        answer = s[half]
    else:
        answer = s[half-1:half+1]

    return answer

print(solution(s1))
print(solution(s2))