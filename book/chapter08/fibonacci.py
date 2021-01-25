'''
피보나치 수열 (재귀적)
Top-down
'''

# 한 번 계산된 결과를 Memoization하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    # print('f({0})'.format(x), end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))