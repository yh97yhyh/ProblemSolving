'''
< 소수 찾기 >
한자리 숫자가 적힌 종이 조각이 흩어져있습니다.
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

- numbers는 길이 1 이상 7 이하인 문자열입니다.
- numbers는 0~9까지 숫자만으로 이루어져 있습니다.
- 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
'''

n1 = "17"
n2 = "011"

import itertools

def solution(numbers):
    perms =[]
    for i in range(1, len(numbers)+1):
        els = [list(x) for x in itertools.permutations(numbers, i)]
        perms.extend(els)
    for i in range(len(perms)):
        perms[i] = int(''.join(perms[i]))
    perms = list(set(perms))
    print(perms)
    answer = count_prime(perms)
    return answer

def count_prime(li):
    cnt = 0
    for number in li:
        is_prime = True
        if number != 1 and number != 0:
            for f in range(2, number):
                if number % f == 0:
                    is_prime = False
        else:
            is_prime = False
        if is_prime:
            cnt += 1
    return cnt

# print(solution(n1))
print(solution(n2))

# 합친 코드
# def solution2(numbers):
#     combs =[]
#     count = 0
#     for i in range(1, len(numbers)+1):
#         els = [list(x) for x in itertools.permutations(numbers, i)]
#         combs.extend(els)
#     for i in range(len(combs)):
#         combs[i] = int(''.join(combs[i]))
#     combs = list(set(combs))
#
#     for number in combs:
#         is_prime = True
#         if number != 1 and number != 0:
#             for f in range(2, number):
#                 if number % f == 0:
#                     is_prime = False
#         else:
#             is_prime = False
#         if is_prime:
#             count += 1
#     return count