'''
문제 설명
정수 배열 numbers가 주어집니다.
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''

n1 = [2, 1, 3, 4, 1]
n2 = [5, 0, 2, 7]

def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result.append(numbers[i] + numbers[j])

    result = list(set(result))
    result.sort()
    return result

print(solution(n1))
print(solution(n2))