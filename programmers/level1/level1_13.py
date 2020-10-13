'''
< 소수 찾기 >
효율성 실패
'''

n1, n2 = 10, 5

def isprime(n):
    if n == 2:
        return True
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def solution(n):
    cnt = 0
    if n >= 2:
        cnt += 1
    for i in range(3, n+1, 2):
        if i == 1:
            continue
        if isprime(i):
            cnt += 1
    return cnt

print(solution(n1))
print(solution(n2))