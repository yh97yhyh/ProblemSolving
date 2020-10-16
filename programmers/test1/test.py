'''
< 직사각형 좌표 >
'''

def solution(v):
    xList = []
    yList = []
    answer = []
    for x, y in v:
        xList.append(x)
        yList.append(y)
    for x in xList:
        if xList.count(x) == 1:
            answer.append(x)
            break
    for y in yList:
        if yList.count(y) == 1:
            answer.append(y)
            break

    return answer