'''
구현
시간
'''

hour = int(input())

count = 0
sec = 60
minute = 60
for h in range(hour + 1):
    for m in range(minute):
        for s in range(sec):
            newTime = []
            newTime.append(str(h))
            newTime.append(str(m))
            newTime.append(str(s))
            newTime = ''.join(newTime)
            if '3' in newTime:
                count += 1
                # print(newTime)

print(count)