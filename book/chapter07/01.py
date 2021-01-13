'''
부품 찾기
'''

def solution(havaArr, needArr):
    for num in needArr:
        if num in havaArr:
            print('yes', end=' ')
        else:
            print('no', end=' ')

n = int(input())
havaArr = list(map(int, input().split()))
m = int(input())
needArr = list(map(int, input().split()))

solution(havaArr, needArr)