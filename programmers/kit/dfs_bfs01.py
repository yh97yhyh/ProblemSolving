
n = [1, 1, 1, 1, 1]
t = 3

def solution(numbers, target):
    answer = 0

    def operator(numbers, target, idx=0):
        if idx < len(numbers):
            operator(numbers, target, idx+1)

            numbers[idx] *= -1
            operator(numbers, target, idx+1)

        elif sum(numbers) == target:
            nonlocal answer
            answer += 1

    operator(numbers, target)
    return answer

print(solution(n, t))