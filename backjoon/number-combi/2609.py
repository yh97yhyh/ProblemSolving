'''
최대공약수와 최대공배수
'''

import sys

a, b = map(int, sys.stdin.readline().split())

# 최대공약수
def gcd(a, b):
    while b: # b가 0이 될 때까지 반복
        a, b = b, a % b
    return a
print(gcd(a, b))

# 최소공배수 (a, b의 곱에서 최대공약수를 나누어준 것과 같음)
def lcm(a, b):
    return a * b // gcd(a, b)
print(lcm(a, b))