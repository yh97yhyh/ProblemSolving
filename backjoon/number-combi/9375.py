'''
패션왕 신해빈
'''

import sys

roof = int(sys.stdin.readline())

for i in range(roof):
    num = int(sys.stdin.readline())
    clothes = []
    clothesDict = {}
    answer = 1
    for j in range(num):
        name, kind = sys.stdin.readline().split()
        clothes.append([name, kind])
    for name, kind in clothes:
        if kind in clothesDict.keys():
            clothesDict[kind].append(name)
        else:
            clothesDict[kind] = [name]
    for kind in clothesDict:
        answer = answer * (len(clothesDict[kind])+1)
    answer = answer - 1
    print(answer)
