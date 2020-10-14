
n = [1, 1, 1, 1, 1]
t = 3

def solution2(numbers, target):
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

def solution(numbers, target):
    answer = [0]
    for i in numbers:
        tmp = []
        for j in answer:
            tmp.append(j+i)
            tmp.append(j-i)
        answer = tmp
        print(tmp)
    return answer.count(target)


print(solution(n, t))