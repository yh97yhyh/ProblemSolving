'''
구현
왕실의 나이트
'''

data = input()
x = int(ord(data[0])) - int(ord('a')) + 1
y = int(data[1])

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)]

count = 0
for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]
    if next_x >= 1 and next_x <= 8 and next_y >= 1 and next_y <=8:
        count += 1

print(count)