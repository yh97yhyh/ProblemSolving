'''
구현
상하좌우
'''
import switch as switch

n = int(input())
move = input()
move = ''.join(move.split())

x = 1
y = 1
for m in move:
    if m == 'L':
        if y == 1:
            continue
        else:
            y -= 1
    elif m == 'R':
        if y == n:
            continue
        else:
            y += 1
    elif m == 'U':
        if x == 1:
            continue
        else:
            x -= 1
    elif m == 'D':
        if x == 5:
            continue
        else:
            x += 1

print(x, y)




