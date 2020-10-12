'''
< 나누어 떨어지는 숫자 배열 >
'''

arr1, divisor1 = [5, 9, 7, 10], 5
arr2, divisor2 = [2, 36, 1, 3], 1
arr3, divisor3 = [3, 2, 6], 10

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()

    return answer

print(solution(arr1, divisor1))
print(solution(arr2, divisor2))
print(solution(arr3, divisor3))