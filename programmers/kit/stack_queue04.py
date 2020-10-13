'''
< 프린터 >
'''

p1 = [2, 1, 3, 2]
l1 = 2
p2 = [1, 1, 9, 1, 1, 1]
l2 = 0


def solution(priorities, location):
    printList = [i for i in range(len(priorities))]
    sortedPrintList = []

    while priorities:  # 제일 높은 우선순위일 때
        if priorities[0] == max(priorities):
            sortedPrintList.append(printList.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            printList.append(printList.pop(0))
    return sortedPrintList.index(location) + 1

print(solution(p1, l1))
print(solution(p2, l2))