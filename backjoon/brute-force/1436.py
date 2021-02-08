'''
영화감독 숌
'''

import sys

n = int(sys.stdin.readline())
number = 666

while(n):
    if '666' in str(number):
        n -= 1
    number += 1

print(number-1)

'''
n = 2일 때, number의 값은 while문에서 666부터 증가
number = 666이니 n은 -1로 인해 1이 됨.
number은 667부터 1씩 증가하고 1666일 때, n은 0이 되어 while문이 종료.
'''