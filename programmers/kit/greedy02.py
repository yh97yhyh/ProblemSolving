'''
< 큰 수 만들기 >
'''


n1, k1 = "1924", 2
n2, k2 = "1231234", 3
n3, k3 = "4177252841", 4

from itertools import combinations

def solution(number, k):
    answer = []
    combis = list(combinations(list(number), len(number) - k))
    for combi in combis:
        combi = ''.join(combi)
        answer.append(combi)
    print(answer)
    return max(answer)

# def solution(number, k):
#     answer = []
#     number = list(number)
#     length = len(number) - k
#     cnt = 0
#     while len(answer) < length:
#         maxNum = max(number)
#         i = number.index(maxNum)
#         print(maxNum)
#         if len(number[i:]) >= length - len(answer):
#             answer.append(maxNum)
#         number.pop(i)


    return answer



print(solution(n1, k1))
print(solution(n2, k2))
print(solution(n3, k3))