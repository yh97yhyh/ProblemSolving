'''
< 주식가격 >
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.
'''

p1 = [1, 2, 3, 2, 3]
p2 = [1, 2, 3, 2, 3, 1]
p3 = [3, 1]

# 효율성 테스트 실패
def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = prices[i:len(prices)-1]
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                time = prices[i:j]
                break
        answer.append(len(time))
    return answer

# 정답
def solution2(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            count = count + 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
    return answer

print(solution2(p1))
print(solution2(p2))
print(solution2(p3))
