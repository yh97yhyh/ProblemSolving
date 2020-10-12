'''
< 체육복 >
'''


n1, n2, n3 = 5, 5, 3
lost1, lost2, lost3 = [2, 4], [2, 4], [3]
reserve1, reserve2, reserve3 = [1, 3, 5], [3], [1]

# 오답
# def solution2(n, lost, reserve):
#     lend = []
#     reserve = list(set(reserve) - set(lost))
#     lost = list(set(lost) - set(reserve))
#     for i in range(len(reserve)):
#         for j in range(len(lost)):
#             if abs(reserve[i] - lost[j]) == 1:
#                 lend.append(lost[j])
#                 break
#
#     return n - len(list(set(lost) - set(lend)))

def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n - len(set_lost)


print(solution(n1, lost1, reserve1))
print(solution(n2, lost2, reserve2))
print(solution(n3, lost3, reserve3))