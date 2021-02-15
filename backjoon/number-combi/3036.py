'''
링
'''

import sys
from fractions import Fraction

n = int(sys.stdin.readline())

rings = list(map(int, sys.stdin.readline().split()))

answers = []
for i in range(1, n):
    answer = Fraction(rings[0], 1) / Fraction(rings[i], 1)
    print('{}/{}'.format(answer.numerator, answer.denominator))