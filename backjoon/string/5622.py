'''
다이얼
'''

import sys

dials = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

string = list(sys.stdin.readline())

sum = 0
for s in string:
    for d in dials[3:]:
        if d.find(s) != -1:
            # print(d, s)
            sum += dials.index(d)

print(sum)