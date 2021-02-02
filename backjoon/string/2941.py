'''
크로아티아 알파벳
'''

import sys
string = sys.stdin.readline()
string = string.replace('\n', '')

croatias= ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in croatias:
    string = string.replace(c, '*')

print(len(string))