
p1 = [4, 1, 4, 7, 6]
p2 = [13, 7, 3, 7, 5, 16, 12]
p3 = [0, 0]

def solution(price):
    answer = []
    for i in range(len(price)):
        cnt = 0
        for j in range(i+1, len(price)): # i+1의 index부터 끝까지 비교
            cnt += 1
            if price[i] < price[j]:
                answer.append(cnt)
                break

            if j == len(price)-1: # price 리스트의 끝까지 가도 이득이 없으면
                answer.append(-1)
                break

    answer.append(-1) # price 리스트의 마지막값은 항상 이득이 없다
    return answer

print(solution(p1))
print(solution(p2))
print(solution(p3))




