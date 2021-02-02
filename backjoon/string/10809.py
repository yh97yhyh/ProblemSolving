'''
알파벳 찾기
'''

import sys

arr = sys.stdin.readline()
alphas = [-1 for i in range(26)] # 알파벳 갯수만큼

for i in range(len(arr)-1):
    index = arr.find(arr[i]) # 처음 등장하는 위치
    alphas[ord(arr[i])-97] = index

for alpha in alphas:
    print(alpha, end=' ')