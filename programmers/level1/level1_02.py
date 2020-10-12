'''
< 2016년 >
'''

a, b = 5, 24
a2, b2 = 2, 1

def solution(a, b):
    day = 0
    date = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for m in month[0:a-1]:
        day += m

    day += b
    return date[(day % 7)]


print(solution(a, b))
print(solution(a2, b2))