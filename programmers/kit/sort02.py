'''
< 가장 큰 수 >
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
예를 들어, 주어진 정수가 [6, 10, 2]라면
[6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

- numbers의 길이는 1 이상 100,000 이하입니다.
- numbers의 원소는 0 이상 1,000 이하입니다.
- 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
'''

num1 = [6, 10, 2]
num2 = [3, 30, 34, 5, 9]

# 오답
# def solution(numbers):
#     numStr = []
#     for number in numbers:
#         numStr.append(str(number))
#     numStr.sort(reverse=True)
#     for i, j in zip(numStr, numStr[1:]):
#         if i[0] == j[0] and len(i) > len(j):
#             n = numStr.index(i)
#             temp = numStr[n]
#             numStr[n] = numStr[n+1]
#             numStr[n+1] = temp
#     return(''.join(numStr))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

print(solution(num1))
print(solution(num2))

'''
python에서 join 함수는 배열을 특정 문자로 구분하여 문자열로 변환해주는 함수이다.
근데 왜 string을 int로 변환하고 다시 string으로 변환해서 리턴하는지 이해가 안됐는데
그렇게 join만 사용하면 0일 때가 문제다.
[0,0,0,0] 을 input으로 넣는다면 '0000'이 리턴되므로 int로 변환해서 '0'으로 바꿔야 한다.
그리고 오버플로우 방지를 위해 다시 str으로 변환해야 하는 것!!!!
'''