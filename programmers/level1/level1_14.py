'''
< 수박수박수박수박수박수? >
'''

n1, n2 = 3, 4

def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 != 0:
            answer.append('수')
        elif i % 2 == 0:
            answer.append('박')
    answer = ''.join(answer)
    return answer

print(solution(n1))
print(solution(n2))