'''
< 두 정수 사이의 합 >
'''

a1, b1 = 3, 5
a2, b2 = 3, 3
a3, b3 = 5, 3

def solution(a, b):
    numList = []
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        numList.append(i)

    return sum(numList)

print(solution(a1, b1))
print(solution(a2, b2))
print(solution(a3, b3))